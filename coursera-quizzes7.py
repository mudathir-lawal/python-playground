cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for amphibian, organ in cool_beasts.items():
    print("{} have {}".format(amphibian, organ))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothing, colour_list in wardrobe.items():
	for colour in colour_list:
		print("{} {}".format(colour, clothing))
        
            