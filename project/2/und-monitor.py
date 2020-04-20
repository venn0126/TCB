# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
monitor a product stock and add a new product
'''

import requests
import json 
import jsonpath
import time
from bs4 import BeautifulSoup as bs
import copy
from discord_webhook import DiscordWebhook, DiscordEmbed


def addsepline():
    print("-----------------------------------------------------------------------------------------------")

def addseptag():
    print("##################################################################")


def update_shopify_db(webhookLink,productLink):

		print('开始监控...')
		# url = 'https://undefeated.com/products/og-era-lx-paisley-truewhite'	
		link = productLink + '.json'
		working = False

		headers = {
	        'authority': 'undefeated.com',
		    'cache-control': 'max-age=0',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
		    'sec-fetch-dest': 'document',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		    'sec-fetch-site': 'none',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-user': '?1',
		    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja;q=0.6',
		    'cookie': '__cfduid=d09d419807f4dd37c1818f2c70edcfa811585908364; cart_currency=USD; cart_sig=; _shopify_country=United+States; _shopify_y=aff7102b-518d-4550-820c-762227984b23; secure_customer_sig=',
		    'if-none-match': 'cacheable:d5cb1c48186da58f909b290c3c485ea2',
		    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
		    'Sec-Fetch-Dest': 'image',
		    'If-None-Match': '"i8rrRXjy01lh7HUi1aLxB2L62HY="'
   		 }
		 # Get the products on the site
		productName = ''
		price = ''
		hypePicLink = ''
		idList = []
		variant = []
		try:
			r = requests.get(link,timeout=3, headers=headers)
			working = True
		except:
			try:
				r = requests.get(link,timeout=5, headers=headers)
				working = True
			except:
				working = False

		if working:
			product_json=r.text
			#json string to py obj
			product_dict = json.loads(product_json)
			productName = product_dict['product']['title']
			images = jsonpath.jsonpath(product_dict,expr='$.product.images')
			# print(variants[0])
			hypePicLink = images[0][0]['src']
			# print(hypePicLink)
			variants = jsonpath.jsonpath(product_dict,expr='$.product.variants')
			variant = variants[0]
			price = variants[0][1]['price']
			# print(price)
			# print(type(variants))



		size_avaiable = []
		current_size_avaiable = []
		next_size_avaiable = []


		while True:
		
			# 对比
			if current_size_avaiable != next_size_avaiable:
				print('stock update...')
				send_webhook(webhookLink,productName,productLink,price,current_size_avaiable,idList,hypePicLink)
	   			# 赋值
				next_size_avaiable = copy.deepcopy(current_size_avaiable)


			try:
				res = requests.get(productLink, headers=headers,timeout=3)
				working = True
			except:
				try:
					res = requests.get(productLink, headers=headers,timeout=5)
					working = True
				except:
					working = False

			if working:
				# 获取跳转后的页面源码
				soup = bs(res.content, 'html.parser')
				option_list = soup.find(id='SingleOptionSelector-1').find_all('option')
				#遍历select的选项列表
				# for option in option_list:
	   # 			 	print("value:%s text:%s"%(option['value'],option.text))
				if current_size_avaiable:
	   				current_size_avaiable.clear()

				for option in option_list:
	   				if 'SOLD OUT' not in option.text and option['value']:
	   					current_size_avaiable.append(option['value'])
	   					for var in variant:
	   						if var['option2'] == option['value']:
	   							idList.append(var['id'])
	   							

			time.sleep(5)




def send_webhook(webhookLink,productName,productLink,price,sizeList,idList,hypePicLink):
	price_format = '${}'.format(price)
	# embed
	webhook = DiscordWebhook(url=webhookLink, username='Undefeated',avatar_url='https://cdn.cybersole.io/media/discord-logo.png')

	embed = DiscordEmbed(title=productName, description=productLink, color=65280)
	embed.add_embed_field(name='Price', value=price_format,inline=False)
	for index in range(len(sizeList)):
		carLink = 'https://undefeated.com/cart/{}:1'.format(idList[index])
		value_format = '[{}]({})'.format(idList[index],carLink)
		embed.add_embed_field(name=sizeList[index],value=value_format)

	embed.set_footer(text='AugusAIO',icon_url='https://cdn.discordapp.com/attachments/569722032137437191/677350898556600355/kobe.jpg')
	embed.set_timestamp()
	embed.set_thumbnail(url=hypePicLink)
	webhook.add_embed(embed)
	response = webhook.execute()
	print("数据发送中,请稍后...")
	if response.status_code == 204:
		print('恭喜🎉!!!undefeated库存更新通知发送成功!')
	else:
		print('很遗憾😭...undefeated库存更新通知发送失败,请检查输入参数.')

	


webhookLink = input("请输入webhook link(默认https://discordapp.com/api/webhooks/686448285908860930/I3p93IBKwh5Pc6MVaUmW83S3lGo0kA8hr3GuCtAilZJlErhlrtvPUgjs27iro7tr67Pd):")
if webhookLink == "":
	webhookLink = "https://discordapp.com/api/webhooks/686448285908860930/I3p93IBKwh5Pc6MVaUmW83S3lGo0kA8hr3GuCtAilZJlErhlrtvPUgjs27iro7tr67Pd"
print(webhookLink)
addseptag()


productLink = input("请输入要监控单品链接(默认https://undefeated.com/products/og-era-lx-paisley-truewhite):")
if productLink == "":
	productLink = "https://undefeated.com/products/og-era-lx-paisley-truewhite"
print(productLink)
addseptag()

update_shopify_db(webhookLink,productLink)





        	





