class PlaceToGo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class University(PlaceToGo):
    ...
        
class Office(PlaceToGo):
    ...
    
class Person:
    def __init__(self, name, x, y, place_to_go):
        self.name = name
        self.x = x
        self.y = y
        self.place_to_go = place_to_go

    def get_distance_from_place_to_go(self):
        return (
            (self.place_to_go.x - self.x) ** 2 + (self.place_to_go.y - self.y) ** 2
        ) ** 0.5
        
class Student(Person):
    ...
        
class Employee(Person):
    ...
        
        
dsu = University(0, 0)
s = Student("Ibrahim", 10, 1, dsu)
# print(s.get_distance_from_place_to_go())
        
home = Office(1, 5)
e = Employee("Ibrahim", 10, 1, home)
# print(e.get_distance_from_place_to_go())

###

class Shape:
    name = "asd"
    def get_area(self):
        return 0

class Circle(Shape):
    def get_area(self):
        return "se"

# func_or_method_name (args) return_type

c = Circle()
print(c.name)
