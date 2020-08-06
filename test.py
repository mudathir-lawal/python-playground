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




def group_list(group, users):
  members = ""
  for user in users:
      members += (' {},'.format(user))  
  return '{}: {}'.format(group, members.__(len(users) - 1))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


# UNDER CONSTRUCTION:
# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = text.split()
#   print(words)
#   for word in words:
#     # Create the pig latin word and add it to the list
#     words.append('{}{}'.format(text[0], 'ay'))
#     # Turn the list back into a phrase
#     words = say.join(words)
#   return words
		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
