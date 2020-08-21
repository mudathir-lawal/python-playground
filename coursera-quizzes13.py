class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"
#____

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"


class Piglet:
	pass

hamlet = Piglet()	
	
class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "Hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Mudathir") 
# Call the greeting method
print(some_person.greeting())
