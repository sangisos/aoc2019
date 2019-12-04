#!/bin/python


def main():
	f=open("input","r")
	fuel=0
	for line in f:
		fuel+=int(line)//3-2
	f.close()
	print(fuel)





if __name__=="__main__":
	main()
