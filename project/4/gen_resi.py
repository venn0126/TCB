#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 20200421
# @Author  : Augus

import random
import json
import pandas as pd
import os
import string

def addsepline():
    print("-----------------------------------------------------------------------------------------------")

def addseptag():
    print("##################################################################")


def setupCountry():
    oxylab = pd.read_csv('oxylab.csv')
    oxylab = list(oxylab['Country'].values)
    oxylabCountryList = list(set(oxylab))
    oxylabCountryList.pop(0)

    geosurf = pd.read_csv('geosurf.csv')
    geosurf = list(geosurf['ctr'].values)
    geosurfCountryList = list(set(geosurf))
    geosurfCountryList.pop(0)
  
    countryDict = {
        'oxylab' :oxylabCountryList,
        'geosurf' :geosurfCountryList

    }
    with open('country.json','w') as f:
        json.dump(countryDict,f)

# oxylab gen proxy
def genOxylab(count,country,userName,passWord):
    # 获取当前目录下的资源文件
    with open('country.json','r') as countryDict:
        countryDict = json.load(countryDict)

    oxylabCountry = countryDict['oxylab']
    proxyList = []

    if  type(country) == list:
        for j in range(len(country)):
            if country[j].upper() in oxylabCountry:
                for m in range(count):
                    sessionId = random.random()
                    proxyList.append('pr.oxylabs.io:3333:customer-{}-cc-{}-sessid-{}-sesstime-60:{}'.format(userName,country[j],sessionId,passWord))

            else:
                print('oxylab国家代码无效1')
                continue
    else:
        print('oxylab国家代码无效2')

    proxyList = list(set(proxyList))
    print(len(proxyList))
    return proxyList

# geosurf gen proxy
def genGeosurf(count,country,userName,passWord):
    with open(f'country.json','r')  as countryDict:
        countryDict = json.load(countryDict)


    geosurfCountry = countryDict['geosurf']
    # print(geosurfCountry)
    proxyList = []
    if type(country) == list:
        for i in range(len(country)):
            if country[i].upper() in geosurfCountry:
                for j in range(count):
                    ranStr = ''.join(random.sample(string.ascii_letters + string.digits, 6))
                    proxyList.append(f'{country}-90m.geosurf.io:5555:{userName}+{country[i]}+{userName}-{ranStr}:{passWord}')
            else:
                print('geosurf国家代码无效1')
                continue
    else:
        print('geosurf国家代码无效2')
    proxyList = list(set(proxyList))
    print(len(proxyList))
    return proxyList


def main():

    # setupCountry()
    country = input('请输入国家(多个国家请用英文;分开)):')
    if country == '':
         country = 'us;uk'
    print(country)
    addsepline()
    countryList = country.split(';')

    bot = input('请输入你要分配proxy的bot(多个bot请用英文;分开):')
    if bot == '':
        bot = 'cyber;kodai;fleek'
    print(bot)
    addsepline()
    botList = bot.split(';')

    proxyCount = input('请输入你要分配给不同bot的proxy的数量(默认100条,多个国家请用英文;分开)')
    if proxyCount == '':
        proxyCount = '100;100;100'
    print(proxyCount)
    addsepline()
    proxyCountList = proxyCount.split(';')

    #oxylab,geosurf
    provider = input('请输入你要分配proxy的供应商(默认oxy):')
    if provider == '':
        provider = 'geosurf'
    print(provider)
    addsepline()

    userName =  input('请输入你要分配proxy的用户名(默认test001):')
    if userName == '':
        userName = 'test001'
    print(userName)
    addsepline()

    passWord =  input('请输入你要分配proxy的密码(默认123456):')
    if passWord == '':
        passWord = '123456'
    print(passWord)
    addsepline()

    for i in range(len(botList)):
        if provider == 'oxylab':
            proxyList = genOxylab(int(proxyCountList[i]),countryList,userName,passWord)
        elif provider == 'geosurf':
            proxyList = genGeosurf(int(proxyCountList[i]),countryList,userName,passWord)
        else:
            print('暂不支持此供应商，请联系null')
        file = open(f'{botList[i]}.txt','w')
        for i in range(len(proxyList)):
            file.write(proxyList[i])
            file.write('\n')
        file.close()
    
    print(f'proxy分配结束,请到{os.getcwd()}目录下查看')

main()