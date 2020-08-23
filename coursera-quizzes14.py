
class Repository:
     def __init__(self):
         self.packages = {}
     def add_package(self, package):
          self.packages[package.name] = package
     def total_size(self):
         result = 0
         for package in self.packages.values():
             result += package.size
         return result


class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

print(Turtle.category)

class Snake(Animal):
    category = "reptile"
