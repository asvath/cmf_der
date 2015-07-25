from histogram import histoplot
from prehisto import prehisto
from prehistoric import prehistoric 	
import cfg
import numpy as np

onezero,oneone,oneonefive,onetwo,onetwofive,onethree,onethreefive,onefour,onefourfive,onefive,onefivefive = np.loadtxt("%s_one_at_time_percentile.txt" %cfg.name,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))
twozero,twoone,twoonefive,twotwo,twotwofive,twothree,twothreefive,twofour,twofourfive,twofive,twofivefive = np.loadtxt("%s_two_at_time_percentile.txt" %cfg.name,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))
threezero,threeone,threeonefive,threetwo,threetwofive,threethree,threethreefive,threefour,threefourfive,threefive,threefivefive = np.loadtxt("%s_three_at_time_percentile.txt" %cfg.name,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))






histoplot(cfg.name,onezero,twozero,threezero,"0000")
histoplot(cfg.name,oneone,twoone,threeone,"1000")
histoplot(cfg.name,oneonefive,twoonefive,threeonefive,"1500")
histoplot(cfg.name,onetwo,twotwo,threetwo,"2000")
histoplot(cfg.name,onetwofive,twotwofive,threetwofive,"2500")
histoplot(cfg.name,onethree,twothree,threethree,"3000")
histoplot(cfg.name,onethreefive,twothreefive,threethreefive,"3500")
histoplot(cfg.name,onefour,twofour,threefour,"4000")
histoplot(cfg.name,onefourfive,twofourfive,threefourfive,"4500")
histoplot(cfg.name,onefive,twofive,threefive,"5000")
histoplot(cfg.name,onefivefive,twofivefive,threefivefive,"5500")

