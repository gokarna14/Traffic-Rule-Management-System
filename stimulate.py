from physical.objects import System, Operation


def set_duration(index):
    tv = int(Operation.total_vehicles)
    wv = int(System.lights[index].waiting_vehicles)
    for i in range(12):

        if i != 0 and i != 3 and i != 6 and i != 9:
            if wv > 5:
                System.lights[i].duration = int((wv/tv)*System.max_waiting_time)
            else:
                System.lights[i].duration = int(wv*5)


def red_others(i):
    b = c = d = e = 0
    if i == 2:
        b = 11
        c = 12
        d = 5
        e = d
    elif i == 3:
        b = 5
        c = 6
        d = 12
        e = d
    elif i == 5:
        b = 8
        c = 2
        d = 3
        e = d
    elif i == 6:
        b = 3
        c = 11
        d = 8
        e = 9
    elif i == 8:
        b = 3
        c = 6
        d = 11
        e = 5
    elif i == 9:
        b = 2
        c = 6
        d = 11
        e = 12
    elif i == 11:
        b = 2
        c = 6
        d = 8
        e = 9
    elif i == 12:
        b = 3
        c = 2
        d = 5
        e = d
    System.lights[b-1].red()
    System.lights[c-1].red()
    System.lights[d-1].red()
    System.lights[e-1].red()


def green_other(i):
    g = {
        '2' : '8',
        '3' : '9',
        '5' : '11',
        '6' : '12',
        '8' : '2',
        '9' : '3',
        '11' : '5',
        '12' : '6'
    }
    System.lights[int(g.get(str(i), str(i))) - 1].green()
    System.lights[0].green()
    System.lights[3].green()
    System.lights[6].green()
    System.lights[9].green()


def delay():
    print(f'DELAY {System.time_to_hold} second(s)')


def process(numbers_=[]):
    if len(numbers_) == 12:
        for i in range(12):
            System.lights[i].waiting_vehicles = numbers_[i]
    else:
        print("ERROR INPUT")
        exit()
    Operation.calculation(numbers_)
    priority_index = Operation.determine_priority_index()
    System.lights[priority_index].green()
    set_duration(priority_index)
    red_others(priority_index + 1)
    green_other(priority_index + 1)
    Operation.record_all()
    System.time_to_hold = System.lights[Operation.priority_index].duration
    for i in System.lights:                 # most important line
        i.show_status()

    delay()
