#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

import sys
dict={}
for arg in sys.argv[1:]:
    list1=arg.split(':')
    dict[list1[0]]=list1[1]
for key,value in dict.items():
    print("ID:",key," ","Name:",value)
