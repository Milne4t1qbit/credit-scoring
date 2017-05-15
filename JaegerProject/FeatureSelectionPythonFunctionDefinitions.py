'''
Created on Apr 16, 2017   (c) 1QBit
Python Source for the Optimal Feature Selection Notebooks on qdk.1qbit.com
@author: Andrew Milne
There are four main components (and room for improvement in all of them):
- the *findJumpByHash* function to calculate the hash of the subset list, so that changes to the subset list 
  are "perceived" as a jump in an integer value,
- the *subsetRecursiveFinder* function to perform the search recursively,
- the *subsetFinder* function to "wrap" the basic recursive search, perform type conversion, etc.
  Inputs are pandas dataframes as returned by the corr() function
- the *subsetDataMediator* class, whose instances can be passed by reference, which allows a setter to 
  set values at a low level of the recursion for use at a higher level. 
  The idea is to avoid unnecessary calls to the solver simply because results at a low level 
  were not reported.  It's an instance of the MEDIATOR DESIGN PATTERN, with the mediator
  reference passed by value in the function calls.
'''
import numpy    as np                       # @UnusedImport (annotation for Eclipse/PyDev)
import scipy    as sp                       # @UnusedImport
from scipy import stats                     # @UnusedImport
from math  import floor                     # @UnusedImport
import pandas                               # @UnusedImport
import qdk

########################### FUNCTION DEFINITIONS ###########################
def makeE31Q(rhoMatrix, yVector, alphaParameter):
#     debug=False
    # M rows, N columns
    rhoM=rhoMatrix.shape[0]; rhoN=rhoMatrix.shape[1]
    blockGood=(rhoM==rhoN)
    if not blockGood : return "The rhoMatrix argument was NOT square."
 
    trueQm=np.eye(rhoM) # easy way to get a matrix we can fill
    for i in range(rhoM):
        for j in range(rhoM):
            if( i==j ):
            #then
                trueQm[i,j]=alphaParameter*abs(yVector[i])
            else:
                trueQm[i,j]=-(1-alphaParameter)*abs(rhoMatrix[i,j])
            #endif
        #endfor
    #endfor
    return trueQm
#enddef

def polyFromE31QMatrix(blockMatrix):
    blockDebug= False
    blockBuilder= qdk.QuadraticBinaryPolynomialBuilder()
    # M rows, N columns
    blockM=blockMatrix.shape[0]; blockN=blockMatrix.shape[1]
    blockGood=(blockM==blockN)
    if not blockGood : return "Not a square matrix."
    for i in range(blockM):
        for j in range(blockN):
            blockCoeff=blockMatrix[i,j]
            if blockDebug: print i, j, "  ", blockCoeff
            blockBuilder.add_term(blockCoeff,i,j)
        #endfor
        
    #endfor
    blockPoly=blockBuilder.build_polynomial()
    if blockDebug : print "Matrix processed completely.  Polynomial follows: "
    if blockDebug : print blockPoly
    return blockPoly
#enddef block
