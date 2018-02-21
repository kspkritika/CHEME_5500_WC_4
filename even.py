sum=0
i=2
for x in range(1,49):
	i=i+2
	sum=sum+i
sum2=sum+2
print(sum2)

#i=1
#sum=0
#while i < 101:
	#if i%2==0:
		#sum=sum+i
#i=i+1
#print('sum of even numbers is:',sum)


def sumeven():
	n = 49.0
	a = 2.0
	l = 98.0
	#d = 2.0
	#S = (n/2)*(2*a+((n-1)*d))
	S = (n/2)*(a+l)
	return (S)
print(sumeven())
