#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

k = 0
if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    s = 0
    for item in A:
        if abs(item) < 3:
            k += 1
            s += item

    print(k)
    print(s)