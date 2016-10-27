'''
Created on Oct 25, 2016. (c) 1QBit.
@author: Andrew Milne
'''
################################################
if __name__ == '__main__': pass
################################################
print "Hello from the TrialMain Module"

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

from qdk.algorithms import *                # @UnusedWildImport
from qdk.binary_polynomial import *         # @UnusedWildImport
from qdk.common_solver_interface import *   # @UnusedWildImport

print "Imports completed."

df3 = pd.DataFrame({ 
 'A' : 1., 
 'B' : pd.Timestamp('20130102'), 
 'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
 'D' : np.array([3] * 4,dtype='int32'),
 'E' : pd.Categorical(["test","train","test","train"]),
 'F' : 'foo' })

print df3
df3.plot()
plt.show()



