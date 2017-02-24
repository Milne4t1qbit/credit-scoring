'''
Created on Oct 25, 2016. (c) 1QBit.
@author: Andrew Milne
'''
#print "Hello from the Jaeger Driver Module"
import numpy    as np                       # @UnusedImport (annotation for Eclipse/PyDev)
import scipy    as sp                       # @UnusedImport
# import networkx as nx                       # @UnusedImport
# import matplotlib         as mpl            # @UnusedImport
# import matplotlib.pyplot  as plt            # @UnusedImport
# import matplotlib.path    as mpath          # @UnusedImport
# import matplotlib.lines   as mlines         # @UnusedImport
# import matplotlib.patches as mpatches       # @UnusedImport
# from   matplotlib.collections import PatchCollection  # @UnusedImport
import pandas   as pd                       # @UnusedImport
# import math                                 # @UnusedImport
# from  scipy import stats                    # @UnusedImport
# from  math  import floor                    # @UnusedImport
# import itertools                            # @UnusedImport
import sklearn                              # @UnusedImport
from   sklearn                  import preprocessing
from   sklearn.svm              import  SVC # @UnusedImport
from   sklearn.model_selection  import  cross_val_score   # @UnusedImport
import os                                   # @UnusedImport
import sys                                  # @UnusedImport
import jaeger                               # @UnusedImport
import jaeger.JaegerReferenceData           # @UnusedImport
# import qdk                                  # @UnusedImport
import time
# print "Using QDK version "+ qdk.algorithms.__version__

# the following works only in Jupyter (iPython)
# %matplotlib inline

dfau=pd.read_csv("./data/au_data_pre_with_headers.csv")
print("Expecting shape (690, 15), received "+str(dfau.shape))
featuresOnly=dfau.drop("A15",1)
classOnly=dfau["A15"]

nRows=len(jaeger.JaegerReferenceData.huangFeatureListList)
mY=classOnly.as_matrix()
scoresList=[]; timeList=[]
nFold=10
print("Row   Alpha         OCAR     SVC OCAR ("+str(nFold)+"-fold)     Time (s)   Feature Subset  ")

# print("Row   Features        OCAR     SVC OCAR ("+str(nFold)+"-fold)    Time (s)   Feature Subset  ")

# print("Row   Features        OCAR     SVC OCAR ("+str(nFold)+"-fold)    Time (s)   Feature Subset  ")

# skip the empty set in position zero
for iRow in range(1,nRows):
    start=time.time()
    fList=         jaeger.JaegerReferenceData.huangFeatureListList[iRow]
    alpha=         jaeger.JaegerReferenceData.huangAlpha[iRow]
    ocar  =        jaeger.JaegerReferenceData.huangOCAR[iRow]
    subsetString = str(fList)  # make this nicer later
    nFeatures=len(fList)
    diX=featuresOnly[fList]
    floatX=(diX.as_matrix()).astype(np.float64)
    mX=preprocessing.scale(floatX)
#     mX=floatX
    #mCls=SVC(kernel="rbf") # get a fresh one, I hope
    
    # mCls.fit(mX,mY)
    mScores=cross_val_score(SVC(kernel="poly",tol=0.001),mX,mY,cv=nFold,n_jobs=-1)

    
    mValues=mScores.tolist()
    scoresList.append(mValues)

    msm=mScores.mean()
    msu=2*mScores.std() 
    end=time.time()
    dt=end-start
    timeList.append(dt)
    print("%2d    %0.9f   %0.4f   %0.4f (+/- %0.4f)    %8f   %s" 
          % (iRow, alpha, ocar, msm, msu, dt, subsetString )   )
 
#     print("%2d      %2d           %0.4f   %0.4f (+/- %0.4f)    %8f " 
#           % (iRow, nFeatures, ocar, msm, msu, dt )   )

#     print msm 
#endfor
# print " "
for i in range(len(scoresList)): print ("i="+str(i)+", max="+str(max(scoresList[i]))+"    "+str(scoresList[i]))
# print " "
# the following line has two purposes: (1) to hold a breakpoint so that the debugger can be used to
# examine the internal variables before termination, and (2) to show in the console that control has 
# been returned from the matplotlib windows, because when there's a lot of them, it can be hard to tell.
print ("And that's all she wrote.")
# and so it ends.
