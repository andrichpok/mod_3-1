calls = 0
def count_calls(call):
    global calls
    calls += call
    return calls

def string_info(string):
    list_1 = []
    list_1.append(len(string))
    list_1.append(string.upper())
    list_1.append(string.lower())
    count_calls(1)
    return list_1

def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = list_to_search.lower()
    count_calls(1)
    return string in list_to_search
    


a = string_info(str(input('Введите слово: ')))
b = is_contains(str(input('Введите слово для его поиска в списке: ')), str(input('Введите список: ')))
print(a)
print(b)
print(calls)