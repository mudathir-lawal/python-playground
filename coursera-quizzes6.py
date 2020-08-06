

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [] 

for i, filename in enumerate(filenames):
  if filename.endswith('hpp'):  
    n = len(filename) - 2
    newfilenames.append(filename[:n])
    print('{}, {}, {}'.format(i, n, filename))
  else:
    newfilenames.append(filename)
    print('{}, {}, {}'.format(i, '-', filename))

print('{} {}'.format('\n', filenames))    
print('{} {}'.format('\n', newfilenames))  
print('\n\n')

###
def guest_list(guests):
	for index, guest in enumerate(guests):
		guest_name, age, occupation = guests[index]
		print('{} is {} years old and works as {}'.format(guest_name, age, occupation))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

def group_list(group, users):
  members = ""
  for idx, user in enumerate(users):
    if idx < len(users) - 1:
      members += (' {},'.format(user))
    else:
      members += (' {}'.format(user))   
  return '{}: {}'.format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
print('\n')

######
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for k in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if k >= value:
                result += letter
                k -= value
            else:
                result += '-'
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


def pig_latin(text):
  say = " "
  # Separate the text into words
  words = text.split()
  new_words_list = []

  for word in words:
    # Create the pig latin word and add it to the list
    new_words_list.append('{}{}{}'.format(word[1:], word[0], 'ay'))
    # Turn the list back into a phrase
  new_text = say.join(new_words_list)
  return new_text
		  
print('\n')      
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


####
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  return words

words = pig_latin("hello how are you")
print('\n')
print(words)
print(type(words))

####
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# Epilogue starts on page 39
# Chapter 3 now starts on page 24
# What are the current contents of the dictionary?
# Is there a Chapter 5?

toc["Epilogue"] = 39
toc["Chapter 3"] = 24
print(toc)
if "Chapter 5" in toc:
    print(True)
else:
    print(False)