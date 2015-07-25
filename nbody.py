
import numpy as np

########################################################


def readviewdat(filename):
	with open(filename,"r") as f:
		snap={}
		dt = np.dtype([('x',np.float32),('y',np.float32),('z',np.float32),('m',np.float32)])
		a = np.fromfile(filename, dtype = dt)
		l=len(a['x'])/2
		k=l+1000
		mass=np.sum(a['m'][:l])
		snap['x']=a['x'][:l]
		snap['y']=a['y'][:l]
		snap['z']=a['z'][:l]
		snap['m']=a['m'][:l]
		snap['vx']=a['x'][l:]
		snap['vy']=a['y'][l:]
		snap['vz']=a['z'][l:]
		return snap

import sys

def main():
    print(readviewdat(sys.argv[1]))

#------------------------------------------------------------------------------
# Start program execution.
#
if __name__ == '__main__':
    main()
