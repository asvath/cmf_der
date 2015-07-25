import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.interpolate
from itertools import cycle

def filter_value(a,b,value):
	someList=zip(a,b)
	for x, y in someList:
	        if x == value :
	            return x,y



def histoplot(nameofplot): 

	"""
	Example:

	$ipython hmrplot list nameofplot

	"""
	c=cm.rainbow(np.linspace(0,1,3))
	acyc=cycle(c)
	ray=[]

	onezero,oneone,oneonefive,onetwo,onetwofive,onethree,onethreefive,onefour,onefourfive,onefive,onefivefive = np.loadtxt("%s_one_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))
	twozero,twoone,twoonefive,twotwo,twotwofive,twothree,twothreefive,twofour,twofourfive,twofive,twofivefive = np.loadtxt("%s_two_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))
	threezero,threeone,threeonefive,threetwo,threetwofive,threethree,threethreefive,threefour,threefourfive,threefive,threefivefive = np.loadtxt("%s_three_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))

	y=[10,20,30,40,50,60,70,80,90]
	#particle 1
	lmax=np.log10(onezero[-1])
	lmin=np.log10(onezero[0])
	xsone=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(onezero,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsone)
	ysone=w**2
	splinedfit=splinefit.derivative()

	ysoneder=splinedfit(xsone)*2*w
	ysoneder=ysoneder/(4*np.pi*xsone**2)

	dy=splinedfit(onezero)*2*np.sqrt(y)
	dy=dy/(4*np.pi*onezero**2)
	
	#particle 2

	lmax=np.log10(twozero[-1])
	lmin=np.log10(twozero[0])
	xstwo=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(twozero,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xstwo)
	ystwo=w**2
	splinedfit=splinefit.derivative()

	ystwoder=splinedfit(xstwo)*2*w
	ystwoder=ystwoder/(4*np.pi*xstwo**2)

	dy2=splinedfit(twozero)*2*np.sqrt(y)
	dy2=dy2/(4*np.pi*twozero**2)



	#particle 3

	lmax=np.log10(threezero[-1])
	lmin=np.log10(threezero[0])
	xsthree=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(threezero,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsthree)
	ysthree=w**2
	splinedfit=splinefit.derivative()

	ysthreeder=splinedfit(xsthree)*2*w
	ysthreeder=ysthreeder/(4*np.pi*xsthree**2)

	dy3=splinedfit(threezero)*2*np.sqrt(y)
	dy3=dy3/(4*np.pi*threezero**2)


	#plotsy


	plt.plot(xsone,ysone,label="first 1%")
	plt.scatter(onezero,y,color="darkorange")
	
	plt.plot(xstwo,ystwo,label="next 1%")
	plt.scatter(twozero,y,color="lime")

	plt.plot(xsthree,ysthree,label="same mass as first 1%")
	plt.scatter(threezero,y,color="blue")

	plt.title('%s_time0000'%nameofplot)
	plt.ylabel('number of particles')
	plt.xlabel('r')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_0000.pdf" %nameofplot)
	plt.close()


	plt.plot(np.log10(xsone),np.log10(ysoneder),label="first 1%")
	plt.scatter(np.log10(onezero[:-1]),np.log10(dy[:-1]),color="darkorange")

	plt.plot(np.log10(xstwo),np.log10(ystwoder),label="next 1%")
	plt.scatter(np.log10(twozero[:-1]),np.log10(dy2[:-1]),color="lime")

	
	plt.plot(np.log10(xsthree),np.log10(ysthreeder),label="same mass as 1%")
	plt.scatter(np.log10(threezero[:-1]),np.log10(dy3[:-1]),color="blue")

	plt.title('%s_derivative_time_0000'%nameofplot)
	plt.ylabel('log (Density)')
	plt.xlabel('log (r)')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_der0000.pdf" %nameofplot)
	plt.close()
	

	#time 100
	#particle 1
	lmax=np.log10(oneone[-1])
	lmin=np.log10(oneone[0])
	xsone=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(oneone,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsone)
	ysone=w**2
	splinedfit=splinefit.derivative()

	ysoneder=splinedfit(xsone)*2*w
	ysoneder=ysoneder/(4*np.pi*xsone**2)

	dy=splinedfit(oneone)*2*np.sqrt(y)
	dy=dy/(4*np.pi*oneone**2)
	
	#particle 2

	lmax=np.log10(twoone[-1])
	lmin=np.log10(twoone[0])
	xstwo=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(twoone,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xstwo)
	ystwo=w**2
	splinedfit=splinefit.derivative()

	ystwoder=splinedfit(xstwo)*2*w
	ystwoder=ystwoder/(4*np.pi*xstwo**2)

	dy2=splinedfit(twoone)*2*np.sqrt(y)
	dy2=dy2/(4*np.pi*twoone**2)



	#particle 3

	lmax=np.log10(threeone[-1])
	lmin=np.log10(threeone[0])
	xsthree=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(threeone,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsthree)
	ysthree=w**2
	splinedfit=splinefit.derivative()

	ysthreeder=splinedfit(xsthree)*2*w
	ysthreeder=ysthreeder/(4*np.pi*xsthree**2)

	dy3=splinedfit(threeone)*2*np.sqrt(y)
	dy3=dy3/(4*np.pi*threeone**2)


	#plotsy


	plt.plot(xsone,ysone,label="first 1%")
	plt.scatter(oneone,y,color="darkorange")
	
	plt.plot(xstwo,ystwo,label="next 1%")
	plt.scatter(twoone,y,color="lime")

	plt.plot(xsthree,ysthree,label="same mass as first 1%")
	plt.scatter(threeone,y,color="blue")

	plt.title('%s_time0100'%nameofplot)
	plt.ylabel('number of particles')
	plt.xlabel('r')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_0100.pdf" %nameofplot)
	plt.close()


	plt.plot(np.log10(xsone),np.log10(ysoneder),label="first 1%")
	plt.scatter(np.log10(oneone[:-1]),np.log10(dy[:-1]),color="darkorange")

	plt.plot(np.log10(xstwo),np.log10(ystwoder),label="next 1%")
	plt.scatter(np.log10(twoone[:-1]),np.log10(dy2[:-1]),color="lime")

	
	plt.plot(np.log10(xsthree),np.log10(ysthreeder),label="same mass as 1%")
	plt.scatter(np.log10(threeone[:-1]),np.log10(dy3[:-1]),color="blue")

	plt.title('%s_derivative_time_0100'%nameofplot)
	plt.ylabel('log (Density)')
	plt.xlabel('log (r)')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_der0100.pdf" %nameofplot)
	plt.close()
		
	#time150



	#particle 1
	lmax=np.log10(oneonefive[-1])
	lmin=np.log10(oneonefive[0])
	xsone=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(oneonefive,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsone)
	ysone=w**2
	splinedfit=splinefit.derivative()

	ysoneder=splinedfit(xsone)*2*w
	ysoneder=ysoneder/(4*np.pi*xsone**2)

	dy=splinedfit(oneonefive)*2*np.sqrt(y)
	dy=dy/(4*np.pi*oneonefive**2)
	
	#particle 2

	lmax=np.log10(twoonefive[-1])
	lmin=np.log10(twoonefive[0])
	xstwo=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(twoonefive,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xstwo)
	ystwo=w**2
	splinedfit=splinefit.derivative()

	ystwoder=splinedfit(xstwo)*2*w
	ystwoder=ystwoder/(4*np.pi*xstwo**2)

	dy2=splinedfit(twoonefive)*2*np.sqrt(y)
	dy2=dy2/(4*np.pi*twoonefive**2)



	#particle 3

	lmax=np.log10(threeonefive[-1])
	lmin=np.log10(threeonefive[0])
	xsthree=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(threeonefive,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsthree)
	ysthree=w**2
	splinedfit=splinefit.derivative()

	ysthreeder=splinedfit(xsthree)*2*w
	ysthreeder=ysthreeder/(4*np.pi*xsthree**2)

	dy3=splinedfit(threeonefive)*2*np.sqrt(y)
	dy3=dy3/(4*np.pi*threeonefive**2)


	#plotsy


	plt.plot(xsone,ysone,label="first 1%")
	plt.scatter(oneonefive,y,color="darkorange")
	
	plt.plot(xstwo,ystwo,label="next 1%")
	plt.scatter(twoonefive,y,color="lime")

	plt.plot(xsthree,ysthree,label="same mass as first 1%")
	plt.scatter(threeonefive,y,color="blue")

	plt.title('%s_time0150'%nameofplot)
	plt.ylabel('number of particles')
	plt.xlabel('r')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_0150.pdf" %nameofplot)
	plt.close()


	plt.plot(np.log10(xsone),np.log10(ysoneder),label="first 1%")
	plt.scatter(np.log10(oneonefive[:-1]),np.log10(dy[:-1]),color="darkorange")

	plt.plot(np.log10(xstwo),np.log10(ystwoder),label="next 1%")
	plt.scatter(np.log10(twoonefive[:-1]),np.log10(dy2[:-1]),color="lime")

	
	plt.plot(np.log10(xsthree),np.log10(ysthreeder),label="same mass as 1%")
	plt.scatter(np.log10(threeonefive[:-1]),np.log10(dy3[:-1]),color="blue")

	plt.title('%s_derivative_time_0150'%nameofplot)
	plt.ylabel('log (Density)')
	plt.xlabel('log (r)')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_der0150.pdf" %nameofplot)
	plt.close()

	#time200

	
	#particle 1
	lmax=np.log10(onetwo[-1])
	lmin=np.log10(onetwo[0])
	xsone=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(onetwo,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsone)
	ysone=w**2
	splinedfit=splinefit.derivative()

	ysoneder=splinedfit(xsone)*2*w
	ysoneder=ysoneder/(4*np.pi*xsone**2)

	dy=splinedfit(onetwo)*2*np.sqrt(y)
	dy=dy/(4*np.pi*onetwo**2)
	
	#particle 2

	lmax=np.log10(twotwo[-1])
	lmin=np.log10(twotwo[0])
	xstwo=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(twotwo,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xstwo)
	ystwo=w**2
	splinedfit=splinefit.derivative()

	ystwoder=splinedfit(xstwo)*2*w
	ystwoder=ystwoder/(4*np.pi*xstwo**2)

	dy2=splinedfit(twotwo)*2*np.sqrt(y)
	dy2=dy2/(4*np.pi*twotwo**2)



	#particle 3

	lmax=np.log10(threetwo[-1])
	lmin=np.log10(threetwo[0])
	xsthree=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(threetwo,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsthree)
	ysthree=w**2
	splinedfit=splinefit.derivative()

	ysthreeder=splinedfit(xsthree)*2*w
	ysthreeder=ysthreeder/(4*np.pi*xsthree**2)

	dy3=splinedfit(threetwo)*2*np.sqrt(y)
	dy3=dy3/(4*np.pi*threetwo**2)


	#plotsy


	plt.plot(xsone,ysone,label="first 1%")
	plt.scatter(onetwo,y,color="darkorange")
	
	plt.plot(xstwo,ystwo,label="next 1%")
	plt.scatter(twotwo,y,color="lime")

	plt.plot(xsthree,ysthree,label="same mass as first 1%")
	plt.scatter(threetwo,y,color="blue")

	plt.title('%s_time0200'%nameofplot)
	plt.ylabel('number of particles')
	plt.xlabel('r')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_0200.pdf" %nameofplot)
	plt.close()


	plt.plot(np.log10(xsone),np.log10(ysoneder),label="first 1%")
	plt.scatter(np.log10(onetwo[:-1]),np.log10(dy[:-1]),color="darkorange")

	plt.plot(np.log10(xstwo),np.log10(ystwoder),label="next 1%")
	plt.scatter(np.log10(twotwo[:-1]),np.log10(dy2[:-1]),color="lime")

	
	plt.plot(np.log10(xsthree),np.log10(ysthreeder),label="same mass as 1%")
	plt.scatter(np.log10(threetwo[:-1]),np.log10(dy3[:-1]),color="blue")

	plt.title('%s_derivative_time_0200'%nameofplot)
	plt.ylabel('log (Density)')
	plt.xlabel('log (r)')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_der0150.pdf" %nameofplot)
	plt.close()

	#two be continued

if __name__ == "__main__":
	import sys
	histoplot(str(sys.argv[1]))

