import random
from . import strings

def sum_of_list(input_list):
    try:
        sum = 0
        for data in input_list:
            sum += int(data)
        return sum
    except ValueError:
        print('...invalid...')


def remove_alphabet(input_listX):
    input_list = input_listX
    element_index = 0
    replace = ''
    for element in input_list:
        replace = ''
        for sub_element in element:
            if sub_element.isdigit():
                replace += sub_element
        input_list[element_index] = replace
        element_index += 1
    return input_list


def remove_number(input_listX):
    input_list = input_listX[:]
    element_index = 0
    for element in input_list:
        replace = ''
        for sub_element in element:
            if sub_element.isalpha():
                replace += sub_element
        input_list[element_index] = replace
        element_index += 1
    return input_list


def detect_something_from_list(input_list, character_to_detect):
    return_list = []
    for element in input_list:
        if character_to_detect.upper() in element or character_to_detect.lower() in element:
            return_list.append(element)
    return return_list


def frequency_of_elements(l, element):
    freq = 0
    for ele in l:
        if ele == element:
            freq += 1
    return freq


def random_return(l):
    w = random.randint(0, len(l) - 1)
    if l[w] != '':
        return l[w]
    else:
        return l[w-1]


def last_filter(l = []):
    return_ = []
    for i in l:
        p = i.lower()
        p = strings.return_alphabet(p)
        return_.append(p)
    return return_


def remove_empty_member(l = []):
    for element in l:
        if element == '':
            l.remove(element)
    return l


def string_present_bool(string='', list_=[]):
    for element in list_:
        if strings.return_alphabet(string) == element:
            return True


def sorted_(list_ = []):
    l = list_
    l.sort()
    return l

def remove_duplicate(list_ = []):
    l = []
    for i in list_:
        if i not in l:
            l.append(i)
    return l