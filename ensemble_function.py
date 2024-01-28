import os
import numpy as np
import math
import time
import argparse
import copy

def compute_component_folding(bit,MH,MW,limit):
	PE=1
	SIMD=1

	best=0
	#start = time.time()
	for j in range(1,math.ceil(MW/2)+1):
		for i in range(1,math.ceil(MH/2)+1):
			if (MH%i==0 and MW%j==0):
				if MH/i*MW/j*bit<32768:
					if MH/i*MW/j*bit>best:
						PE=MH/i
						SIMD=MW/j
						best=MH/i*MW/j*bit

	#end = time.time()
	#delta = end - start
	#print("took %.5f seconds to process" % delta)

	#print("PE: %d"%(PE))
	#print("SIMD: %d"%(SIMD))

	return PE, SIMD

def next_component_folding(bit,MH,MW,limit,ki,kj):
	PE=ki
	SIMD=kj
	done=0
	
	best=PE*SIMD*bit
	print('best')
	print(best)
	#start = time.time()
	for i in range(ki,math.ceil(MH/2)+1):
		if(done!=1):
			for j in range(kj,math.ceil(MW/2)+1):
				if(done!=1):
					print(j)
					if (MH%i==0 and MW%j==0):
						print(j)
						print(i*j*bit)
						print(i*j*bit<32768)
						if i*j*bit<32768:
							print(j)
							print(i*j*bit>best)
							if i*j*bit>best:
								print(j)
								PE=i
								SIMD=j
								best=i*j*bit
								done=1
								print(best)



	#end = time.time()
	#delta = end - start
	#print("took %.5f seconds to process" % delta)

	print("PE: %d"%(PE))
	print("SIMD: %d"%(SIMD))

	return PE,SIMD

def optimize_CNN(bit, layer, dim, latency, hw, limit):
	print((dim))
	print(np.shape(dim))
	scale = np.ones(dim.shape, dtype=int)
	print('scale')
	print(scale)
	temp_scale=copy.deepcopy(scale)
	for i in range(0,len(layer)):
		print(i)
		[MH,MW]=dim[i,:]
		print(dim)
		[PE,SIMD]=next_component_folding(bit,MH,MW,limit,scale[i,0],scale[i,1])
		print([PE,SIMD])
		temp_scale[i,:]=[PE,SIMD]
	for i in range(0,len(layer)):
		print(i)
		temp=copy.deepcopy(scale)
		#print("temp")
		#print(temp)
		#print("scale")
		#print(scale)
		temp[i,:]=temp_scale[i,:]
		#print(temp_scale[i,:])
		#print("temp")
		#print(temp)
		#print("scale")
		#print(scale)
		


	return scale
 
def compute_latency(scale, latency):

def compute_hw(scale, hw):



      



