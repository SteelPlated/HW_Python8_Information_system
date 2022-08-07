'''
Создать информационную систему позволяющую работать с сотрудниками
некой компании \ студентами вуза \ учениками школы
'''
from tkinter import END


database = {}
db = {'parents': 1, 'children': 2, 'klass':3, 'teachers':4 }


def reading_file_to_dict(number_file):
    with open(f'{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        # print(data)
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))


def print_children(second_name):
    id = [i[0] for i in database[db['parents']] if second_name in i[2]][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:5]) + '\n' for i in deti])
def print_children_klass(klass):
    id = [i[0] for i in database[db['children']] if klass in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])
def print_theacher_klass(klass):
    id = [i[1] for i in database[db['klass']] if klass in i][0]
    teachers = [i for i in database[db['teachers']] if id == i[0]]
    print(*[' '.join(i[1:4]) + '\n' for i in teachers])

def save():
    with open(f'1.txt', 'w', encoding='utf-8') as file:
       for i in database[db['parents']]:
           file.writelines(f'{i[0]};{i[1]};{i[2]}\n')
           
    with open(f'2.txt', 'w', encoding='utf-8') as file_2:
       for i in database[db['children']]:
           file_2.writelines(f'{i[0]};{i[1]};{i[2]};{i[3]};{i[4]};{i[5]}\n')
                      
    with open(f'3.txt', 'w', encoding='utf-8') as file_3:
       for i in database[db['klass']]:
           file_3.writelines(f'{i[0]};{i[1]}\n')
           
    with open(f'4.txt', 'w', encoding='utf-8') as file_4:
       for i in database[db['teachers']]:
           file_4.writelines(f'{i[0]};{i[1]};{i[2]}\n')
           
def create_menu():
    print('----------------------------------------------------- \n'
          '|    1. Вывести данные                               | \n'
          '|    2. Добавить запись                              | \n'
          '|    3. Сохранить данные и завершить работу          | \n'          
           '-----------------------------------------------------')
reading_file_to_dict(1)
reading_file_to_dict(2)
reading_file_to_dict(3)
reading_file_to_dict(4)
while True:
    create_menu()
    command = int(input('Введите номер команды: '))
    if command == 1:
        number_file=int(input('Что выводим? \n 1:Родители \n 2:Дети \n 3:Классы\n 4:Учителя\n 5:Дети по фамилии \n 6:Дети по классу\n 7:Учителя по классу\n'))
        if number_file==1:
            print(database[1])
        elif number_file==2:
            print(database[2])
        elif number_file==3:
            print(database[3])
        elif number_file==4:
            print(database[4])
        elif number_file==5:
            surname=input('Фамилия: ')
            print_children(surname)
        elif number_file==6:
            klass=input('Класс: ')
            print_children_klass(klass)
        elif number_file==7:
            klass=input('Класс: ')
            print_theacher_klass(klass)      
        #Доделать      
    elif command == 2:
        number_file=int(input('В какую таблиццу вводим данные? \n 1:Родители \n 2:Дети \n 3:Классы\n 4:Учителя\n'))
        if number_file==1:
            id=len(database[db['parents']])
            surname=input('Фамилия: ')
            name=input('Имя: ')
            str_data=str(id)+';'+name+';'+surname
            database[number_file].append(str_data.split(';'))
        elif number_file==2:
            id=len(database[db['children']])
            par_id=input('введите id родителя: ')
            name=input('Имя: ')
            surname=input('Фамилия: ')
            bd=input('введите день рождения: ')
            klass_id=input('введите номер класса: ')
            str_data=str(id)+';'+par_id+';'+name+';'+surname+';'+bd+';'+klass_id
            database[number_file].append(str_data.split(';'))
        elif number_file==3:
            teacher_id=input('введите id учителя: ')
            klass_id=input('введите номер класса: ')
            str_data=klass_id+';'+teacher_id
            database[number_file].append(str_data.split(';'))
        elif number_file==4:
            id=len(database[db['teachers']])
            surname=input('Фамилия: ')
            disciplin=input('введите предмет: ')
            str_data=str(id)+';'+surname+';'+disciplin
            database[number_file].append(str_data.split(';'))
    elif command == 3:
        save()
        break


