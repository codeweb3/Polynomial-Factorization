import numpy as np

poly = [ ]

inputstr = input() + ';'
i = 1
prev = 0;
inlen = len(inputstr)
if(inputstr[0] != '-'):
	inputstr = '+' + inputstr
while i < inlen:
	while i < inlen:
		if(inputstr[i] == '+' or inputstr[i] == '-' or inputstr[i] == ';'):
			break;
		i += 1
	ncounting = False
	if(inputstr[prev] == '-'): poly.append('-1')
	for j in inputstr[prev+1:i]:
		#print(inputstr[j], end = "")
		if ord('0') <= ord(j) <= ord('9'):
			if ncounting == False:
				ncounting = True
				poly.append(j)
			else:
				poly[len(poly)-1] = poly[len(poly)-1] + (j)
		else:
			poly.append(j)
			ncounting = False
	poly.append("|")
	prev = i
	i += 1
print(poly)