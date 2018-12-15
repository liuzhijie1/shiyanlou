#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

import sys

salary={}

def print_money(dicts):
    for key,value in dicts.items():
        print("%s:%.2f"%(key,value))

def count_money(money):
    if money>=0 and money <=1500:
        get=(money*0.03-0)
    elif money>1500 and money <=4500:
        get=(money*0.1-105)
    elif money>4500 and money <=9000:
        get=(money*0.2-555)
    elif money>9000 and money <=35000:
        get=(money*0.25-1005)
    elif money>3500 and money<=55000:
        get=(money*0.3-2755)
    elif money>55000 and money<=80000:
        get=(money*0.35-5505)
    else:
        get=(money*0.45-13505)
    return get

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        list1=arg.split(':')
        try:
            salary[list1[0]]=int(list1[1])
        except:
            print("Parameter Error")

    for key,value in salary.items():
        value=value-(value*0.165)
        if value<=3500:
            salary[key]=value
        else:
            temp=count_money(value-3500)
            salary[key]=value-temp
    print_money(salary)
