import os
import numpy as np
import math
import time
import argparse
from compute_component_folding import *

#parameter setting
parser = argparse.ArgumentParser()

parser.add_argument('--m', type=int, default=1)     #Default values set to 1


parser.add_argument('--b', type=int, default=3)     #Default values set to 3
parser.add_argument('--h', type=int, default=100)
parser.add_argument('--w', type=int, default=576)
parser.add_argument('--l', type=int, default=32768)
args = parser.parse_args()

mode=int(args.m)
bit=int(args.b)
MH=int(args.h)
MW=int(args.w)
limit = int(args.l)
args = parser.parse_args()

start = time.time()
if (mode==1):
	print("You have chosen component optimization")
	[PE, SIMD]=compute_component_folding(bit,MH,MW,limit)

if (mode==2):
	print("You have chosen homogeneous ensemble optimization")
	layer=["C","L"]
	dim=np.array([[100,100],[100,100]])
	hw=np.array([[3,2],[1,1]])
	latency=np.array([200,100])
	lim=100
	scale=optimize_CNN(bit, layer, dim, latency, hw, limit)

if (mode==3):
	print("You have chosen heterogeneous ensemble optimization")

end = time.time()
delta = end - start

if (mode==1):
	print("PE: %d"%(PE))
	print("SIMD: %d"%(SIMD))
if (mode==2):
	print("You have chosen homogeneous ensemble optimization")

if (mode==3):
	print("You have chosen heterogeneous ensemble optimization")


print("took %.5f seconds to process" % delta)

      



