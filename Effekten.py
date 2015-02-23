__author__ = 'AntonF'

"""
Poop ask for poop resistance
poop ask for poop voltage
poop calculate poop effect
poop print poop result
"""


def test():
    try:
        (float(vol) ** 2) / float(res)
    except ZeroDivisionError:
        print("Can't divide with 0.")
        exit()
    except ValueError:
        print("An error has occurred check for non numerical inputs.")
        exit()

#Get Input Values
res = input("Input resistance: ")
vol = input("Input voltage: ")

print("Resistance = {0}, Voltage = {1}".format(res, vol))

test()

#Calc Power
power = (float(vol) ** 2) / float(res)

#Print Results
print("Effect = {0} W".format(power))