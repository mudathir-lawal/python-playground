

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


def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  print(words)
#   for word in words:
#     # Create the pig latin word and add it to the list
#     words.append('{}{}'.format(text[0], 'ay'))
#     # Turn the list back into a phrase
#     words = say.join(words)
#   return words
		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
