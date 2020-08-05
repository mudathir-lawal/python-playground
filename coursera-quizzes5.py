
print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
====
def student_grade(name, grade):
	return "{student} received {score}% on the exam.".format(student=name, score=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
=====
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for char in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if char != " ":
			new_string = new_string + char.upper()
			reverse_string = char.upper() + reverse_string
		else:
			continue		 
	# Compare the strings
	if reverse_string == new_string:
		return True
	return False

print(is_palindrome("Lawal")) # Should be True
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
============

def nametag(first_name, last_name):
	return("{first_name} {last_name_initial}.".format(first_name = first_name, last_name_initial = last_name[0] ))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 
============
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.2f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
=====================
Q:
5.Question 5
The replace_ending function replaces the old string in a sentence with the new 
string, but only if the sentence ends with the old string. If there is more than 
one occurrence of the old string in the sentence, only the one at the end is 
replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") 
should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-
sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no 
changes made).
====================
def replace_ending(sentence, old, new):
	is_both_lower = old.islower() == new.islower()
	is_both_upper = old.isupper() == new.isupper()
	is_same_case = is_both_lower or is_both_upper
	first_part = sentence[:len(sentence) - len(old)]
	# Check if the old string is at the end of the sentence 
	# if first_part == old and is_same_case:
	if sentence.endswith(old) and is_same_case:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = ""
		new_sentence = i.join([first_part, new])
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
================================
def convert_distance(miles):
	km = miles * 1.6 
	miles = int(miles)
	result = '{:>2d} miles equals {:>5.2f} km'.format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
==============

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing
========

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for char in elements:
		# Does this element belong in the resulting list?
		if (i == 0) or ((i % 2) == 0):
			# Add this element to the resulting list
			new_list.append(char)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
===========
def file_size(file_info):
	file_name, file_format, file_size= file_info # Unpack tuple
	return("{:>5.2f}".format(file_size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
=====
def skip_elements(elements):
	# code goes here
	char_list = []
	for index, string in enumerate(elements):
		if index % 2 == 0 or index == 0:
			char_list.append(string)
	return char_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
======


def get_users_contact(info_list):
  i = 0
  contact_list = []

  for full_name, email in enumerate(info_list[i]):
    full_name, email = info_list[i]
    contact_list.append(('{full_name}<{email}>').format(full_name=full_name, 
    email=email))
    i += 1
  return contact_list  

sample_list = [('Femi Akinshiku', 'femi.akins@andela.com'), ('Mudathir Lawal', 
'mudathir.lawal@google.com'), ('Ammaar AbduSalaam', 'ammar.as@berkley.edu')]
print(get_users_contact(sample_list))
print(typeof(contact_list[0]))
============

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [] 

for i, filename in enumerate(filenames):
  if filename.endswith('hpp'):  
    n = len(filename) - 2
    newfilenames.append(filename[:n])
    print('{}, {}, {}'.format(i, n, filename))
    
print('{} {}'.format('\n', newfilenames)) 

