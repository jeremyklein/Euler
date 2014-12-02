def fib(n):
	if n<2:
		return n
	return fib(n-2)+fib(n-1)


def main():
	number=0
	i=0
	sum=0
	while number<4000000:
		number=fib(i)
		if number%2==0:
			sum+=number
		i+=1
	print sum

main()