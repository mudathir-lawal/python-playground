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
