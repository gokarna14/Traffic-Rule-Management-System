from datetime import datetime
import os
"""
SHOW STATUS IS MOST IMPORTANT
"""


class TrafficLight:
    def __init__(self, name, waiting_vehicles = 0):
        self.red_light = True
        self.yellow_light = False
        self.green_light = False
        self.rlt = 0
        self.ylt = 0
        self.glt = 0
        self.name = name
        self.four_wheelers = 0
        self.two_wheelers = 0
        self.waiting_vehicles = int(waiting_vehicles)
        self.duration = 500
        try:
            os.makedirs('Data/' + str(name))
        except FileExistsError:
            pass
        self.file = open('Data/' + str(name) + '/' + str(datetime.date(datetime.now())) + '.txt', 'a')
        self.on_light = 'RED'

    def reset(self):
        self.red_light = True
        self.yellow_light = False
        self.green_light = False
        self.rlt = 0
        self.ylt = 0
        self.glt = 0
        self.four_wheelers = 0
        self.two_wheelers = 0

    def red(self):
        self.reset()
        self.red_light = True
        self.yellow_light = False
        self.green_light = False
        self.on_light = 'RED'

    def yellow(self):
        self.reset()
        self.red_light = False
        self.yellow_light = True
        self.green_light = False
        self.on_light = 'YELLOW'

    def green(self):
        self.reset()
        self.red_light = False
        self.yellow_light = False
        self.green_light = True
        self.on_light = 'GREEN'

    def all_on(self):
        self.reset()
        self.red_light = True
        self.yellow_light = True
        self.green_light = True
        self.on_light = 'ALL'

    def record(self):
        self.file = open('Data/' + str(self.name) + '/' + str(datetime.date(datetime.now())) + '.txt', 'a')
        self.file.write(f'''*
Time: {datetime.time(datetime.now())}        
Light on:                               {self.on_light}
Waiting vehicles =                      {self.waiting_vehicles}
Number of two wheelers passed:          {self.two_wheelers} 
Number of four wheelers passed:         {self.four_wheelers}   
Duration of operation:                  {self.duration} second(s)
#
''')
        self.file.close()

    def erase_data(self):
        password = input('ENTER PASSWORD: ')
        while 1:
            if password.lower() == 'prabas':
                self.file = open('Data/' + str(self.name) + '/' + str(datetime.date(datetime.now())) + '.txt', 'w')
                self.file.write('')
                print('ERASED')
                break
            elif password.lower() == 'exit':
                break
            else:
                print('Wrong password !! TYPE "exit" and press enter OR enter the valid password')
                password = input()

    def show_status(self):
        self.record()
        print(f'''
{self.name}
Vehicles: {self.waiting_vehicles}   Duration: {self.duration}   Light: {self.on_light}  ''')


