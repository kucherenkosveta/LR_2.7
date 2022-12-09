#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    b = input('b = ')
    d = input('d = ')
    f = input('f = ')
    g = input('g = ')
    l = input('l = ')
    u = input('u = ')
    e = input('e = ')
    m = input('m = ')
    n = input('n = ')
    z = input('z = ')
    h = input('h = ')
    i = input('i = ')
    r = input('r = ')
    x = input('x = ')
    y = input('y = ')
    a = input('a = ')
    k = input('k = ')
    s = input('s = ')

    mn_a = {b, d, f, g, l, u}
    mn_b = {d, e, f, m, n, z}
    mn_c = {h, i, r, x, y}
    mn_d = {a, e, f, k, r, s, x}
    mn_u = set("abcdefghijklmnopqrstuvwxyz")
    a = mn_u.difference(mn_a)
    print('Множество A = ', mn_a)
    print('Множество B = ', mn_b)
    print('Множество C = ', mn_c)
    print('Множество D = ', mn_d)

    mn_x = (mn_a.difference(mn_b)).intersection(mn_b.union(mn_d))
    print('\nМножество X = ', mn_x)

    mn_y =(a.intersection(mn_d)).union(mn_c.difference(mn_b))
    print('Множество Y = ', mn_y)