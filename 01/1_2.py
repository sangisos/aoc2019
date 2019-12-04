#!/bin/python


def main():
	f=open("input","r")
	fuel=0
	for line in f:
		modfuel=int(line)//3-2
		addfule=modfuel//3-2
		while (addfule > 0) :
			modfuel+=addfule
			addfule=addfule//3-2
		fuel+=modfuel
	f.close()
	print(fuel)





if __name__=="__main__":
	main()
