class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.current = current
        self.top = top
        self.bottom = bottom
    
    def __str__(self):
        return "Current floor: {}".format(self.current)
        
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current == self.top:
            return
        else:
            self.current = self.current + 1
        
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current == self.bottom:
            return
        else:
            self.current = self.current - 1
        
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor >= self.bottom and floor <= self.top:
            self.current = floor
        else:
            return
        
elevator = Elevator(-1, 10, 0)



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


class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person.greeting)
