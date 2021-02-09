poly = [ ]
ansrange = 100
charlist = [ ]

def evaluate(x):
	a = { }
	a

inputstr = input() + ';'
prev = 0;

inlen = len(inputstr)
for i in inputstr:
	if ord('a') <= ord(i) <= ord('z'):
		charlist.append(i)
charlist = list(dict.fromkeys(charlist))
if(inputstr[0] != '-'):
	inputstr = '+' + inputstr

i = 0
ncounting = False
while i < inlen:
	if(inputstr[i] == '-'):
		poly.append('|')
		poly.append('-1')
	elif inputstr[i] == '+' or inputstr[i] == ';': poly.append('|')
	else:
		if ord('0') <= ord(inputstr[i]) <= ord('9'):
			if ncounting == False:
				ncounting = True
				poly.append(inputstr[i])
			else:
				poly[len(poly)-1] = poly[len(poly)-1] + (inputstr[i])
		else:
			poly.append(inputstr[i])
			ncounting = False
	i += 1
print(poly)
