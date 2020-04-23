#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Time    : 2020/4/21 18:07
# @Author  : Augus

import requests
import time
import numpy as npy

'''

5. 简单的proxy筛选脚本(支持保存延迟在预设值以下的proxy列表，测试最好能实现多测几次取平均值的逻辑)
- 通过对google的request测试来测试proxy连通性（ 如果你想支持别的网站，可以作为附加项）
- 利用requests 模块实现
- 每条proxy，最好测试多次取其平均值，因为网络有其不稳定性
- 输入为一个proxy列表的txt
- 输出为一个筛选过可以达到proxy的延迟结果程序设置要求的proxy列表（延迟小于 xxx ms)
- 要求在console输出每条

hint:
- requests 的 proxy使用，需要https和http proxy都设置才会生效，并且格式不一样
- 运行该脚本不要再你的本地运行, 需要去服务器或者国外的local
- 延迟设定要根据你的网络情况来决定
'''



def addsepline():
    print("-----------------------------------------------------------------------------------------------")

def addseptag():
    print("##################################################################")



def setupProxyFromUser(fileName):
    proxyList = []
    with open(fileName + '.txt') as f:
        proxyStr = f.read()
        proxyListRows = proxyStr.split('\n')
        for i in range(len(proxyListRows)):
            if ':' in proxyListRows[i]:
                temp = proxyListRows[i]
                proxys = temp.split(':')
                proxy = {'http': 'http://' + proxys[2] + ':' + proxys[3] + '@' + proxys[0] + ':' + proxys[1] + '/',
                        'https': 'http://' + proxys[2] + ':' + proxys[3] + '@' + proxys[0] + ':' + proxys[1] + '/'}
                proxyList.append(proxy)
    return proxyList


def setupProxyFromIp(fileName):
    proxyList = []
    with open(fileName + '.txt') as f:
        proxyStr = f.read()
        proxyListRows = proxyStr.split('\n')
        for i in range(len(proxyListRows)):
            if ':' in proxyListRows[i]:
                temp = proxyListRows[i]
                proxies = {'http': 'http://' + temp,  'https': 'http://' + temp}
                proxyList.append(proxies)
    return proxyList


def testProxy(originProxyList,proxyList,times,averageValue,host):
    lastProxyList = []
    for i in range(len(originProxyList)):
        speedList = []
        for j in range(times):
           try:
            r = requests.get(host,timeout=5,proxies=proxyList[i])
            speedList.append(r.elapsed.microseconds/1000)
            # print('{} response time is {}'.format(p,r.elapsed.microseconds))
           except Exception as e:
            print(f'请求异常,发生错误>{e}')
            
            time.sleep(1)

                # 和要求的平均值比较

        if npy.mean(speedList) < averageValue:
            print('{} speed is {}'.format(originProxyList[i],npy.mean(speedList)))
            lastProxyList.append(originProxyList[i])
            file = open('goodProxy.txt','a')
            file.write(str(originProxyList[i].replace('\'', '')))
            file.write('\n')
            file.close()

    addsepline()
    if not lastProxyList:
        print('筛选完成,没有符合条件的proxy')
    else:
        print('筛选完成,请查看当前目录的goodProxy.txt文件')

def main():
    proxyList = []
    try:
        proxyList = setupProxyFromUser('proxy')
    except :
        proxyList = setupProxyFromIp('proxy')

    if not proxyList:
        print('获取proxy失败,请检查')
        return
    # get origin proxy list
    with open('proxy.txt','r') as f:
        originProxyStr = f.read()
    originProxyList = originProxyStr.split('\n')
    print(f'Loaded {len(originProxyList)} proxies')

    times = input('请输入你想要每个proxy测试的次数(默认3):')
    if times == '':
        times = 3
    print(times)
    addsepline()

    averageValue = input('请输入你想要筛选的延迟的平均值(默认1500ms):')
    if averageValue == '':
        averageValue = 1500
    print(averageValue)
    addsepline()

    host = input('请输入你想要测试的目的主机地址(默认www.google.com):')
    if host == '':
        # host = 'https://www.google.com/'
        host = 'https://www.supremenewyork.com/'
    print(host)
    addsepline()

    # proxyList = [{'http' : 'http://24.172.225.122:53281','https' :'http://24.172.225.122:53281'}]

    print('筛选开始,请稍后...')
    testProxy(originProxyList,proxyList,int(times),float(averageValue),host)

main()
