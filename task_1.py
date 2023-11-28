#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cоздайте словарь, связав его с переменной school, и наполните данными, 
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.). 
# Внесите изменения в словарь согласно следующему: 
#     а) в одном из классов изменилось количество учащихся, 
#     б) в школе появился новый класс, 
#     с) в школе был расформирован (удален) другой класс. 
#     Вычислите общее количество учащихся в школе.

if __name__=="__main__":
    classes = {}

    while True:
        command = input("$ ").lower()

        match command:
            case 'exit':
                break

            case 'add' | 'modified':
                name = input("Введите название класса: ").upper()
                count_stud = int(input("Введите колличество учащихся в классе: "))
                classes[name] = count_stud

            case 'del':
                name = input("Введите класс, который хотите удалить: ").upper()
                del classes[name]

            case 'list':
                line = '+-{}-+-{}-+-{}-+'.format('-' * 4, '-' * 10, '-' * 12)
                print(line)
                print('| {:^4} | {:^10} | {:^12} |'.format("№", "Название", "Количество"))
                print(line)

                a = 1
                for name, count_stud in classes.items():
                    print('| {:^4} | {:^10} | {:^12} |'.format(a, name, count_stud))
                    a += 1
                    print(line)
