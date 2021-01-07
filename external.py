name = "Glen"
surname = "Chiridza"
age = 9
isActive = False
amount = 9.00

print("my name is {} {} age is {} {}".format(name, surname, age, isActive))

def looping():
    for i in range(0,11):
        isActive = True
        print(i)
        isActive = False

    while(isActive):
        print("well we are in the while statement now")

def credentails():
    print("{} {} {}".format(name, surname, age))


def print_values():
    print("my credentials")
    credentails()


if __name__ == '__main__':
    # print_values()
    looping()
