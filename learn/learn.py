import string

# Type checking
a = 1
print (a, type(a))
a = 1.1
print(a, type(a))
a = "virat"
print(a, type(a))


b = a[1:]

# String concatination
b = "T" + b

a = 1 + 1.5 + 2
print(a, type(a))

# string package usage
print(b.upper())

# string formattting
print(' I like {}'.format('apples'))
print('Players order: {y}, {x}, {z}' .format(x = 'virat', y = 'ajinkya', z = 'MS'))

# Floating number formatting
float_n = 104.256987
print(float_n)
print('number set to precison: {r:1.3f}'.format(r=float_n))

# fstrings
name = 'virat'
age = 29
print(f'{name} is {age} years old')

# -------------------------------------------------------- List ------------------------------------------------------------------------

myList = ["Virat", 29, 59.5]

print(len(myList))
print("{x} is {y} years old and has average of {z}".format(x=myList[0], y=myList[1], z=myList[2]))
print(f"{myList[0]} is {myList[1]} years old and has average of {myList[2]}")


# Type concatination
list = ["one", "two", "three"]
anotherList = ["four", "five"]
print(list + anotherList)
list = list + anotherList
print(list)

# mutate elements in list
list[0] = 'ONE'
print(list)

# append to list
list.append('six')
print(list)

# pop operation
a = list.pop()
print(a)
print(list)

# pop operation at index position
a = list.pop(0)
print(a)
print(list)
a = list.pop(-1)
print(a)
print(list)

# sort list
list = ['b', 'a', 't', 'u', 'w']
print(list)
list.sort()
print(list)
list.reverse()
print(list)

list = [56,34,12,10,1,5]
print(list)
list.sort()
print(list)
list.reverse()
print(list)

# Sort using method
list = [56,34,12,10,1,5]
new_list = sorted(list)
print(new_list, list)

# ----------------------------------------------------------- Dictionaries ----------------------------------------------------------------
priceLookup = {'apple':180, 'orange':80}
print(priceLookup['apple'])
# dictionary is similar to list, it can hold different types
my_dict = {"apple":180, 3:"Virat", "k1" : [1, "key1"], "k2": {"passwd1": 100, "passwd2": 200}, "k3":['a','b','c']}
print(my_dict["apple"], my_dict[3], my_dict["k1"], my_dict['k2']) 
# accesing values by indexing
print(my_dict["k1"][1], my_dict["k2"]["passwd2"])
# accessing value by index and processing
print(my_dict["k3"][2].upper())
# adding element to dictionary
my_dict["vmware"] = 12
print(my_dict)
# changing value of any key
my_dict["apple"] = 190
print(my_dict["apple"])
# accesing list of keys from dictionary
print(my_dict.keys())
#accessing values
print(my_dict.values())
# accessing both key values as tuple
print(my_dict.items())

#---------------------------------------------------------------Tuple----------------------------------------------------------------------
t = ('virat', 29, 59)
print(t[0])
# couting on tuple
t = ('a', 'a', 'a', 'a', 1,2,3,1)
print(t.count('a'), t.count(1))
# indexing tuple
print(t.index(1))
# Tuple are immutable, we cannot do this ex: t[0] = 'kohli'

# ----------------------------------------------------- sets -------------------------------------------------------------------
myset = set()
print(myset)
myset.add(1)
myset.add("Virat")
myset.add(2.3)
print(myset)
# no duplicates allowed in sets
myset.add(1)
myset.add(2.3)
print(myset)
# typecasting list to set
my_list = [7,7,7,3,3,3,1,1,1,1,1]
myset = set(my_list)
print(myset)
# Indexing does not work on sets ex: print(myset[1])

# none data type
a = None
print(type(a))

# ----------------------------------------------------------- File operations ----------------------------------------------------
myfile = open('test.txt')
print(myfile.read())
# Seek set the file
myfile.seek(0)
# save the content
content = myfile.read()
print(content)
# To get file content line by line
myfile.seek(0)
content = myfile.readlines()
print(content)
#accessing the lines as index
print(content[0], content[1])
myfile.close()

# below doesnot require close() of a file, when the block ends, the file gets closed
with open("test.txt") as myfile:
    content = myfile.read()

# Open file in append mode
with open("test.txt", mode='a') as myfile:
    myfile.write("I am learning GO")
with open("test.txt", mode='r') as myfile:
    content = myfile.read()
print(content)
# creates file
with open("abc.txt", mode='w') as myfile:
    myfile.write("I am learning python")
with open("abc.txt", mode='r') as myfile:
    content = myfile.read()
print(content)

#----------------------------------------------------------- Control flow ---------------------------------------------------------------
hungry = False
if hungry:
    print('I am not hungry')
else:
    print("I am hungry")

loc = "IT"

if loc == "IT":
    print("Bangalore")
elif loc == "MONEY":
    print("Mumbai")
elif loc == "Politics":
    print("Delhi")
else:
    print("Does not exist")

myList = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for v in myList:
    if v %2 == 0:
        sum += v
print(f"sum of even numbers = {sum}")

for v in "hello":
    print(v)

# empty receiver
for _ in "hello":
    print("Hi")

# tuple
t = (1,2,3)

for v in t:
    print(v)

my_list = [(1,2),(3,4),(4,5)]
for v in my_list:
    print(v)

# tuple unpacking, we can access the individual elements
my_list = [(1,2),(3,4),(4,5)]
for a, b in my_list:
    print(a)

# iterate through the dictionaries
my_dict = {'k1':1, 'k2': 2, 'k3':3}
for v in my_dict:
    print(v)
for v in my_dict.items():
    print(v)
for key, value in my_dict:
    print(key, value)
for value in my_dict.values():
    print(value)

x = 0
while x < 5:
    print(x)
    x = x +1
else:
    print("x is not less than 5")

for v in my_dict:
    # nothing to be done then use
    pass

for v in "hello":
    if v == 'e':
        continue
    print(v)

for v in "hello":
    if v == 'e':
        break

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x = x +1

# range operator range (start, stop, [step])
for v in range(3,10,2):
    print(v)

# enumerate operator
s = "hello"
for v in enumerate(s):
    print(v)

for index, letter in enumerate(s):
    print(index)
    print(letter)

# zip function returns tuple, zips to list which is shortest 
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [100,200]

for v in zip(list1, list2, list3):
    print(v)

for a, b,c in zip(list1, list2, list3):
    print(b)

list1 = zip(list1, list2)
print(list1)

# in operator
list1 = ['a','b','c']
a = 'a' in list1
print(a)

a = 'key1' in {'key1': 123}
print(a)

d = {'key1': 123}
a = 123 in d.values()
print(a)
a = 'key2' in d.items()
print(a)

# min and max operator
myList = [12,23,1,67,34]
print(min(myList))
print(max(myList))

# importing method from a library
from random import shuffle
myList = [12,23,1,67,34, 12,78,45]
# shuffle dont return anything, its inplace function
shuffle(myList)
print(myList)

from random import randint
a = randint(0, 100)
print(a)

# taking input from user, always takes as string
# ip = input("Enter input: ")
# print(ip, type(ip))
# a = int(ip)
# print(a, type(a))

# ----------------------------------------------------- list comprehensions ------------------------------------------------------------
myList = []
for v in "hello":
    myList.append(v)
print(myList)

# we can do above using this
myList = [v for v in "hello"]
print(myList)

myList = [v for v in range(2, 10, 2)]
print(myList)

myList = [v**2 for v in range(2, 10, 2)]
print(myList)

myList = [v**2 for v in range(2, 10) if v % 2 == 0]
print(myList)

celcius = [10,20,35.5, 45]
fahr = [((9/5) * v + 32) for v in celcius]
print(fahr)

# some complex stuff, double loop using comphrehensions
result = [x * y for x in [1,2,3] for y in [1,10,1000] ]
print(result)

