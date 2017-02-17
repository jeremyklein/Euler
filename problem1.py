

def main():
	num=[]
	dups=[]
	sum=0
	sumDups=0
	for i in range (0,1000):
		if (i%3==0):
			num.append(i)
		if(i%5==0):
			num.append(i)
		if (i%3==0)&(i%5==0):
			dups.append(i)
	for i in range (len(dups)):
		sumDups+=dups[i]
	for i in range(len(num)):
		sum+=num[i]
	print sum-sumDups
main()

