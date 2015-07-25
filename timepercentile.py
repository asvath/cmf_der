import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from itertools import cycle

def percentileplot(filename,nameofplot): 

	"""
	Example:

	$ipython hmrplot list nameofplot

	"""
	c=cm.rainbow(np.linspace(0,1,6))
	acyc=cycle(c)
	
	time, oneone,onetwo,onethree,onefour,onefive,onesix,oneseven,oneeight,onenine,twoone,twotwo,twothree,twofour,twofive,twosix,twoseven,twoeight,twonine,threeone,threetwo,threethree,threefour,threefive,threesix,threeseven,threeeight,threenine  = np.loadtxt(filename,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27))
	time=time*0.016     	
	l,p=filename.split(".txt")
	
	name=[oneone,onetwo,onethree,onefour,onefive,onesix,oneseven,oneeight,onenine]
	name2=[twoone,twotwo,twothree,twofour,twofive,twosix,twoseven,twoeight,twonine]
	name3=[threeone,threetwo,threethree,threefour,threefive,threesix,threeseven,threeeight,threenine]
	
	with open("%s_one_at_time_percentile.txt" %nameofplot,"w") as f:
		for i in name:
		
				
			coeff=np.polyfit(time,i,3)
			polynomial=np.poly1d(coeff)
			one0000=polynomial(0)
			one1000=polynomial(1000)
			one1500=polynomial(1500)
			one2000=polynomial(2000)
			one2500=polynomial(2500)
			one3000=polynomial(3000)
			one3500=polynomial(3500)
			one4000=polynomial(4000)
			one4500=polynomial(4500)
			one5000=polynomial(5000)
			one5500=polynomial(5500)
			f.write('%f %f %f %f %f %f %f %f %f %f %f\n' %(one0000,one1000,one1500,one2000,one2500,one3000,one3500,one4000,one4500,one5000,one5500))


		
	with open("%s_two_at_time_percentile.txt" %nameofplot,"w") as f:
		for i in name2:
		
			
			coeff=np.polyfit(time,i,3)
			polynomial=np.poly1d(coeff)
			two0000=polynomial(0)
			two1000=polynomial(1000)
			two1500=polynomial(1500)
			two2000=polynomial(2000)
			two2500=polynomial(2500)
			two3000=polynomial(3000)
			two3500=polynomial(3500)
			two4000=polynomial(4000)
			two4500=polynomial(4500)
			two5000=polynomial(5000)
			two5500=polynomial(5500)
			f.write('%f %f %f %f %f %f %f %f %f %f %f\n' %(two0000,two1000,two1500,two2000,two2500,two3000,two3500,two4000,two4500,two5000,two5500))


		
	with open("%s_three_at_time_percentile.txt" %nameofplot,"w") as f:
		for i in name3:
		
			
			coeff=np.polyfit(time,i,3)
			polynomial=np.poly1d(coeff)
			three0000=polynomial(0)
			three1000=polynomial(1000)
			three1500=polynomial(1500)
			three2000=polynomial(2000)
			three2500=polynomial(2500)
			three3000=polynomial(3000)
			three3500=polynomial(3500)
			three4000=polynomial(4000)
			three4500=polynomial(4500)
			three5000=polynomial(5000)
			three5500=polynomial(5500)
			f.write('%f %f %f %f %f %f %f %f %f %f %f\n' %(three0000,three1000,three1500,three2000,three2500,three3000,three3500,three4000,three4500,three5000,three5500))
	

	



if __name__ == "__main__":
	import sys
	percentileplot(str(sys.argv[1]),str(sys.argv[2]))

