def fackt(n):
	if n<2:
		return 1
	f=1
	while n>=2:
		f*=n
		n-=1
	return f



print(fackt(0))
print(fackt(1))
print(fackt(2))
print(fackt(3))
print(fackt(4))
print(fackt(5))
