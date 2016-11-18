'''
Created on Nov 10, 2016. (C) 1QBit
@author: Andrew Milne
'''
import numpy as np # calms the PyDev error checker, which can't handle dependencies amongst modules
print "Initializing reference data for AU and DE data sets."

###### AUSTRALIAN (AU) DATA
if(True):   # define huangAlpha in a foldable way
    huangAlpha   =  np.zeros(22) # set it up
    huangAlpha[0]=  np.inf
    huangAlpha[1]=  0.0
    huangAlpha[2]=  0.060546875
    huangAlpha[3]=  0.3046875
    huangAlpha[4]=  0.400390625
    huangAlpha[5]=  0.419921875
    huangAlpha[6]=  0.5078125
    huangAlpha[7]=  0.59765625
    huangAlpha[8]=  0.703125
    huangAlpha[9]=  0.71875
    huangAlpha[10]= 0.75
    huangAlpha[11]= 0.779296875
    huangAlpha[12]= 0.802734375
    huangAlpha[13]= 0.826171875
    huangAlpha[14]= 0.830078125
    huangAlpha[15]= 0.837890625
    huangAlpha[16]= 0.86328125
    huangAlpha[17]= 0.880859375
    huangAlpha[18]= 0.8984375
    huangAlpha[19]= 0.90234375
    huangAlpha[20]= 0.955078125
    huangAlpha[21]= 1.0
#endif

if(True):   # define huangFeatureListList in a foldable way
    huangFeatureListList= [ 
        [],
        ['A8'],
        ['A1', 'A8'],
        ['A8', 'A14'],
        ['A1', 'A8', 'A14'],
        ['A4', 'A8', 'A12'],
        ['A1', 'A5', 'A8', 'A14'],
        ['A1', 'A5', 'A8', 'A10', 'A14'],
        ['A4', 'A5', 'A8', 'A10', 'A14'],
        ['A5', 'A7', 'A8', 'A10', 'A14'],
        ['A4', 'A5', 'A7', 'A8', 'A9', 'A14'],
        ['A4', 'A5', 'A7', 'A8', 'A9', 'A13', 'A14'],
        ['A4', 'A5', 'A7', 'A8', 'A9', 'A10', 'A14'],
        ['A4', 'A5', 'A7', 'A8', 'A9', 'A10', 'A13', 'A14'],
        ['A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A14'],
        ['A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A12', 'A14'],
        ['A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A12', 'A13', 'A14'],
        ['A2', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A12', 'A13', 'A14'],
        ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A12', 'A14'],
        ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A12', 'A13', 'A14'],
        ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14'],
        ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',  'A10', 'A11', 'A12', 'A13', 'A14']  ] 
#endif
    
if(True):   # define huangOCAR in a foldable way
    huangOCAR=0.0001*np.array([  
       0,
    5551,
    8551,
    8580,
    8565,
    8580,
    8594,
    8696,
    8754,
    8725,
    8652,
    8768,
    8652,
    8797,
    8681,
    8681,
    8739,
    8725,
    8696,
    8739,
    8739,
    8710   ])
#endif

if(True):  # define huangSubs and huangAlpha in a foldable way
    # shape=(22,14)sets up a matrix with rows 0 to 21, and 15 columns numbered 0 to 14
    # we will ignore element 0 in order to use Huang's 1-origin indexing.
    huangSubs  = np.zeros(shape=(22,15))
    huangAlpha = np.zeros(22)
    # 0 elements - present in the matrix but will not be plotted, so nothing here
    hRow=0
    huangAlpha[hRow]=np.inf
    
    # 1 element
    hRow=1
    huangAlpha[hRow]=0.0
    huangSubs[hRow,8]=1
    
    # 2 elements
    hRow=2
    huangAlpha[hRow]=0.060546875
    huangSubs[hRow,1]=1; huangSubs[hRow,8]=1; 
    
    hRow=3
    huangAlpha[hRow]=0.3046875
    huangSubs[hRow,8]=1; huangSubs[hRow,14]=1
    
    # 3 elements
    hRow=4
    huangAlpha[hRow]=0.400390625
    huangSubs[hRow,1]=1; huangSubs[hRow,8]=1; huangSubs[hRow,14]=1
    
    
    hRow=5
    huangAlpha[hRow]=0.419921875
    huangSubs[hRow,4]=1; huangSubs[hRow,8]=1; huangSubs[hRow,12]=1
    
    # 4 elements
    hRow=6
    huangAlpha[hRow]= 0.5078125
    huangSubs[hRow,1]=1; huangSubs[hRow,5]=1; huangSubs[hRow,8]=1; huangSubs[hRow,14]=1
    
    # 5 elements
    hRow=7
    huangAlpha[hRow]= 0.59765625
    huangSubs[7,1]=1; huangSubs[7,5]=1; huangSubs[7,8]=1; huangSubs[7,10]=1; huangSubs[7,14]=1
    
    hRow=8
    huangAlpha[hRow]= 0.703125
    huangSubs[8,4]=1; huangSubs[8,5]=1; huangSubs[8,8]=1; huangSubs[8,10]=1; huangSubs[8,14]=1
    
    hRow=9
    huangAlpha[hRow]= 0.71875
    huangSubs[9,5]=1; huangSubs[9,7]=1; huangSubs[9,8]=1; huangSubs[9,10]=1; huangSubs[9,14]=1
    
    # 6 elements
    hRow=10
    huangAlpha[hRow]= 0.75
    huangSubs[hRow,4]=1; huangSubs[hRow,5]=1; huangSubs[hRow,7]=1; huangSubs[hRow,8]=1; 
    huangSubs[hRow,9]=1; huangSubs[hRow,14]=1
    
    # 7 elements
    hRow=11
    huangAlpha[hRow]= 0.779296875
    huangSubs[11,4]=1;  huangSubs[11,5]=1;  huangSubs[11,7]=1; huangSubs[11,8]=1; 
    huangSubs[11,9]=1;  huangSubs[11,13]=1; huangSubs[11,14]=1
    
    hRow=12
    huangAlpha[hRow]= 0.802734375
    huangSubs[12,4]=1;  huangSubs[12,5]=1; huangSubs[12,7]=1; huangSubs[12,8]=1; 
    huangSubs[12,9]=1;  huangSubs[12,10]=1; huangSubs[12,14]=1
    
    # 8 elements
    hRow=13
    huangAlpha[hRow]= 0.826171875
    huangSubs[13,4]=1;  huangSubs[13,5]=1;  huangSubs[13,7]=1;  huangSubs[13,8]=1; 
    huangSubs[13,9]=1;  huangSubs[13,10]=1; huangSubs[13,13]=1; huangSubs[13,14]=1
    
    hRow=14
    huangAlpha[hRow]= 0.830078125
    huangSubs[14,4]=1;  huangSubs[14,5]=1;  huangSubs[14,6]=1; huangSubs[14,7]=1;
    huangSubs[14,8]=1;  huangSubs[14,9]=1; huangSubs[14,10]=1; huangSubs[14,14]=1
    
    # 9 elements
    hRow=15
    huangAlpha[hRow]= 0.837890625
    huangSubs[15,4]=1;  huangSubs[15,5]=1;  huangSubs[15,6]=1; huangSubs[15,7]=1;
    huangSubs[15,8]=1;  huangSubs[15,9]=1; huangSubs[15,10]=1; huangSubs[15,12]=1
    huangSubs[15,14]=1; 
    
    # 10 elements
    hRow=16
    huangAlpha[hRow]= 0.86328125
    huangSubs[hRow,4]=1;  huangSubs[hRow,5]=1;  huangSubs[hRow,6]=1; huangSubs[hRow,7]=1;
    huangSubs[hRow,8]=1;  huangSubs[hRow,9]=1; huangSubs[hRow,10]=1; huangSubs[hRow,12]=1
    huangSubs[hRow,13]=1; huangSubs[hRow,14]=1; 
    
    # 11 elements
    hRow=17
    huangAlpha[hRow]= 0.880859375
    huangSubs[hRow,2]=1;  huangSubs[hRow,4]=1;  huangSubs[hRow,5]=1; huangSubs[hRow,6]=1;
    huangSubs[hRow,7]=1;  huangSubs[hRow,8]=1;  huangSubs[hRow,9]=1; huangSubs[hRow,10]=1
    huangSubs[hRow,12]=1; huangSubs[hRow,13]=1; huangSubs[hRow,14]=1
    
    hRow=18
    huangAlpha[hRow]= 0.8984375
    huangSubs[hRow,2]=1;  huangSubs[hRow,3]=1;  huangSubs[hRow,4]=1; huangSubs[hRow,5]=1;
    huangSubs[hRow,6]=1;  huangSubs[hRow,7]=1;  huangSubs[hRow,8]=1; huangSubs[hRow,9]=1
    huangSubs[hRow,10]=1; huangSubs[hRow,12]=1; huangSubs[hRow,14]=1
    
    # 12 elements
    hRow=19
    huangAlpha[hRow]= 0.90234375
    huangSubs[hRow,2]=1;  huangSubs[hRow,3]=1;  huangSubs[hRow,4]=1;  huangSubs[hRow,5]=1;
    huangSubs[hRow,6]=1;  huangSubs[hRow,7]=1;  huangSubs[hRow,8]=1;  huangSubs[hRow,9]=1
    huangSubs[hRow,10]=1; huangSubs[hRow,12]=1; huangSubs[hRow,13]=1; huangSubs[hRow,14]=1
    
    # 13 elements
    hRow=20
    huangAlpha[hRow]= 0.955078125
    huangSubs[hRow,2]=1;  huangSubs[hRow,3]=1;  huangSubs[hRow,4]=1;  huangSubs[hRow,5]=1;
    huangSubs[hRow,6]=1;  huangSubs[hRow,7]=1;  huangSubs[hRow,8]=1;  huangSubs[hRow,9]=1;
    huangSubs[hRow,10]=1; huangSubs[hRow,11]=1; huangSubs[hRow,12]=1; huangSubs[hRow,13]=1;
    huangSubs[hRow,14]=1; 
    
    # 14 elements
    hRow=21
    huangAlpha[hRow]= 1.0
    huangSubs[hRow,1]=1;  huangSubs[hRow,2]=1;  huangSubs[hRow,3]=1;  huangSubs[hRow,4]=1;
    huangSubs[hRow,5]=1;  huangSubs[hRow,6]=1;  huangSubs[hRow,7]=1;  huangSubs[hRow,8]=1;
    huangSubs[hRow,9]=1;  huangSubs[hRow,10]=1; huangSubs[hRow,11]=1; huangSubs[hRow,12]=1;
    huangSubs[hRow,13]=1; huangSubs[hRow,14]=1; 
#endif

###### GERMAN (DE) DATA
if(True):   #  define hdeAlpha 
    hdeAlpha= [
    0.0,
    0.120239258,
    0.422912598,
    0.422973633,
    0.531921387, 
    0.601623535,
    0.620391846,
    0.658599854,
    0.684204102,
    0.694030762,
    0.711578369,
    0.723571777,
    0.753265381,
    0.839416504,
    0.861663818,
    0.875,
    0.876800537,
    0.886505127,
    0.894195557,
    0.9112854,
    0.930633545,
    0.946868896,
    0.960479736,
    0.976745605,
    0.985107422,
    0.985168457,
    0.991271973,
    0.994476318,
    0.997283936,
    0.99822998,
    1
    ]
#endif

if(True):   # define hdeIndexLists
    hdeIndexLists=[
        [
            1
        ],
        [
            5, 11, 21
        ],
        [
            1, 2, 7
        ],
        [
            5, 11, 16, 21
        ],
        [
            1, 2, 7, 10 
        ],
        [
            1, 2, 3, 7
        ],
        [
            1, 2, 3, 7, 19
        ],
        [
            1, 2, 3, 5, 7
        ],
        [
            1, 3, 5, 7, 9, 16
        ],
        [
            1, 3, 5, 7, 9, 16, 19
        ],
        [
            1, 2, 3, 5, 7, 11, 19
        ],
        [
            1, 2, 3, 5, 7, 11, 16, 19
        ],
        [
            1, 2, 3, 5, 7, 11, 16, 19, 21
        ],
        [
            1, 2, 3, 5, 7, 10, 11, 16, 19, 21
        ],
        [
            1, 2, 3, 5, 7, 10, 11, 15, 16, 19, 21
        ],
        [
            1, 2, 3, 5, 7, 9, 10, 11, 16, 19, 21
        ],
        [
            1, 2, 3, 5, 6, 7, 9, 11, 16, 19, 21
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 11, 15, 16, 19, 21
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 10, 11, 15, 16, 19, 21
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 15, 16, 19, 21
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 15, 16, 17, 19, 21
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 15, 16, 17, 19, 20, 21
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 15, 16, 17, 19, 20, 21
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 24        
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 23
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 23, 24
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
        ]
    ]
#endif

if(True):   # define hdeOcar
    hdeOcar=0.001*np.array(
        [
        700,
        706,
        735,
        719,
        734,
        754,
        754,
        758,
        751,
        745,
        758,
        765,
        774,
        768,
        768,
        771,
        771,
        775,
        773,
        772,
        772,
        773,
        776,
        774,
        775,
        773,
        775,
        775,
        776,
        772,
        783
        ]    )
#endif