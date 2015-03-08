__author__ = 'AntonF'
import time

print('This Program Will Calculate The RC Time Constant.')
resistance = input('Ange Värdet För Resistansen: ')
capacitance = input('Ange Värdet För Kapacitansen: ')
sumOfRC = float(resistance) * float(capacitance)
print('Tau = {0}'.format(float(sumOfRC)))
print('Efter {0} Sek Uppnår Du Slutvärdet'.format(float(sumOfRC * 5)))
