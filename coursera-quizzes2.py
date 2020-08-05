def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
    # keep just the fractional part of the quotient
	if denominator == 0:
	    return 0
	decimal = numerator % denominator	
	return decimal / denominator
	

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)
	


def format_name(first_name, last_name):
	# code goes here
	if first_name and last_name:
		string = "Name: " + last_name + ", " + first_name
	elif first_name and last_name != True:
		string = "Name: " + first_name
	elif last_name != "" and first_name == "": # Using a diff style here
		string = "Name: " + last_name
	elif first_name != True and last_name != True:
		string = ""	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string



def exam_grade(score):
	if score > 95 and score <= 100:
		grade = "Top Score"
	elif score >= 60 and score <= 100:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)
===

def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
===
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
===
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
===
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
===
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24
======

def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  divisor = 1
  while ( divisor < n ) and ( n % divisor == 0 ):
    # if divisor == n:
    #   divisor += 1
    #   break
    sum += divisor
    divisor += 1
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
=====

def func(num):
    add = []
    total_sum = 0
    for i in range(1, num - 1):
        if num % i == 0:
            add.append(str(i))
            total_sum += i

    return "{}={}".format("+".join(add), total_sum)
    ===