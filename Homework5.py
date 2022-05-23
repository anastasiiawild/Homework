def function_homework1():
    print("Hello, World!")
    str = 'Hello, Python!'
    print(str)
    print(str.lower())
    print(str.upper())
    print(str.title())

function_homework1()

def function_homework2():
    Name = input("What is your name?")
    Goal = input("What is your goal?")
    Time = input("When will you start working in a QA position?")
    print(f"Hi user. Your name is {Name}. Your goal is {Goal}. "
      f"You will start working in a QA position {Time}.")


function_homework2()

def function_homework3():
    a = input("a:")
    b = input("b:")
    c = input("c:")
    if a > b:
        print("so sad message")
    elif b > a:
        if b > c:
            print("absolutely happy message")
        else:
            print("not so sad message")
    elif a == b:
            print("something about equality")


function_homework3()

def function_homework4():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = str(a)

    while a < b:
        print("sad message")
        a += c
        d = d + " " + str(a)
        continue

    else:
        print("unbelievable")
        print("history of increments", d)


function_homework4()



