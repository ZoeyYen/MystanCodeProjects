"""
File: weather_master.py
Name:Zoey
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program is for weather data analysis, and It computes
	the highest, lowest, average, cold days among the inputs.
	"""
	print('stancode "Weather Master 4.0"!')
	n = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if n == EXIT:
		print('No temperatures were entered.')
	else:
		Max = n
		Min = n
		total = n
		total_days = 1
		if n < 16:
			cold_days = 1
		else:
			cold_days = 0
		while True:
			n = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
			if n == EXIT:
				break
			# Find the highest
			if n > Max:
				Max = n
			# Find the lowest
			if n < Min:
				Min = n
			# sum of input and count total days
			total = total + n
			total_days += 1
			# count the cold days( < 16)
			if n < 16:
				cold_days += 1
		print('Highest temperature = '+str(Max))
		print('Lowest temperature = '+str(Min))
		print('Average = '+str(total/total_days))
		print(str(cold_days)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
