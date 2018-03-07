# -*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. 
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def ispalindrome(n):
	stringy = str(n)
	stringybackwards = stringy[::-1]
	if stringy == stringybackwards:
		return True
	else:
		return False


a = 100
b = 100
palindromes = []
while a<1000:
	while b<1000:
		if ispalindrome(a*b):
			palindromes.append(a*b)
		b+=1
	b=100
	a+=1
print(max(palindromes))
