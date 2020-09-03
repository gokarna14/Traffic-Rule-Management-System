# poles and lights are equivalent
from datetime import datetime
from physical.objects import System, Operation
from useful_functions import list_
import stimulate
import os


def check_input_data(list__=[]):
    for i in list__:
        if int(i) < 0:
            return False
    return True


try:
    try:
        file = open('Data/UniversalData/Cycle' + str(datetime.date(datetime.now())) + '.txt', 'r')
    except FileExistsError:
        pass
    cycle = int(file.read())
    file.close()
except FileNotFoundError:
    cycle = 1
while 1:
    System.cycle = cycle
    inupt_number_of_vehicles = input('ENTER VEHICLES separating by comma (12 numbers): ')
    v = inupt_number_of_vehicles
    vl = v.split(',')
    vl = list_.remove_empty_member(vl)
    vl = list_.remove_alphabet(vl)
    if check_input_data(vl):
        stimulate.process(vl)
    else:
        print('ERROR INPUT')
        break
    cycle += 1
    file = open('Data/UniversalData/Cycle' + str(datetime.date(datetime.now())) + '.txt', 'w')
    file.write(str(cycle))
    file.close()

