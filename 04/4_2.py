#!/bin/python

def main():
	s = 0
	n = 707912
	while n >= 165432:
		#print(n)
		a = n // 100000
		a1 = n%100000
		b = a1 // 10000
		if(a > b):
			#print(n,a,b,a1)
			n-=a1+1
			#print(n)
			continue
		b1 = n%10000
		c = b1 // 1000
		if(b > c):
			n-=b1+1
			continue
		c1 = n%1000
		d = c1 // 100
		if(c > d):
			n-=c1+1
			continue
		d1 = n%100
		e = d1 // 10
		if(d > e):
			n-=d1+1
			continue
		f = n%10
		if(e > f):
			n-=f+1
			continue
		#if (a!=b and b!=c and c!=d and d!=e and e!=f):
		#	n-=1
		#	continue
		#if a==b and b==c or b==c and c==d or c==d and d==e:
		#	c
		r=[a,b,c,d,e,f]
		doubleexists=False
		streak=0
		l=0
		for i in range(len(r)):
			if r[i] == l: 
				doubleexists = True
				streak+=1
				if streak > 1 :
					doubleexists = False 
				#print(n, doubleexists)
			else:
				streak=0
				if doubleexists:
					break
			l=r[i]

		#print(a,b,c,d,e,f)
		if doubleexists:
			s+=1
		n-=1
	print(s)

	

if __name__=="__main__":
	main()
