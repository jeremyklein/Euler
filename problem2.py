def main():
	sum=0
	fib=1
	while fib<4000000:
		fib+=fib
		print fib
		if fib%2==0:
			sum=sum+fib
			print fib
			print sum
	print sum

main()