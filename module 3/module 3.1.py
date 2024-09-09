#2023/10/06 00:00|Домашняя работа по уроку "Пространство имён"
calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    kortej = str(string)
    result = (len(kortej), kortej.upper(), kortej.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_ = list(list_to_search)
    count_calls()
    for i in range(len(list_)):
        if str(list_[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue

    return result


print(string_info('Kuznetsk'))
print(string_info('Sozvezdie'))
print(is_contains('Study', ['stella', 'StUdY', 'BANANAAAAAA']))
print(is_contains('Motocycle', ['Ban_vsem_za_moy_schet', 'Bike']))
print(calls)
