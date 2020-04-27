# -*- coding=utf-8 -*-
#@author Augus
#@time 2020/04/27

'''

激活状态码

0:激活成功
-1:激活失败

'''

import cloudscraper
import pandas as pd


def addsepline():
    print("-----------------------------------------------------------------------------------------------")

def addseptag():
    print("##################################################################")

def setupProxyFromUser(proxy):
    proxyList = []
    for i in range(len(proxy)):
        if ':' in proxyListRows[i]:
            temp = proxyListRows[i]
            proxys = temp.split(':')
            proxy = {'http': 'http://' + proxys[2] + ':' + proxys[3] + '@' + proxys[0] + ':' + proxys[1] + '/',
                    'https': 'http://' + proxys[2] + ':' + proxys[3] + '@' + proxys[0] + ':' + proxys[1] + '/'}
            proxyList.append(proxy)
    return proxyList


def setupProxyFromIp(proxy):
    proxyList = []
    for i in range(len(proxy)):
        if ':' in proxyListRows[i]:
            temp = proxyListRows[i]
            proxies = {'http': 'http://' + temp,  'https': 'http://' + temp}
            proxyList.append(proxies)
    return proxyList
 

def importLinkProxy():
	data = pd.read_csv('linkProxy.csv')
	linkList = list(data['link'].values)
	proxyList = list(data['proxy'].values)
	return data,linkList,proxyList


def outputToCsvStatus(i,status,data):
	data['status'][i] = status
	data.to_csv('linkProxy',index=False)


def main():
	addseptag()
	print('开始加载链接和代理...')
	addseptag()
	data,links,proxy = importLinkProxy()
	proxyList = []
	try:
		proxyList = setupProxyFromUser(proxy)
	except:
		proxyList = setupProxyFromIp(proxy)

	headers = {
		    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	}

	
	with open('2captcha.txt') as f:
		apiKey = f.read()
		for i in range(len(links)):
			scraper = cloudscraper.create_scraper(interpreter='nodejs',
													recaptcha={
													'provider': '2captcha',
													'api_key': apiKey
													})
			try:
				r = scraper.get(links[i],headers=headers,proxies=proxyList[i])
				if r.status_code == 200 or r.status_code == 301:
					print('激活成功')
					status = '0'
					outputToCsvStatus(i,status,data)
				else:
					print('激活失败')
					status = '-1'
					outputToCsvStatus(i,status,data)
			except:
				print('激活失败')
				status = '-1'
				outputToCsvStatus(i,status,data)


main()
