#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cоздайте словарь, где ключами являются числа, а значениями – строки. Примените к нему метод items(),
# c помощью полученного объекта dict_items создайте новый словарь, "обратный" исходному,
# т. е. ключами являются строки, а значениями – числа.

numbers_v1 = {1:"one", 2:"two", 3:"three"}
numbers_v2 = {}

for a, b in numbers_v1.items():
    numbers_v2[b] = a

print(numbers_v1)
print(numbers_v2)


