#!/bin/python


def main():
	f=open("input","r")
	s=f.readline()
	line1 = [x for x in s.strip('\n').split(',')]
	s=f.readline()
	line2 = [x for x in s.strip('\n').split(',')]
	f.close()
	#print(line1)
	#print(line2)
	l1=[]
	cross=[]
	pos=[0,0]
	for subline in line1:
		distance=int(subline[1:])
		direction=subline[0] 
		dirvec=[0,0]
		if(direction == 'R'):
			dirvec[0]=1
		elif(direction == 'L'):
			dirvec[0]=-1
		elif(direction == 'U'):
			dirvec[1]=1
		elif(direction == 'D'):
			dirvec[1]=-1
		for step in range(distance):
			pos[0]+=dirvec[0]
			pos[1]+=dirvec[1]
			l1.append(pos.copy())

	pos=[0,0]
	for subline in line2:
		distance=int(subline[1:])
		direction=subline[0] 
		dirvec=[0,0]
		if(direction == 'R'):
			dirvec[0]=1
		elif(direction == 'L'):
			dirvec[0]=-1
		elif(direction == 'U'):
			dirvec[1]=1
		elif(direction == 'D'):
			dirvec[1]=-1
		for step in range(distance):
			pos[0]+=dirvec[0]
			pos[1]+=dirvec[1]
			if pos in l1:
				cross.append(pos.copy())
	print(cross)
	shortest=sum([abs(x) for x in cross[0]])
	for c in cross:
		d = sum([abs(x) for x in c])
		if d < shortest:
			shortest=d
	print(shortest)

if __name__=="__main__":
	main()
