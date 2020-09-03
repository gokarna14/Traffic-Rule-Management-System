def emoji(list_ = []):
    emo = {
    ':)' : '🙂',
    ':(' : '☹',
    ':D' : '😁'
    }
    return_list = []
    for element in list_:
        return_list.append(emo.get(element,element))
    return return_list