from prehisto import prehisto
from prehistoric import prehistoric
import matplotlib.pyplot as plt


def histoplot(nameofplot,name1,name2,name3,namesy): 

	
	prehisto(name1,"first 1%","blue")
	prehisto(name2,"second 1%","red")
	prehisto(name3,"same mass as first 1%","green")


	plt.title('%s_%s'%(nameofplot,namesy))
	plt.ylabel('number of particles')
	plt.xlabel('r')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_%s.pdf" %(nameofplot,namesy))
	plt.close()
	
	prehistoric(name1,"first 1%","blue")
	prehistoric(name2,"second 1%","red")
	prehistoric(name3,"same mass as first 1%","green")
	
	plt.title('%s_derivative_time_0000'%nameofplot)
	plt.ylabel('log (Density)')
	plt.xlabel('log (r)')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_der_%s.pdf" %(nameofplot,namesy))
	plt.close()






if __name__ == "__main__":
	import sys
	histoplot(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))
