#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys
import csv

class Args(object):
    def __init__(self):
        self.args=sys.argv[1:]
        self.configfile=''
        self.sourcefile=''
        self.targetfile=''
        try:
            index=self.args.index('-c')
            self.configfile=self.args[index+1]
            index=self.args.index('-d')
            self.sourcefile=self.args[index+1]
            index=self.args.index('-o')
            self.targetfile=self.args[index+1]
        except:
            print('1 ERROR')
       # print(self.configfile,self.sourcefile,self.targetfile)


class Config(object):
    def __init__(self,source):
        self.config=self._read_config(source)
       # print(self.config)

    def _read_config(self,source):
        config={}
        with open(source) as file:
            string=file.readlines()
            for x in string:
                two=x.split('=')
                config[two[0].strip()]=float(two[1].strip())
        return config



class UserData(object):
    def __init__(self,source):
        self.config=self._read_config(source)
       # print(self.config)

    def _read_config(self,source):
        config={}
        with open(source) as f:
             data=list(csv.reader(f))
        try:
            for i in data:
                config[i[0]]=int(i[1])
        except:
            print('2 ERROR')
        return config

class IncomeTaxCalculator(object):
    def calc_for_all_userdata(self,config,source):
        result=[]
        low=config['JiShuL']
        high=config['JiShuH']
        tax=0.0
        for key,value in config.items():
            if key != 'JiShuL' and key != 'JiShuH':
                tax+=value
      #  print(low,high,tax)
        for key,value in source.items():
            if value<low:
                num_tax=low*tax
            elif value>high:
                num_tax=high*tax
            else:
                num_tax=value*tax
            temp=value-num_tax
            if temp<=3500:
                num_fee=0.00
            else:
                num_fee=count_money(value-num_tax-3500)
            num_total=value-num_tax-num_fee
            result.append(list((int(key),value,format(num_tax,"0.2f"),format(num_fee,"0.2f"),format(num_total,"0.2f")))) 
        print(result)
        return result


    def export(self,config,source,default='csv'):
        result=self.calc_for_all_userdata(config,source)
        print(result)
        with open(default,'w') as f:
            writer=csv.writer(f)
            writer.writerows(result)
    

def count_money(money):
    if money>=0 and money <=1500:
        get=(money*0.03-0)
    elif money>1500 and money <=4500:
        get=(money*0.1-105)
    elif money>4500 and money <=9000:
        get=(money*0.2-555)
    elif money>9000 and money <=35000:
        get=(money*0.25-1005)
    elif money>35000 and money<=55000:
        get=(money*0.3-2755)
    elif money>55000 and money<=80000:
        get=(money*0.35-5505)
    else: 
        get=(money*0.45-13505)     
    return get

if __name__ == '__main__':
    ar=Args()
    con=Config(ar.configfile)
    user=UserData(ar.sourcefile)
    asd=IncomeTaxCalculator()    
    asd.calc_for_all_userdata(con.config,user.config)
    asd.export(con.config,user.config,ar.targetfile)
















    
