from physical.external import TrafficLight
from useful_functions import list_
import os
from datetime import datetime
from operator import itemgetter


class System:
        number_of_lights = 12
        frequently_operable_lights = 8
        max_waiting_time = 800
        cycle = 0
        time_to_hold = 0
        skip_less_than5 = False
        l = []
        for i in range(1, number_of_lights + 1):
                l.append('light' + str(i))
        l1 = TrafficLight(l[0])
        l2 = TrafficLight(l[1])
        l3 = TrafficLight(l[2])
        l4 = TrafficLight(l[3])
        l5 = TrafficLight(l[4])
        l6 = TrafficLight(l[5])
        l7 = TrafficLight(l[6])
        l8 = TrafficLight(l[7])
        l9 = TrafficLight(l[8])
        l10 = TrafficLight(l[9])
        l11 = TrafficLight(l[10])
        l12 = TrafficLight(l[11])
        lights = [
                l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12
        ]
        lanes = ['a', 'b1', 'b2' 'c', 'd', 'e', 'f1', 'f2', 'g', 'h', 'i', 'j1', 'j2', 'k', 'l', 'm', 'n1', 'n2', 'o',
                 'p']


class Operation:
        highest_number_index = 0
        lowest_number_index = 0
        highest_number = 0
        lowest_number = 0
        less_than_5_index = []
        less_than_5_numbers = []
        priority_index = 0
        total_vehicles = 0
        previously_green_lights = []
        numbers_ = []
        green_poles_index = []      # actually its name not index
        red_poles_index = []
        green_lights_duration = []
        red_lights_duration = []
        @staticmethod
        def reset():
                if len(Operation.previously_green_lights) == System.frequently_operable_lights:
                        Operation.previously_green_lights = []
                Operation.highest_number_index = 0
                Operation.lowest_number_index = 0
                Operation.highest_number = 0
                Operation.lowest_number = 0
                Operation.less_than_5_index = []
                Operation.less_than_5_numbers = []
                Operation.priority_index = 0
                Operation.total_vehicles = 0
                Operation.numbers_ = []
                System.skip_less_than5 = False
                System.time_to_hold = 0

        @staticmethod
        def calculation(numbers_=[]):
                h = numbers_[0]
                ll = numbers_[0]
                Operation.reset()
                Operation.numbers_ = numbers_
                Operation.total_vehicles = int(list_.sum_of_list(numbers_))
                print(f'Total vehicles: {Operation.total_vehicles}')
                index = 0
                for i in numbers_:
                        if index != 0 and index != 3 and index != 6 and index != 9:
                                if int(i) > int(h):
                                        h = i
                                        Operation.highest_number_index = index
                                if int(i) < int(ll):
                                        ll = i
                                        Operation.lowest_number_index = index
                                if 5 >= int(i) > 0:
                                        Operation.less_than_5_index.append(index)
                                        Operation.less_than_5_numbers.append(int(i))

                        index += 1
                Operation.highest_number = int(h)
                Operation.lowest_number = int(ll)

        @staticmethod
        def record_all():
                red = green = ''
                Operation.green_poles_index = []
                Operation.red_poles_index = []
                Operation.green_lights_duration = []
                for i in System.lights:
                        if i.red_light:
                                Operation.red_poles_index.append(i.name)
                                Operation.red_lights_duration.append(i.duration)
                                red += str(i.name) + '        Duration:' + str(i.duration) + ' second(s)' + '\n'
                        elif i.green_light:
                                Operation.green_poles_index.append(i.name)
                                Operation.green_lights_duration.append(i.duration)
                                green += str(i.name) + '        Duration:' + str(i.duration) + ' second(s)' + '\n'
                try:
                        os.makedirs('Data/UniversalData')
                except FileExistsError:
                        pass
                file = open('Data/UniversalData/' + str(datetime.date(datetime.now())) + '.txt', 'a')
                file.write(f'''
*
Cycle = {System.cycle}

Time: {datetime.time(datetime.now())} 
Total vehicles recorded:  {Operation.total_vehicles}
MAXIUMUM VEHICLES : {System.lights[Operation.highest_number_index].waiting_vehicles}  
MINIMUM VEHICLES  : {System.lights[Operation.lowest_number_index].waiting_vehicles} 
Priority given to: LIGHT{Operation.priority_index + 1}
Previously green lights on this cycle: {Operation.previously_green_lights}
Time to hold: 

Number of vehicles on:
        
        LIGHT 1 = {Operation.numbers_[0]}
        LIGHT 2 = {Operation.numbers_[1]}
        LIGHT 3 = {Operation.numbers_[2]}
        LIGHT 4 = {Operation.numbers_[3]}
        LIGHT 5 = {Operation.numbers_[4]}
        LIGHT 6 = {Operation.numbers_[5]}
        LIGHT 7 = {Operation.numbers_[6]}
        LIGHT 8 = {Operation.numbers_[7]}
        LIGHT 9 = {Operation.numbers_[8]}
        LIGHT 10= {Operation.numbers_[9]}
        LIGHT 11= {Operation.numbers_[10]}
        LIGHT 12= {Operation.numbers_[11]}


Green poles:
{green}


Red poles:
{red}
#
''')
                file.close()

        @staticmethod
        def determine_priority_index():
                if len(Operation.less_than_5_numbers) != 0 and not System.skip_less_than5:
                        count = 0
                        while 1:
                                priority = list_.random_return(Operation.less_than_5_index)
                                if str(priority) not in Operation.previously_green_lights:
                                        break
                                count += 1
                                if count > len(Operation.numbers_):
                                        System.skip_less_than5 = True
                                        break
                        if not System.skip_less_than5:
                                Operation.previously_green_lights.append(str(priority))
                                print(f'Priority: Light{priority + 1}')
                                Operation.priority_index = priority
                                return priority
                count = 0
                while 1:
                        vehicles = Operation.numbers_
                        temp = []
                        for i in range(len(vehicles)):
                                temp.append((int(vehicles[i]), i))
                        temp = sorted(temp, key=itemgetter(0, 1))
                        priority = temp[len(temp) - count - 1][1]
                        if str(priority) not in Operation.previously_green_lights:
                                break
                        else:
                                count += 1
                Operation.previously_green_lights.append(str(priority))
                print(f'Priority: Light{priority + 1}')
                Operation.priority_index = priority
                return priority
