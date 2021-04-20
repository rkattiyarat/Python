
def first():
    age = 20
    status = "new"
    first_name = "John Smith"
    print (first_name)
    print (age)
    print (status)




def second():
    name = input("what is your name? ")
    print ("Hello " + name)

def third():
    birth_year = input("Enter your birth year: ")
    age = 2021 - int(birth_year)
    print(age)

def fourth():
    age = input("Enter your age:")
    birth_year = (2021 - int (age))
    print (birth_year)

def fifth():
    a= 10.1
    b = 20
    print("First ",a)
    print("Second ",b)
    print("sum:",a+b)

def six():
    first = input("First: ")
    second = input("Second: ")
    sum = int(first) + int(second)
    print(sum)

def seven():
    first = input("First: ")
    second = input("Second: ")
    sum = float(first) + float(second)
    print(sum)

def eight():
    first = input("First: ")
    second = input("second: ")
    sum = float(first) + float(second)
    print("sum: " + str(sum))

def nine():
    name = "Rungnapa Kattiyarat"
    print(name.upper())
    print(name.lower())
    print(name)
    print(name.find("a"))
    print(name.replace("Rungnapa", "Rose"))
    print("Kattiyarat" in name)

def ten():
   print(10+5)
   print(50//4)

def eleven():
    price = 15
    print(price > 20 or price < 30)
    print(price > 10 and price < 30)
    print(not price > 20)

def twelve():
    temperature = 5
    if temperature > 30:
        print("It's a hot day")
        print("Drink plenty of water")
    elif temperature > 20:# (20, 30]
        print("It's a nice day")
    elif temperature > 10: # (10, 20]
        print("It's a bit cold")
    else:
        print("It's cold")

def thirteen():
    weight = int(input("weight: "))
    unit = input("(K)g or (L)bs: ")
    if unit.upper() == "K":
        converted = weight /0.45
        print("weight in Lbs: " + str(converted))
    else:
        converted = weight * 0.45
        print("weight in Kgs: " + str(converted))

def fourteen():
    i = 1
    while i <= 5:
         print(i)
         i = i + 1
    i = 1
    while i <= 10:
        print(i * "*")
        i = i + 1
    i = 1
    while i <= 1_000:
        print(i)
        i = i + 1

def fifteen():
    names = ["Rose", "Stephen", "kate", "Sarah", "Sam"]
    names[1] = "Steven"
    print(names[1:4])
    print(names)

    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    numbers.insert(0, -1)
    numbers.remove(2)
    numbers.clear()
    print(3 in numbers)
    print(15 in numbers)
    print(numbers)
    print(len(numbers))

def sixteen():
    numbers = [1, 2, 3, 4, 5]
    for item in numbers:
        print(item)
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i = i + 1

def seventeen():
   numbers = range(5, 10, 2)
   for number in range(5):
       print(number)
   for number in numbers:
       print(number)








