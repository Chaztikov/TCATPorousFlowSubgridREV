
make_plots=0

import os,sys,re,subprocess
import pandas as pd
import numpy as np
import scipy
from scipy.spatial import KDTree
from scipy.interpolate import BSpline
from scipy.interpolate import splrep, splder, sproot,make_interp_spline
#import mayavi
#from mayavi import mlab

#import quadpy, orthopy, pygmsh
#from helpers import compute_volume
#import sympy
#from sympy im
#from sympy.abc import a,b,c

use_weighted_average = 0

cwd = "/home/chaztikov/Documents/data/pack0/timelog/TCATtimelog/"

def getfname(n,x,y,z,getsubcell=1):
    if(getsubcell==1):
        out = "timelog.tcat."
        out+=str(n).zfill(5)
        out+="."
        out+=str(x).zfill(2)
        out+="-"
        out+=str(y).zfill(2)
        out+="-"
        out+=str(z).zfill(2)    
        return cwd+out
    else:
        out = "timelog.tcat."
        out+=str(n).zfill(5)  
        return cwd+out
#.00007.01-02-01
tol = 1e-4
err = 1
nn=7


gdata = pd.read_csv(cwd+"../pack.out"," ")
zeroplusminus=[0,-1,1]
'''get vol. frac. solid'''
datas=[]
solidvols=[]
totals = []
errors = []
count=0

for i in [1,2]:
    for j in [1,2]:
        for k in [1,2]:
            
            idx = np.where( np.sign(gdata[['x']]-0.5) == zeroplusminus[i] )[0]
            idy = np.where( np.sign(gdata[['y']]-0.5) == zeroplusminus[j] )[0]
            idz = np.where( np.sign(gdata[['z']]-0.5) == zeroplusminus[k] )[0]
            ids = np.intersect1d(idx,np.intersect1d(idy,idz))
            rr = gdata[['r']].values[ids].copy()
            vols = rr**3 * np.pi * 4/3
            '''volume solid'''
            vfs = vols.sum()
            solidvols.append(vfs)
            
            count+=1;
            fname = getfname(nn,i,j,k)
            data=pd.read_csv(fname, ' ')
            datas.append(data[['sw','pw']].values)

fname = getfname(nn,i,j,k,getsubcell=0)
data0=pd.read_csv(fname, ' ')        
datas.append(data0[['sw','pw']].values)
#np.savetxt("")

gdata = pd.read_csv(cwd+"../pack.out" , " ", skiprows=0)
meancoords = ( gdata[['x','y','z']].max() - gdata[['x','y','z']].min() )  / 2
meancoords = [0.5,0.5,0.5]


for i in [1,2]:
    for j in [1,2]:
        for k in [1,2]:
            idx = np.where( np.sign(gdata[['x']]-0.5) == zeroplusminus[i] )[0]
            idy = np.where( np.sign(gdata[['y']]-0.5) == zeroplusminus[j] )[0]
            idz = np.where( np.sign(gdata[['z']]-0.5) == zeroplusminus[k] )[0]
            ids = np.intersect1d(idx,np.intersect1d(idy,idz))
            rr = gdata[['r']].values[ids].copy()
            vols = rr**3 * np.pi * 4/3
            '''volume solid'''
            vfs = vols.sum()


solidvols=[]
totals = []
errors = []
#f=open("errors.csv","w+")
header = "".join(['time,', 'sw,', 'pw,', 'pn,', 'awn,', 'ans,', 'aws,', 'Jwn,', 'Kwn,', 'lwns,',
       'cwns,', 'KNwns,', 'KGwns,', 'vawx,', 'vawy,', 'vawz,', 'vanx,', 'vany,',
       'vanz,', 'vawnx,', 'vawny,', 'vawnz,', 'vawnsx,', 'vawnsy,', 'vawnsz,',
       'Gwnxx,', 'Gwnyy,', 'Gwnzz,', 'Gwnxy,', 'Gwnxz,', 'Gwnyz,', 'Gwsxx,', 'Gwsyy,',
       'Gwszz,', 'Gwsxy,', 'Gwsxz,', 'Gwsyz,', 'Gnsxx,', 'Gnsyy,', 'Gnszz,', 'Gnsxy,',
       'Gnsxz,', 'Gnsyz,', 'trawn,', 'trJwn,', 'trRwn,', 'wwndnw,', 'wwnsdnwn,',
       'Jwnwwndnw,', 'Euler,', 'Kn,', 'Jn,', 'An'])
#f.write(header)
#f.write("\n")
swvfs_total = 0
for nn in range(nn):
    total = 0;
    count=0;
    for i in [1,2]:
        for j in [1,2]:
            for k in [1,2]:
                print("Octant "+str([i,j,k]) + "\n\n")
                idx = np.where( np.sign(gdata[['x']]-0.5) == zeroplusminus[i] )[0]
                idy = np.where( np.sign(gdata[['y']]-0.5) == zeroplusminus[j] )[0]
                idz = np.where( np.sign(gdata[['z']]-0.5) == zeroplusminus[k] )[0]
                ids = np.intersect1d(idx,np.intersect1d(idy,idz))
                rr = gdata[['r']].values[ids].copy()
                vols = rr**3 * np.pi * 4/3
                '''volume solid'''
                vfs = vols.sum()
                solidvols.append(vfs)
                
                count+=1;
                fname = getfname(nn,i,j,k)
                
                data=pd.read_csv(fname, ' ')
                
                data['time'] = data['pw']*data['sw']*vfs
                swvfs_total += data['sw']*vfs
                
                itertotal = data.sum(axis=0)
                
                if(use_weighted_average==1):
                    itertotal *= vfs
                
                totals.append( itertotal )
                total += itertotal
                


    solidvoltotal = np.sum(solidvols)
    total0 = pd.read_csv(getfname(nn,i,j,k,0), ' ').sum()

    total0['time'] = total0['pw']*total0['sw']*solidvoltotal #/(total0['sw']*solidvoltotal)
#    total /= swvfs_total
    
    if(use_weighted_average==1):
        total0 *= solidvoltotal;
    error = total - total0
    error = np.abs(error)
    
    inz = np.where( np.abs(error) > tol)[0]
    print("\n\n",error[inz] / total0[inz],
          len(inz))
    errvals = np.abs( error.values )
    errors.append(errvals)

if(use_weighted_average):
    np.savetxt("errors_porosweighted.csv",errors,header=header)
else:
    np.savetxt("errors.csv",errors,header=header,delimiter=', ')

