import numpy as np

poly = [ ]

inputstr = input() + ';'
i = 1
prev = 0;
inlen = len(inputstr)
while i < inlen:
	while i < inlen:
		if(inputstr[i] == '+' or inputstr[i] == '-' or inputstr[i] == ';'):
			break;
		i += 1
	for j in inputstr[prev:i]:
		#print(inputstr[j], end = "")
		if j == '+': continue
		elif j == '-': poly.append('-1')
		else: poly.append(j)
	poly.append("|")
	prev = i
	i += 1
print(poly)
