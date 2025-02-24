def isPrime(start, end):
	prime = []
	for num in range(max(2,start), end+1):
		isPrime=True
		for i in range(2, int(num**0,5)+1):
			if num % i == 0:
				isPrime = False
				break
		if isPrime:
			prime.append(num)
	return prime
s = int(input())
e = int(input())
result = isPrime(s,e)
print(result)
