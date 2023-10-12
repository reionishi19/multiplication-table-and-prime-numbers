"""
Rei Onishi
September 21, 2023

This program will print out a multiplication table and print out prime numbers within a criteria.
"""

#8 and 10 times table.

for timestable8 in range(1, 8+1): 
    for timestable10 in range(1, 10+1):
        multiplication = timestable8 * timestable10
        print("%2d" % (multiplication), end=' ') #This will print horizontally
    print() #This will print the next loop on the next line
   
#Printing prime numbers below 250

for number in range(2,250):
	prime= True
	for x in range(2, number):
		if number % x == 0:
			prime = False
			break
	if prime == True:
		print(number)

#Printing prime numbers that end in 3
for number in range(2,250):
	prime = True
	for x in range(2, number):
		if (number % x == 0):
			prime = False
			break
	if (prime == True) and (number % 10 == 3):
		print(number)


#Printing prime numbers OR perfect numbers
for number in range(2, 250):
    prime = True
    for x in range(2, number):
        if number % x == 0:
            prime = False
            break
    divisors_sum = 0
    for x in range(1, number):
        if number % x == 0:
            divisors_sum += x
    if (prime == True) or (divisors_sum == number):
        print(number)

