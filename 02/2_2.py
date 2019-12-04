#!/bin/python


def main():
	f=open("input","r")
	s=f.read()
	f.close()
	prgorig = [int(x) for x in s.strip('\n').split(',')]
	del(s)
	noun=-1
	verb=0
	while(True):
		noun+=1
		if(noun>99):
			noun=0
			verb+=1
		prg=prgorig.copy()
		prg[1]=noun
		prg[2]=verb
		for i in range(0,len(prg),4):
			if prg[i] == 99:
				break
			if prg[i]==1:
				prg[prg[i+3]]=prg[prg[i+1]]+prg[prg[i+2]]
			if prg[i]==2:
				prg[prg[i+3]]=prg[prg[i+1]]*prg[prg[i+2]]
		if prg[0]==19690720:
			break
		
	print(noun)
	print(verb)





if __name__=="__main__":
	main()
