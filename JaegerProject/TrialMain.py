'''
Created on Oct 25, 2016. (c) 1QBit.
@author: Andrew Milne
'''
################################################
if __name__ == '__main__': pass
################################################
print "Starting Jaeger Project TrialMain.py"

import string                               # @UnusedImport
import csv                                  # @UnusedImport
import os                                   # @UnusedImport
import logging                              # @UnusedImport
import numpy    as np                       # @UnusedImport
import scipy    as sp                       # @UnusedImport
import networkx as nx                       # @UnusedImport
import matplotlib        as mpl             # @UnusedImport
import matplotlib.pyplot as plt             # @UnusedImport
import pandas   as pd                       # @UnusedImport

from scipy import stats                     # @UnusedImport
from math  import floor                      # @UnusedImport
######## Library datetime is brittle and error-prone. So ignore the warning.
from datetime import timedelta,datetime,time, date  # @UnusedImport
######## Back to normal.
plt.plot()
import qdk
print "Using QDK version "+ qdk.algorithms.__version__

df3 = pd.DataFrame({ 
 'A' : 1., 
 'B' : pd.Timestamp('20130102'), 
 'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
 'D' : np.array([3] * 4,dtype='int32'),
 'E' : pd.Categorical(["test","train","test","train"]),
 'F' : 'foo' })

# print df3
# df3.plot()
# plt.show()

df1=pd.read_csv("./data/au_data_pre_with_headers.csv")
print( "Read file with shape "+str(df1.shape)+", containing "+str(df1.size)+" elements.")
cm1=df1.corr()


import sklearn
from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier()

x=np.array([[1,2,3],[3,4,5]])

y=np.ndarray(1)

# the following line has two purposes: (1) to hold a breakpoint so that the debugger can be used to
# examine the internal variables before termination, and (2) to show in the console that control has 
# been returned from the matplotlib windows, because when there's a lot of them, it can be hard to tell.
print ("And that's all she wrote.")
# and so it ends.
