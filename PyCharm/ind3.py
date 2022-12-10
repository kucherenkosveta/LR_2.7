#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a = {'b', 'd', 'f', 'g', 'l', 'u'}
    b = {'d', 'e', 'f', 'm', 'n', 'z'}
    c = {'h', 'i', 'r', 'x', 'y'}
    d = {'a', 'e', 'f', 'k', 'r', 's', 'x'}
    u = set("abcdefghijklmnopqrstuvwxyz")
    n_a = u.difference(a)
    print('Множество A = ', a)
    print('Множество B = ', b)
    print('Множество C = ', c)
    print('Множество D = ', d)

    x = (a.difference(b)).intersection(c.union(d))
    print('Множество X = ', x)

    y = (n_a.intersection(d)).union(c.difference(b))
    print('Множество Y = ', y)
