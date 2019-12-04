#!/bin/python

def corners(line):
	pos=[0,0]
	l=[]
	for subline in line:
		distance=int(subline[1:])
		direction=subline[0] 
		if(direction == 'R'):
			pos[0]+=distance
		elif(direction == 'L'):
			pos[0]+=-distance
		elif(direction == 'U'):
			pos[1]+=distance
		elif(direction == 'D'):
			pos[1]+=-distance
		l.append(pos.copy())
	return l

def main():
	f=open("input","r")
	s=f.readline()
	line1 = [x for x in s.strip('\n').split(',')]
	s=f.readline()
	line2 = [x for x in s.strip('\n').split(',')]
	f.close()
	#print(line1)
	#print(line2)
	cross=[]
	pos=[0,0]
	l1=corners(line1)
	l2=corners(line2)
	#print(l1)
	#print(l2)
	p11=[0,0]
	p21=[0,0]
	for p12 in l1:
		for p22 in l2:
			if p12[0] == p11[0] and p21[1] == p22[1]:
				if (p11[1] < p21[1] and p21[1] < p12[1]) or (p12[1] < p21[1] and p21[1] < p11[1]):
					if (p21[0] <= p11[0] and p11[0] <= p22[0]) or (p22[0] <= p11[0] and p11[0] <= p21[0]):
						cross.append([p11[0],p21[1]])
			elif p12[1] == p11[1] and p21[0] == p22[0]:
				if (p11[0] < p21[0] and p21[0] < p12[0]) or (p12[0] < p21[0] and p21[0] < p11[0]):
					if (p21[1] <= p11[1] and p11[1] <= p22[1]) or (p22[1] <= p11[1] and p11[1] <= p21[1]):
						cross.append([p21[0],p11[1]])
			p21=p22
		p11=p12
	#print(cross)
	shortest=sum([abs(x) for x in cross[0]])
	for c in cross[1:]:
		d = sum([abs(x) for x in c])
		if d < shortest:
			shortest=d
	print(shortest)

if __name__=="__main__":
	main()
