import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

def prehistoric(name,labelsy,coloursy):

	y=[10,20,30,40,50,60,70,80,90]
	lmax=np.log10(name[-1])
	lmin=np.log10(name[0])
	xsone=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(name,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsone)
	ysone=w**2
	splinedfit=splinefit.derivative()

	ysoneder=splinedfit(xsone)*2*w
	ysoneder=ysoneder/(4*np.pi*xsone**2)

	dy=splinedfit(name)*2*np.sqrt(y)
	dy=dy/(4*np.pi*name**2)

	plt.plot(np.log10(xsone),np.log10(ysoneder),label=labelsy,color=coloursy)
	plt.scatter(np.log10(name[:-1]),np.log10(dy[:-1]),color=coloursy)


if __name__ == "__main__":
	import sys
	prehistoric(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))

