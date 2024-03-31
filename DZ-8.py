
import json

print ('1 - Поиск телефона\n2 - Просмотр телефонного справочника\n3 - Добавить новый контакт\n4 - Изменить существующий контакт\n5 - Удалить контакт')

operation = int(input('Введите код операции - '))

base = 'phonebook.json'

def add_contact(contact, a, b, c, d):
    contact[a] = {'phones': [b], 'email': c, 'birthday': d}
    return contact

def load_from_file (file):
    with open(file) as f:
        file = json.load(f)
    return file

def load_to_file (contact, base):
    with open(base, 'w') as file:
        json.dump(contact, file)

def serch_name(name, file):
    fil = load_from_file(file)
    count = 0
    for i in fil:
        if i == name:
            count += 1
    if count > 0:
        print(fil[name])
    else:
        print('Контакт отсутствует')

def rename (name, file):
    fil = load_from_file(file)
    count = 0
    for i in fil:
        if i == name:
            count += 1
    if count > 0:
        b = input('Введите новый номер телефона - ')
        c = input('Введите новый email - ')
        d = input('Введите дату рождения - ')
        add_contact (fil, name, b, c, d)
        load_to_file (fil, base)
    else:
        print('Контакт отсутствует')

def name_del (name, file):
    fil = load_from_file(file)
    count = 0
    for i in fil:
        if i == name:
            count += 1
    if count > 0:
        fil.pop (name)
        load_to_file (fil, base)
    else:
        print('Контакт отсутствует')

if operation == 1:
        name = (input('Введите имя - '))
        serch_name(name, base)

if operation == 2:
    phonebook = load_from_file(base)
    for i in phonebook:
        print(f'{i} {phonebook.get(i)}')

if operation == 3:
    a = input('Введите название контакта - ')
    b = input('Введите номер телефона - ')
    c = input('Введите email - ')
    d = input('Введите дату рождения - ')
    contact = load_from_file(base)
    add_contact (contact, a, b, c, d)
    load_to_file (contact, base)

if operation == 4:
    name = (input('Введите имя - '))
    rename(name, base)

if operation == 5:
    name = (input('Введите имя - '))
    name_del (name, base)  

load_to_file(load_from_file(base), 'reserv.json')