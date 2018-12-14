#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

import sys

a=set()

for arg in sys.argv[1:]:
    a.add(arg)
b=''
for i in a:
    b+=(i+' ')
print(b)
