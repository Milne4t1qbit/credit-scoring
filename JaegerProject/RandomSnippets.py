'''
Created on Dec 7, 2016

@author: ulysses
'''
def getIfNameHasEquals(s):
    position=s.find("=")
    if(-1==position): return None
    start= 0
    end=   position
    substring= s[start:end]
    return substring
#enddef

def indicesOfNamesWithEquals(x):
    iList=[]
    for i in range(len(x)):
        item=x.__getitem__(i)
        if ("=" in item): iList.append(i)
    #endfor
    return iList
#enddef