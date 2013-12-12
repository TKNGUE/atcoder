
from fileinput import input

def function():
	fin = input()
	line = fin.readline().strip().split(" ")
	N = int(line[0])
	K = int(line[1])
	RList = [ int(x) for x in fin.readline().strip().split(" ")]	
	
	RList.sort()
	optList = RList[N-K:N]
	
	optList.append(0)
	optList.sort()
	sumR = reduce(lambda c,r: 0.5*(c+r), optList)
	print sumR 

function()
