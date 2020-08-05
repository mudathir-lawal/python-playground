
Tip: to calculate the square root of a number xx, you can use x**(1/2).
#===#

num_square = 5 ** ( 1 / 2 )
ratio = ( 1 + num_square ) / 2
print( ratio )

num_square = 5 ** ( 1 / 2 )
ratio = ( 1 + num_square ) / 2
print( ratio )
#===#

bill = 47.28
tip = bill * (15/100)
total = bill + tip
share = total / 2
print("Each person needs to pay: " + str(share))

#===#
numerator = 10
denominator = 10
result = numerator / denominator
print(int(result))
#===#
print("2 + 2 = " + str(2 + 2))
#===#
def print_seconds(hours, minutes, seconds):
    print((hours * 3600) + (minutes * 60) + (seconds * 1))

print_seconds(1,2,3)
#===#
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(str(result))
#===#

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION

def month_days(month, days):
    print(month + " has " + str(days) + " days.")

month_days("July", 31)
month_days("June", 30)
#===#

def get_rectangle_area(base, height): 
    rectangle_area = base * height
    print("The area of the rectangle is: " + str(rectangle_area))

get_rectangle_area(12, 4)

#===#
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km * 2))
#===#

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#===#
def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
#===#


def is_positive(number):
  if number > 0:
    return True
  return None  
#===# 
def is_even(number):
  if number % 2 == 0:
    return True
  return False  
#===#

"""
While explaining that: "The body of the else statement is indented to the right,
and will be ``executed`` if the above if statement doesn’t execute," ``expected`` 
is written instead of ``executed`` 

Could you please correct the typographical error because it can lead to a 
technical confusion for learners. 

Thank you. 

On the third line of the first paragraph, no space is inserted between the words 
"if" and "block." It was written ifblock intead of "if block."
"""


def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks + 1) 
    return block_size * full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
