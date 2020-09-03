def a_to_z_present(string):
    for character in string:
        if character.isalpha():
            return True
    return False


def digit_present(string):
    for character in string:
        if character.isdigit():
            return True
    return False


def special_character_present(string):
    character_set = '!@#$%^&*()+_=-'
    for character in string:
        if character in character_set:
            return True
    return False


def all_present(string):
    if a_to_z_present(string) and digit_present(string) and special_character_present(string):
        return True
    else:
        return False


def return_alphabet(string):
    return_value = ''
    for character in string:
        if character.isalpha():
            return_value += character
    return return_value


def return_digit(string):
    return_value = ''
    for character in string:
        if character.isdigit():
            return_value += character
    return return_value

def special_character_present(string):
    character_set = '!@#$%^&*()+_=-'
    for character in string:
        if character in character_set:
            return True
    return False


def all_present(string):
    if a_to_z_present(string) and digit_present(string) and special_character_present(string):
        return True
    else:
        return False



def string_in_string(to_detect_string, main_string_list):
    for i in main_string_list:
        if i != '':
            if i in to_detect_string:
                if to_detect_string == 'they':
                    return False
                return True
    else:
        return False


def change_pronoun(pronoun = ''):
    pronoun = pronoun.lower()
    d = {
        'he' : 'him',
        'she' : 'her',
        'i' : 'my',
        'they' : 'them'
    }
    return d.get(pronoun,pronoun)