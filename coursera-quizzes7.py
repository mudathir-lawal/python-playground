cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for amphibian, organ in cool_beasts.items():
    print("{} have {}".format(amphibian, organ))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothing, colour_list in wardrobe.items():
	for colour in colour_list:
		print("{} {}".format(colour, clothing))

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      if letter not in result:
        result[letter] = 0
      # Add or increment the value in the dictionary
      result[letter] += 1 
    else:
      continue  
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

