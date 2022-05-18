"""
File: prime_checker.py
Name:Zoey
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. At the beginning, ” Welcome to the prime checker” is printed on Console.
And the program will ask the user to enter an integer that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	Check if input number is a prime or not.
	"""
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n (or -100 to quit): '))
		if n == EXIT:
			break
		elif n <= 1:
			print('please input an integer that is greater than 1')
		elif is_prime(n):
			print(str(n) + ' is a prime number')
		else:
			print(str(n) + ' is not a prime number')
	print('Have a good one!')


def is_prime(n):
	"""
	: param n: int, an integer that is greater than 1
	: return : bool, True if n is a prime number; False if n is not a prime number
	"""
	i = 1
	while True:
		i += 1
		if n % i == 0:
			break
	if i == n:
		return True


	# i = 2
	# while i <= n:
	# 	if n % i != 0:
	# 		i += 1
	# 	else:
	# 		break
	# if i == n:
	# 	return 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
