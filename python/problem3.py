"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def primefactors(n):
	primefactors = []
	i = 2
	while n > 1:
		if n%i == 0:
			primefactors.append(i)
			n/=i
		i+=1 
	return primefactors

print max(primefactors(600851475143))