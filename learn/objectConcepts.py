'''
class Dog():
    species = 'mammal'
    def __init__ (self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    
    def bark(self, num):
        print("WOOF!! my name is {} and number is {}".format(self.name, num))

my_dog = Dog("huskie", "whiskey", "NO_SPOTS")
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)

your_dog = Dog("lab", "brandy", "SPOTS")
print(your_dog.breed)
print(your_dog.name)
print(your_dog.spots)
print(your_dog.species)

my_dog.bark(420)
your_dog.bark(240)

class Circle():
    pi = 3.142
    def __init__(self, radius=1):
        self.radius = radius
        self.area = Circle.pi * radius * radius

    def get_circum(self):
        return 2 * Circle.pi * self.radius

my_circ = Circle(30)
print(my_circ.get_circum())
print(my_circ.area)

# --------------------------------------------------- in heritance ----------------------------------------------------------
class Animal():
    def __init__(self):
        print("Animal created")
    
    def who_am_i(self):
        return "I am an animal"
    def eat (self):
        return "I am eating"

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog is created")

    def bark(self):
        return "Woof!!"
    
    def eat (self):
        return "I am a dog and eating"
    
my_dog = Dog()
print(my_dog.who_am_i())
print(my_dog.eat())
print(my_dog.bark())
# -------------------------------------------------- polymorphism ----------------------------------------------------------------

class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says Woof!!"

class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says Meow"

def pet_speak(pet):
    return pet.speak()

my_cat = Cat("Rum")
my_dog = Dog("Whiskey")

print(pet_speak(my_dog))
print(pet_speak(my_cat))

# --------------------------------------------------- polymorphism and inheritence --------------------------------------------

class Animal():
    def __init__(self, name):
        self.name = name
    
class Dog(Animal):
    
    def speak(self):
        return self.name + " says Woof!!"

class Cat(Animal):
    
    def speak(self):
        return self.name + " says Meow"

def pet_speak(pet):
    return pet.speak()

my_cat = Cat("Rum")
my_dog = Dog("Whiskey")

print(pet_speak(my_dog))
print(pet_speak(my_cat))

# ---------------------------------------------- magic/dunder method starts with __ (underscore, underscore)--------------------------

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"book title: {self.title}, author: {self.author} and contains {self.pages} pages"
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print (f"{self.title} is deleted")

b = Book("learn Go", "Caleb Doxsey", 200)
print(b)
print(len(b))
del b
print(b)

'''