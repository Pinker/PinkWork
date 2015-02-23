__author__ = 'AntonF'


def test():
    try:
        int(number) + 1
        2 / int(number)
    except ZeroDivisionError:
        print("Can't divide with 0.")
        exit()
    except ValueError:
        print("An error has occurred check for non numerical inputs.")
        exit()

print("This will calculate the sum all the integers from 1 to X.")
number = input("Enter an integer: ")

#Try for invalid characters
test()

#Calc Value
totalValue = (int(number)*(int(number)+1))/2

#Print results
print("The total value is: {0}".format(totalValue))
