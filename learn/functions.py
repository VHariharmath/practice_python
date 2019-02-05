
'''
def printString(str):
    print(str)

printString("hello world")

def add(num1, num2):
    return num1+num2

print(add(10,20))

def dog_check(str):
    if 'dog' in str.lower():
        return True
    else:
        return False

print(dog_check("Beaware of Dog"))

def dog_check2(str):
    return 'dog' in str.lower()

print(dog_check2("Beaware of DOg"))

def pig_latin(str):
    l = str[0]
    if l in 'aeiou':
        return str + 'ay'
    else:
        return str[1:] + l + 'bd'

print(pig_latin('apple'))

def prime_number(num1):
    for v in range(2, int (num1/2)):
        if num1 % v == 0:
            return False
        else:
            return True

print(prime_number(33))
print(prime_number(24))

#-------------------------------------------------------- *args and **kwargs---------------------------------------------------
def my_func1(a, b):
    return sum((a, b)) * 0.05

print(my_func1(40,60))

# args return/provide tuple
def my_func2(*args):
    for item in args:
        print(item)

my_func2(10,20,30,40,50,60,70)

def my_func3(*args):
    return sum(args) * 0.05

print(my_func3(40,60,100))

# kwargs return/provide dictionary
def my_func4(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("Fruit selected is {}".format(kwargs['fruit']))
    else:
        print("Not present")

my_func4(fruit="Apple", veggie = 'carrot')

def my_func5(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I have {} {}".format(args[0], kwargs['food']))

my_func5(10,20,30, fruit = 'orange', food='eggs')

# -----------------------------------------functions excercise---------------------------------------------------------------------

def my_func6(a, b):
    if a % 2 ==0 and b %2 ==0:
        return min(a, b)
    else:
        return max(a,b)

print(my_func6(10 , 20))
print(my_func6(11, 13))

def my_func7(x, y):
    a = x.lower()
    b = y.lower()
    if a[0].lower == b[0].lower:
        return True
    else:
        return False

print(my_func7('Python', 'Pearl'))
print(my_func7('Python', 'pearl'))
print(my_func7('Go', 'go'))
print(my_func7('python', 'go'))

def animal_crackers(text):
    text = text.lower()
    word_list = text.split()
    
    return word_list[0][0] == word_list[1][0]

print(animal_crackers('python pearl'))
print(animal_crackers('Go go'))
print(animal_crackers('python go'))

def my_func8(a, b):
    if 20 in (a, b):
        return True
    elif sum((a, b)) == 20:
        return True
    else:
        return False

print(my_func8(10, 10))
print(my_func8(20, 0))
print(my_func8(20,30))
print(my_func8(25,15))

def makes_twenty(a, b):
    return a+b == 20 or a == 20 or b ==20

print(my_func8(10, 10))
print(my_func8(20, 0))
print(my_func8(20,30))
print(my_func8(25,15))

def capitalizeLocation(name):
    a = name.capitalize()
    a = a[:3]
    b = name[3:]
    b= b.capitalize()
    return a+b
print(capitalizeLocation('vinayak'))

def old_string(name):
    if len(name):
        return name[0:3].capitalize() + name[3:].capitalize()
    else:
        return False

print(old_string('vinayak'))

def reverseWords(sentence):
    temp = ""
    list1 = sentence.split(" ", )
    for item in list1:
        temp += item[::-1]
        temp += " "
    return temp

print(reverseWords("I am a human"))
print(reverseWords("We are ready"))


def master_yoda(text):
    return ' '.join(text.split()[::-1])

print(master_yoda("I am a human"))
print(master_yoda("We are ready"))

def findCouple(user_list):
    temp = 0
    for i, v in enumerate(user_list):
        if i == 0:
            temp = v
            continue
        if temp == v:
            print(v, temp)
            return True
        else:
            temp = v
    
    return False

user_list = [1,2,4,2,3,3]
print(findCouple(user_list))
user_list = [1,2,4,2,3,9,3]
print(findCouple(user_list))

def has_33(user_list):
    for i in range(0, len(user_list)-1):
        if user_list[i:i+2] == [3,3]:
            return True
    return False

user_list = [1,2,4,2,3,3]
print(has_33(user_list))
user_list = [1,2,4,2,3,9,3]
print(has_33(user_list))

def paper_doll(str):
    temp = ""
    for v in str:
        temp += v * 3 # which is equivalent to temp += v + v + v
    return temp

print(paper_doll("hello"))

def black_jack(a, b, c):
    tup = (a,b,c)
    total = sum(tup)
    if total < 21:
        return total
    elif total > 21 and 11 in tup:
        return total - 10
    else:
        return 'BUST'
    
print(black_jack(5,6,7))
print(black_jack(9,9,9))
print(black_jack(9,9,11))

def spy_game(user_list):
    local_list = [0, 0, 7]
    result_list = []
    j = 0
    for i in user_list:
        if i == local_list[j]:
            result_list.append(i)
            if j == 2:
                break
            j = j + 1
            continue

    print(result_list, len(result_list))
    return result_list == local_list

print(spy_game([1,2,3,0,5,6,0,1,4,7]))
print(spy_game([1,2,3,0,5,6,0,1,4]))

def spy_game2(user_list):
    code = [0,0,7,'x']

    for v in user_list:
        if v == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game2([1,2,3,0,5,6,0,1,4,7]))
print(spy_game2([1,2,3,0,5,6,0,1,4]))

def numPrimes(num):
    prime_list = []
    
    for i in range(2, num+1):
        for j in range(2, i+1):
            if j == i and i%j == 0:
                prime_list.append(i)
            if i % j == 0:
                break

    return prime_list

prime_list = numPrimes(100)
print(prime_list)
print("Total prime numbers {}".format(len(prime_list)))

# ---------------------------------------------------- Map, Filter, lambda -----------------------------------------------------------

def square(num):
    return num * num

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

my_nums = list(map(square, my_nums))
print(my_nums)

def splicer(text):
    if len(text)%2 == 0:
        return 'EVEN'
    else:
        return text[0]

str_list = ["andy", 'eve', 'sally']
str_list = list(map(splicer, str_list))
print(str_list)

def even(num):
    return num%2 == 0

my_list = [1,2,3,4,5,6,7,8,9]

for n in filter(even, my_list):
    print(n)

my_list = list(filter(even, my_list))
print(my_list)

my_nums = [1,2,3,4,5]
for item in map(lambda num : num ** 2, my_nums):
    print(item)

my_nums = list(map(lambda num : num ** 2, my_nums))
print(my_nums)

my_list = [1,2,3,4,5,6,7,8,9]

my_list= list(filter(lambda num : num%2 == 0, my_list))
print(my_list)

str_list = ["andy", 'eve', 'sally']
str_list = list(map(lambda x:x[0], str_list))
print(str_list)

str_list = ["andy", 'eve', 'sally']
str_list = list(map(lambda x:x[::-1], str_list))
print(str_list)

def stringPalindrome(str):
    return str == str[::-1]

print(stringPalindrome("helllleh"))
num = 123321

def check_num_range(num, low, high):
    if num in range(low, high):
        return True
    else:
        return False

print(check_num_range(23, 20, 50))
print(check_num_range(10, 20, 50))

def count_upper(s):
    d = {"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    return d

print(count_upper("Hello Ladies AnD GenTleman"))

def unique_list(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique_list([1,1,2,3,1,2,3,4,5,6,3,4,5,6]))

def numPalindrome(n):
    temp = 0
    num = n
    while num > 0:
        rem = num % 10
        temp = temp * 10 + rem
        num = num // 10
    return temp == n

print(numPalindrome(1123321))

def multiply(list):
    product = 1
    for i in list:
        product *= i
    return product

print(multiply([1,2,3,4]))
'''
