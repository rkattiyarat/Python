def first():
    secret_number = 28
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess == secret_number:
            print("You won!")
            break
    else:
        print("Sorry, you failed!")

def second():
    command = ""
    started = False
    stopped = False
    while True:
       command =  input("> ").lower()
       if command == "start":
           if started:
               print("Car already started!!")
           else:
               started =True
               print("Car started!")
       elif command == "stop":
           if not started:
                print("Car is already stopped!!")
           else:
                started = False
                print("Car stopped!")
       elif command == "help":
            print("""
start - to start the car
stop - to stop the car
quit - to quit
            """)
       elif command == "quit":
            break
       else:
            print("Sorry, I don't understand")



def third():
    for item in ["Mosh", "John", "Sarah"]:
        print(item)

def fourth():
    prices = [10, 20, 30]

    total = 0
    for price in prices:
        total = total + price
    print(f"Total: {total}")

def fifth():
    for x in range(4):
        for y in range(3):
            print(f'({x}, {y})')
    numbers = [5, 2, 5, 2, 2]
    for x_count in numbers:
        print("x" * x_count)

    numbers = [6, 3, 6, 6, 1]
    for x_count in numbers:
        output = ""
        for count in range(x_count):
            output += "x"
        print(output)
def six():
    numbers = [3, 6, 2, 8, 4, 10]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    print(max)

def seven():
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
    matrix[1][1] = 10
    print(matrix[1][1])
    for row in matrix:
        for item in row:
            print(item)
def eight():
    numbers = [5, 2, 1, 7, 4]
    numbers.append(20)
    numbers.insert(0, 15)
    numbers.remove(2)
    print(numbers.index(7))
    numbers.sort()
    numbers.reverse()
    numbers2 = numbers.copy
    numbers.append(15)
    print(numbers2)
    print(numbers)
def nine():
    numbers = [2, 2, 4, 6, 3, 4, 6, 1]
    uniques = []
    for number in numbers:
        if number not in uniques:
            uniques.append(number)
    print(uniques)

def ten():
    numbers = (1, 2, 3)
    print( numbers[0])

def eleven():
    coordinates = (1, 2, 3)
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]
    x, y, z = coordinates
    print(x)

def twelve():
    customer = {
            "name": "John Smith",
            "age": 30,
            "is_verified": True

            }
    customer["name"] = "Rose"
    customer["birthdate"] = " Jan 1 1980"
    print(customer["birthdate"])
    
def thirteen():
    phone = input("Phone: ")
    digits_mapping = {
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6":"six",
            "7":"seven",
            "8":"eight",
            "9":"nine"
        }
    output = ""
    for ch in phone:
        output += digits_mapping.get(ch, "!") + " "
    print(output)

def fourteen():
    message = input(">")
    words = message.split(' ')
    emojis = {
            ":)": " ",
            ":(": " "
            }
    output = ""
    for word in words:
        output += emojis(words).get(word, word) + " "
    print(output)

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome")


print("Start")
greet_user("John", last_name="Smith")
print("Finish")

def square(number):
    return number * number


print(square(3))

def fifteen():
    try:
        age = int(input("Age: "))
        income = 2000
        risk = income / age
        print(age)
    except ZeroDivisionError:
        print("Age cannot be 0.")
    except ValueError:
        print("Invalid value")

def sixteen():
    #this is an example
    print("Sky is blue")

def seventeen():
    class Point:
        def move(self):
            print("move")
        def draw(self):
            print("draw")
    point1 = Point()
    point1.x = 10
    point1.y = 20
    print(point1.x)
    point1.draw()

    point2 = Point()
    point2.x = 1
    print(point2.x)

def eighteen():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    point = Point(10, 20)
    point.x = 15
    print(point.x)

def nineteen():
    class Person:
        def __init__(self, name):
            self.name = name
        def talk(self):
            print(f"Hi, I am {self.name}")
    john = Person("John Smith")
    john.talk()
    bob = Person("Bob Smith")
    bob.talk()

def twenty():
    class Mammal:
        def walk(self):
            print("walk")

    class Dog(Mammal):
        pass


    class Cat(Mammal):
        pass

    dog1 = Dog()
    dog1.walk()



def lbs_tokg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / 0.45

from utils import find_max

numbers = [10, 3, 6, 2]
max = find_max(numbers)

print(max)

from ecommerce.shipping import calc_shipping


calc_shipping()

import random

for i in range(3):
    print(random.randint(10, 20))

def twentyone():
    import random

    class Dice:
        def roll(self):
           first = random.randint(1, 6)
           second = random.randint(1, 6)
           return first, second

    dice = Dice()
    print(dice.roll())

def twentytwo():
    from pathlib import Path

    path = Path()
    for file in path.glob("*"):
        print(file)


