#!/bin/python


def main():
	f=open("input","r")
	s=f.read()
	f.close()
	prg = [int(x) for x in s.strip('\n').split(',')]
	prg[1]=12
	prg[2]=2
	del(s)
	for i in range(0,len(prg),4):
		if prg[i] == 99:
			break
		if i < prg[i+3]:
			print(prg[0:i],
				" ->-> i:",i,prg[i:i+4]," <-<- ",
				prg[i+4:prg[i+3]],
				"-------->",prg[prg[i+3]],"<----------",
				prg[prg[i+3]+1:])
		else:
			print(prg[0:prg[i+3]],
				"-------->",prg[prg[i+3]],"<----------",
				prg[prg[i+3]+1:i],
				" ->-> i:",i,prg[i:i+4]," <-<- ",
				prg[i+4:])

		if prg[i]==1:
			prg[prg[i+3]]=prg[prg[i+1]]+prg[prg[i+2]]
		if prg[i]==2:
			prg[prg[i+3]]=prg[prg[i+1]]*prg[prg[i+2]]

		
	print(prg[0])
	print(len(prg))





if __name__=="__main__":
	main()
