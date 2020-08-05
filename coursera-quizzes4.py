def factorial(n):
    result = 1
    for x in range(1, n):
        if ( n == 0 ):
            result = result * 1
        else:    
	        result = result * n
	        n = n - 1
    return result

for n in range(0, 9):
    print(n, factorial(n + 1))

====

def factorial(n):
    result = 1
    for x in range(1,___):
        result = ___ * ___
    return ___

for n in range(___,___):
    print(n, factorial(n+___))

===
def get_multiples_of_7():
    for n in range(100):
        if ( n % 7 == 0 or n == 0 ):
            print(str(n) + '\n' )
        else:
          continue    

get_multiples_of_7()
====
===

def retry(operation, attempts):
  for n in range(attempts):
    if operation:
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)
====

def factorial(n):
    result = 1
    for x in range(1, n):
        if ( n == 0 or n == 1 ):
            result = result * 1
        else:    
	        result = result * n
	        n = n - 1
    return result

for n in range(0, 10):
    print(n, factorial(n + 0))
======

def sum_positive_numbers(n):
    sum = 0
    # The base case is n being smaller than 1
    if n < 1:
        return sum
    sum += n        

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return sum + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

=======
def digits(n):
	count = 0
	new_num = 0
	if n == 0:
	  return 1
	while (n > 0):
		count += 1
		last_digit = n % 10
		residue_num = n - last_digit
		n = residue_num / 10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
==========================

def multiplication_table(start, stop):
	for x in range(1, 4):
		for y in range(1, 4):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
=====
def even_numbers(maximum):
	return_string = ""
	for x in range(2, (maximum + 1), 2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
============

def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
===========

def double_word(word):
    return (word * 2) + str(len(word * 2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

===========

def first_and_last(message):
    if message == "":
        return True
    else:
        if message[0] == message[-1]:
            return True    
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
=====

word = "supercalifragilisticexpialidocious"
print(word.index("x"))
=====
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()
