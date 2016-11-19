'''
Created on Nov 15, 2016  (c) 1QBit
@author: Andrew Milne
'''
import numpy    as np                       # @UnusedImport (annotation for Eclipse/PyDev)
import qdk
import matplotlib         as mpl            # @UnusedImport
import matplotlib.pyplot  as plt            # @UnusedImport
import matplotlib.path    as mpath          # @UnusedImport
import matplotlib.lines   as mlines
import matplotlib.patches as mpatches
from   matplotlib.collections import PatchCollection


print "Loads: "+"makeE31Q, makeOtherHuangMatrix, polyFromMatrix, aPlot (for the Au data)"
## Construct a Q matrix that will implement Huang's equation 3.1 (as opposed to the written out version)
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


## Construct a different Q matrix - THIS VARIES AS WE NEED IT

def makeOtherHuangMatrix(rhoMatrix, yVector, alphaParameter):
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
                trueQm[i,j]=4*alphaParameter*abs(yVector[i])
            else:
                trueQm[i,j]=-(1-alphaParameter)*(abs(rhoMatrix[j,i]))
            #endif
        #endfor
    #endfor
    return trueQm
#enddef

def polyFromMatrix(blockMatrix):
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

def aPlot(huangAlpha,huangSubs,milneSubs):
    plt.gcf().clear()
    fig, ax = plt.subplots()  #@UnusedVariable - fig is returned, but not needed 
    ax.set_autoscale_on(False)
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])

    # Matrix row is vertical downwards, column is horizontal rightwards.  
    # Canvas X is horizontal rightwards, Y is vertical upwards.
    # We set the number of rows and columns. 
    (nrows,ncols)=huangSubs.shape
    # nrows=22;ncols=15 # used to fix values for debugging
    xstep=1.0/(float(ncols))
    ystep=1.0/(float(nrows))
    xbase=1.5*xstep
    ybase=1.5*ystep

    fbwidth=  0.6*xstep
    fbheight= 0.6*ystep

    xBoxMidpointToCornerOffset=0.5*fbwidth
    yBoxMidpointToCornerOffset=0.5*fbheight

    fbPad=0.005

    # Puts a soft grey line around the fancy box area for ease of development.
    # The wider line at the bottom deals with a clipping surprise in Jupyter.
    visibleForContext=False
    line1 = mlines.Line2D([0.0,1.0],[0.0,0.0], lw=2.5,visible=visibleForContext, color="k",alpha=0.3)
    line2 = mlines.Line2D([1.0,1.0],[0.0,1.0], lw=1., visible=visibleForContext, color="k",alpha=0.3)
    line3 = mlines.Line2D([1.0,0.0],[1.0,1.0], lw=1., visible=visibleForContext, color="k",alpha=0.3)
    line4 = mlines.Line2D([0.0,0.0],[1.0,0.0], lw=1., visible=visibleForContext, color="k",alpha=0.3)
    ax.add_line(line1)
    ax.add_line(line2)
    ax.add_line(line3)
    ax.add_line(line4)

    plt.axis('equal')
    plt.axis('off')

    # top of column labels
    for jCol in np.arange(1,ncols):
        xfb= xbase+(jCol-1)*xstep          
        yfb= 1 - ybase/2.0  
        collable=str("A")+str(jCol)
        plt.text(xfb, yfb, collable, ha="center", family='sans-serif', size=12)
    #endfor    

    # The alpha label has to be plotted with a Latex representation
    # and argument style peculiar to matplotlib
    plt.text(0.01,0.956, r'$\alpha$', ha="left", size=24)

    # row labels - maybe force precision on alpha
    for iRow in np.arange(1,nrows):
        xfb= 0.01          
        yfb= (1 - (1.1*ybase+(iRow-1)*ystep) )  
        rollable=str(huangAlpha[iRow])[:4]
        plt.text(xfb, yfb, rollable, ha="left", family='sans-serif', size=12)
    #endfor  

    patches = []
    # we are just going to use the indices starting at 1 and pretend
    # that the zeroth element just isn't there.
    # plot x is horizontal and corresponds to the column (j) number
    # the y coord is counted down from the top at y=1
    # We are indexing from 1, although for different reasons on each axis.
    # The first plotted fancy box is plotted at (xbase, ybase) less the offsets
    # to the lower left corner, where matplotlib puts the box origin.
    for iRow in np.arange(1,nrows):
        for jCol in np.arange(1,ncols):
            xfb= xbase+(jCol-1)*xstep          - xBoxMidpointToCornerOffset
            yfb= (1 - (ybase+(iRow-1)*ystep) ) - yBoxMidpointToCornerOffset
            if(0<huangSubs[iRow,jCol]):   
                # colored box
                (kRed, kGreen, kBlue)=(0.7,0.0,0.0)
                kBlue=sum(huangSubs[iRow,:])/float(ncols)
                cRGB=(kRed, kGreen, kBlue)
                fb = mpatches.FancyBboxPatch(
                    [xfb,yfb], fbwidth, fbheight,
                    boxstyle=mpatches.BoxStyle("Round", pad=fbPad),
                    facecolor=cRGB, edgecolor="k", visible=True  )
                patches.append(fb)
            else:
                # empty box
                fb = mpatches.FancyBboxPatch(
                    [xfb,yfb], fbwidth, fbheight,
                    boxstyle=mpatches.BoxStyle("Round", pad=fbPad),
                    facecolor="w", edgecolor="k", visible=True  )
                patches.append(fb)
            #endif
            if(0<milneSubs[iRow,jCol]):   
                # colored box
                fb = mpatches.FancyBboxPatch(
                    [xfb,yfb],  fbwidth, fbheight,
                    boxstyle=mpatches.BoxStyle("Round", pad=fbPad),
                    facecolor="g", edgecolor="k", visible=True
                    )
                patches.append(fb)
            else:
                pass # empty box, if needed, will already be done by here
            #endif
        #endfor j
    #endfor i

    collection = PatchCollection(patches, match_original=True, alpha=0.3) 
    ax.add_collection(collection)

    # The subplots_adjust function can be used to provide scale. The keyword parameters 
    # are positions, e.g. the top must be greater than the bottom.
    # IF YOU CHANGE THIS YOU ALSO HAVE TO CHANGE THE FONT SIZE
    plt.subplots_adjust(left=0, right=2.0, bottom=0, top=2.0)

    plt.show()
#enddef

