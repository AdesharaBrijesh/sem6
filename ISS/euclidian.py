import math
def extendedeuclidian(r1,r2):
	q=0
	r=0
	t1=0
	t2=1
	s1=1
	s2=0
	s=0
	t=0
	i=0
	while r2!=0:
		if i>0:
			r1=r2
			r2=r
		if r2==0:
			q=0
			break
		q=math.floor(r1/r2)
		r=r1-(q*r2)
		if i>0:
			t1=t2
			t2=t
			s1=s2
			s2=s
		t=t1-(q*t2)
		s=s1=(q*s2)
		i+=1
	t1=t2
	t2=t
	s1=s2
	s2=s
	return r1,t1 

a=int(input("Enter first value : "))
b=int(input("Enter second value : "))
r1=max(a,b)
r2=min(a,b)
gcd,inverse=extendedeuclidian(r1,r2)
print("GCD for ",r1," and ",r2," is = ",gcd)
print("Multiplicative Inverse for ",r1," and ",r2," is = ",inverse)
