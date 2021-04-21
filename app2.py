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
fourth()

