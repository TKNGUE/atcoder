#-*- coding:utf-8 -*-
from fileinput import input

atList = ['@','a','t','c','o','d','e','r']

def function():
	fin = input()
	str1 = fin.readline().strip()
	str2 = fin.readline().strip()

	for cnt in range(0,len(str1)):
		if str1[cnt] == '@' and str2[cnt] not in atList:
			print "You will lose"
			return		
		elif str2[cnt] == '@' and str1[cnt] not in atList:
			print "You will lose"
			return	
		elif str1[cnt] != str2[cnt]:
			print "You will lose"
			return	
	print "You can win"

function()

