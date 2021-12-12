#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = list(map(float, input('Введите элементы массива: ').split()))

    s = 0
    sum = 0
    e = 0
    for item in a:
        if item == 0:
            s += 1

    print(f"Количество элементов равных нулю: {s}")

    a_min = 1000.0
    for i, item in enumerate(a):
        if item < a_min:
            a_min = item
            e = i

    for i, item in enumerate(a):
        if i > e:
            sum += item

    print(f"Сумма равна {sum}")
















