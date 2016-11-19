'''
Created on Nov 18, 2016  (c) 1QBit
@author: Andrew Milne
There are four main components (and room for improvement in all of them):
- function to calculate the hash of the subset list, so that changes to the subset list 
  are "perceived" as a jump in an integer value,
- function to perform the search recursively,
- function to "wrap" the basic recursive search, perform type conversion, etc.
- collector class, whose instances can be passed by reference, which allows a setter to 
  set values at a low level of the recursion for use at a higher level. 
  The idea is to avoid unnecessary calls to the solver simply because results at a low level 
  were not reported.  It's an instance of the MEDIATOR DESIGN PATTERN, with the mediator
  reference passed by value in the function calls.
'''
import numpy    as np                       # @UnusedImport (annotation for Eclipse/PyDev)
import scipy    as sp                       # @UnusedImport
from scipy import stats                     # @UnusedImport
from math  import floor                     # @UnusedImport
# import jaeger
from jaeger.JaegerUtilityFunctions   import makeE31Q
from jaeger.JaegerUtilityFunctions   import polyFromMatrix
import qdk

class subsetDataMediator(object):
    def __init__(self,corrMatrix,corrVector,tolerance,recursiveFunctionRef): 
        self.thisCorrMatrix=corrMatrix
        self.thisCorrVector=corrVector
        self.xTolerance=tolerance
        self.yTolerance=0.5 
        self.thisJumpValue=None
        self.thisSubsetRecord=None
        self.jumpList=[]
        self.subsetList=[]
        self.plottablePointList=[]
        self.thisRecursiveFunctionRef=recursiveFunctionRef
        self.thisVerbosity=True
        return
    #enddef
    def getCorrMatrix(self):  return self.thisCorrMatrix
    def getCorrVector(self):  return self.thisCorrVector
    def getXTolerance(self):  return self.xTolerance
    def getYTolerance(self):  return self.yTolerance
    def getFunctionRef(self): return self.thisRecursiveFunctionRef
    def getVerbosity(self):   return self.thisVerbosity

    def setJumpValue(self, jumpValue): self.thisJumpValue=jumpValue;           return
    def setSubsetRecord(self,subset):  self.thisSubsetRecord=subset;           return
    def appendJump(self,jumpElement):  self.jumpList.append(jumpElement);      return
    def appendSubset(self, subset):    self.subsetList.append(subset);         return
    def appendPoint(self, point):      self.plottablePointList.append(point);  return
    
    def getSubsetRecord(self):     return self.thisSubsetRecord
    def getJumpList(self):         return self.jumpList
    def getSubsetList(self):       return self.subsetList
    def getPlottablePoints(self):  return self.plottablePointList
#endclass

def findJumpByHash(candAlpha, subsetMediatorObjectRef):
    cm=subsetMediatorObjectRef.getCorrMatrix()
    cv=subsetMediatorObjectRef.getCorrVector()
    fjQMatrix=makeE31Q(cm,cv,candAlpha)
    fjPoly=polyFromMatrix(fjQMatrix)
    fjPoly.multiply_by_factor(-1)  # mult is done in place
    fjSolver = qdk.GrayExhaustiveSolver()
    fjSolver.disable_timeout()
    fjSolutionList=fjSolver.minimize(fjPoly)
    fjLowEnergySolution=fjSolutionList.get_minimum_energy_solution()
    fjConfig=fjLowEnergySolution.configuration
    fjSubsetList=np.argwhere(fjConfig.values()).flatten().tolist()
    fjHash=hash(tuple(fjSubsetList))
    subsetMediatorObjectRef.setSubsetRecord(fjSubsetList)
    return fjHash
#enddef

def subsetRecursiveFinder(xL,xR,subsetMediatorObjectRef):
    # in its present form, this makes a lot of redundant calls to func
    # todo: revise
    verbose= subsetMediatorObjectRef.getVerbosity() 
    func=    subsetMediatorObjectRef.getFunctionRef()
    tolX=    subsetMediatorObjectRef.getXTolerance()
    tolY=    subsetMediatorObjectRef.getYTolerance()
    # *ensure* that values are copied to local instances
    xLL=xL; xRR=xR;   
    # always call the RHS last, so that the recorded subset is after any jump
    yLL=func(xLL, subsetMediatorObjectRef)
    yRR=func(xRR, subsetMediatorObjectRef)
  
    if (verbose): print "Called for Interval xLL="+str(xLL)+" to xRR="+str(xRR) 

    # do not split the interval if the function is equal at both ends
    if(abs(yLL-yRR)<tolY): 
        if (verbose): print "NO CHANGE IN FUNCTION VALUE ON THIS INTERVAL"  
        return 
    #endif
    
    # do not split the interval below the tolerance
    if(abs(xRR-xLL)<=tolX):           
        if (verbose): 
            print "X TOL LIMIT: func("+str(xLL)+")="+str(yLL)+", func("+str(xRR)+")="+str(yRR)  
        #endif
        #report a jump if one exists
        if(abs(yLL-yRR)>tolY):
            sr=subsetMediatorObjectRef.getSubsetRecord()
            sc=len(sr)
            subsetMediatorObjectRef.appendSubset(sr)
            subsetMediatorObjectRef.appendJump(xRR)
            subsetMediatorObjectRef.appendPoint([xRR,sc])
            print "SUBSET CHANGE AT alpha="+str(xRR).ljust(10," ")+" CARDINALITY: "+str(sc)
            return 
        else:
            if(verbose): print "CONTINUING"
            return
        #endif
    #endif
    xmid=0.5*(xLL+xRR)
    subsetRecursiveFinder(xLL,xmid, subsetMediatorObjectRef)
    subsetRecursiveFinder(xmid,xRR, subsetMediatorObjectRef)
    return 
#enddef

def subsetFinder(dfCorrMatrix,dfCorrVector,tol):
    cMatrix=dfCorrMatrix.as_matrix()
    cVector=dfCorrVector.as_matrix()
    sdm=subsetDataMediator(cMatrix, cVector, tol, findJumpByHash)
    # At this point we simply assume that we are interested in all of [0,1]
    # However, the recursive finder looks for jump points inside the interval.
    # We have to add the points at the ends explicitly
    findJumpByHash(0.0,sdm)
    sr=sdm.getSubsetRecord()
    sc=len(sr)
    sdm.appendSubset(sr)
    sdm.appendJump(0.0)
    sdm.appendPoint([0.0, sc])
    
    subsetRecursiveFinder(0.0, 1.0, sdm)  # the cheese stands alone!
    
    # The jump is reported on the rhs of the interval where the recursion stops,
    # so it's possible that 1.0 may be picked up by the recursive search, especially
    # when the tolerance is large. In the test, we use tol/2.0 just in case the  
    # floating point arithmetic has multißplied so many times by 0.5 that the jump point 
    # is off by a small amount.  The "ideal" test would be rightmost exactly tol away from 1.0.
    rightmostRecordedJump=sdm.getJumpList()[-1]
    if(abs(rightmostRecordedJump-1.0)>tol/2.0):
        findJumpByHash(1.0,sdm)
        sr=sdm.getSubsetRecord()
        sc=len(sr)
        sdm.appendSubset(sr)
        sdm.appendJump(1.0)
        sdm.appendPoint([1.0, sc])
        if( sdm.getVerbosity()): 
            print "Rightmost recorded jump was: "+str(rightmostRecordedJump)
            print "Extending jump points to 1.0"
        #endif
    #endif
    if( sdm.getVerbosity()):
        print "Plottable Points"
        print sdm.getPlottablePoints()
        print ""
        print "Jump List (alphas just after a jump, within the tolerance)"
        print sdm.getJumpList()
        print "Subset List"
        print sdm.getSubsetList()
    #endif
    return sdm  # todo: this could be changed if the sdm was passed to the constructor
#enddef