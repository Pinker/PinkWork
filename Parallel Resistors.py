__author__ = 'AntonF'

print("This will calculate parallel resistors.")
numberOfResistors = input("How many resistors do you have?: ")


def test1():
    try:
        float(resValue) + 1
        1 / float(resValue)
    except ZeroDivisionError:
        print("Can't divide with 0.")
        exit()
    except ValueError:
        print("An error has occurred check for non numerical inputs.")
        exit()


def test():
    try:
        int(numberOfResistors) + 1
        2 / int(numberOfResistors)
    except ZeroDivisionError:
        print("Can't divide with 0.")
        exit()
    except ValueError:
        print("An error has occurred check for non numerical inputs.")
        exit()

test()

rTOT = 0
i = 0
while i < int(numberOfResistors):
    i += 1
    resValue = input("What is the value of the value of nr " + str(i) + " resistor?: ")
    test1()
    newResValue = 1 / float(resValue)
    rTOT += float(newResValue)
print("Your total value of resistance is: {0}".format(1/rTOT))
