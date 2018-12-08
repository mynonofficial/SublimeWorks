def fibo():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b



for num in zip(range(10),fibo()):
	print(num)

