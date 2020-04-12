# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import json 
import jsonpath
import time


from enum import Enum

def addsepline():
    print("-----------------------------------------------------------------------------------------------")

def addseptag():
    print("##################################################################")


addsepline()
print("TCB Project-1")
addsepline()


class BotType(Enum):
    cyber = "Cyber"
    kodai = "Kodai"
    fleek = "Fleek"



class AuthName(Enum):
    cyber = "CyberAIO"
    kodai = "KodaiAIO"
    fleek = "Fleek Framework"



class AuthAvatar(Enum):
    cyber = "https://cdn.cybersole.io/media/discord-logo.png"
    kodai = "https://i.imgur.com/Z1ALPb8.png"
    fleek = "https://gblobscdn.gitbook.com/assets%2F-M1zBlQKkRH0oc66WnA9%2F-M2-H8mZ_mtoD7BQF5e8%2F-M2-HkEYLT98t5VCJCES%2Fimage.png?alt=media&token=aca1e4c3-782f-4dea-b433-f657fc0c420f"
	

def send_webhook(bot,hypeTitle,hypeSize,profileName,hypePicLink,webhookLink,authName,avatar_url):
	profileNameHidden = "||{}||".format(profileName)
	content1 = {
    	  "username": authName,
		  "avatar_url": "https://cdn.cybersole.io/media/discord-logo.png",
		  "embeds": [
		    {
		      "title": "**Successfully checked out!** :rocket:",
		      # "url": "https://google.com/",
		      "description": hypeTitle,
		      "color": 65280,
		      "fields": [
		        {
		          "name": "Store",
		          "value": "Supreme US",
		          "inline": True
		        },
		        {
		          "name": "Size",
		          "value": hypeSize,
		          "inline": True
		        },
		        {
		          "name": "Profile",
		          "value": profileNameHidden,
		          "inline": True
		        },
		        {
		          "name": "Order",
		          "value": "||1234567||",
		          "inline": True
		        },
		        {
		          "name": "Proxy List",
		          "value": "Test001",
		          "inline": True
		        },
		        {
		          "name": "Color",
		          "value": "Black",
		          "inline": True
		        },
		        {
		          "name": "Category",
		          "value": "T-Shirts",
		          "inline": True
		        },
		        {
		          "name": "Captcha Bypass",
		          "value": "Enabled",
		          "inline": True
		        },
		        {
		          "name": "Mode",
		          "value": "Safe",
		          "inline": True
		        }
		      ],
		      "thumbnail": {
		       		"url": hypePicLink
		      },
		      # "image": {
		      #  		"url": "https://assets.supremenewyork.com/187799/rs/hQmg8oQK404.jpg"
		      # },
		      "footer": {
		        "text": "CyberAIO • 2020-04-02T23:54:30.000Z",
		        "icon_url": avatar_url
		      }
		    }
		  ]
		}
	content2 = {
		  "username": authName,
		  "avatar_url": "https://i.imgur.com/Z1ALPb8.png",
		  "embeds": [
		    {
		      "title": ":rocket:  **Kodai Success**  :rocket:",
		      # "url": "https://google.com/",
		      # "description": "Tupac Hologram Tee",
		      "color": 9763487,
		      "fields": [
		        {
		          "name": "Store",
		          "value": "Supreme EU",
		          "inline": True
		        },
		        {
		          "name": "Checkout Speed",
		          "value": "8.537s",
		          "inline": True
		        },
		        {
		          "name": "Product",
		          "value": hypeTitle,
		        },
		        {
		          "name": "Size",
		          "value": hypeSize,
		          "inline": True
		        },
		        {
		          "name": "Profile",
		          "value": profileNameHidden,
		          "inline": True
		        },
		        {
		          "name": "Order Number",
		          "value": "||12345||",
		          "inline": True
		        },
		        {
		          "name": "Slot Info",
		          "value": "||Test-001||",
		        }
		      ],
		      "thumbnail": {
		       		"url": hypePicLink
		      },
		      "footer": {
		        "text": "KodaiAIO —— sup-eu-01 • [Thu Apr02 2020]",
		        "icon_url": avatar_url
		      }
		    }
		  ]
		}
	content3 = {
		  "username": authName,
		  "avatar_url": "https://gblobscdn.gitbook.com/assets%2F-M1zBlQKkRH0oc66WnA9%2F-M2-H8mZ_mtoD7BQF5e8%2F-M2-HkEYLT98t5VCJCES%2Fimage.png?alt=media&token=aca1e4c3-782f-4dea-b433-f657fc0c420f",
		  "embeds": [
		    {
		      "title": "**Successfully checked **out!:zap:",
		      # "url": "https://google.com/",
		      # "description": "Tupac Hologram Tee",
		      "color": 7535101,
		      "fields": [
		        {
		          "name": "Website",
		          "value": "FootpatrolFE",
		          "inline": True
		        },
		        {
		          "name": "Product",
		          "value": hypeTitle,
		          # "value": "[https://www.footpatrol.com/product/white-nike-air-force-1-low/375464_footpatrolcom/](https://google.com)",
		          "inline": True
		        },
		        {
		          "name": "Size",
		          "value": hypeSize,
		           "inline": True
		        },
		        {
		          "name": "Price",
		          "value": "£140.00",
		          "inline": True
		        },
		        {
		          "name": "Payment",
		          "value": "PayPal",
		          "inline": True
		        },
		        {
		          "name": "Complete Payment",
		          "value": "[Click here](https://google.com)",
		          "inline": True
		        },
		        {
		          "name": "Profile",
		          "value": profileNameHidden,
		        },
		        {
		          "name": "Checkout Time",
		          "value": "||Test||",
		        }
		      ],
		      "thumbnail": {
		       		"url": hypePicLink
		      },
		      "footer": {
		        "text": "Fleek Framework - 2020-04-02 20:29:47:918632",
		        "icon_url": avatar_url
		      }
		    }
		  ]
		}
	r = None

	if bot == "Cyber":
 		r = requests.post(webhookLink,json=content1)
	elif bot == "Kodai":
		r = requests.post(webhookLink,json=content2)
	else:
		r = requests.post(webhookLink,json=content3)

	print("数据发送中,请稍后...")
	time.sleep(1)
	if r.status_code == 204:
		print("恭喜🎉!!!您自定义的{} bot web hook发送成功".format(authName))
	else:
		print("很遗憾😭...您自定义的{} bot web hook发送失败,请检查输入参数")

# main 
auth_name = ""
avatar_url = ""
bot = input("请选择bot(1:Cyber,2:Kodai,3:Fleek(默认Fleek)):")
if bot == "1":
    bot = BotType.cyber.value
    auth_name = AuthName.cyber.value
    avatar_url = AuthAvatar.cyber.value
elif bot == "2":
    bot = BotType.kodai.value 
    auth_name = AuthName.kodai.value
    avatar_url = AuthAvatar.kodai.value

else:
    bot = BotType.fleek.value
    auth_name = AuthName.fleek.value
    avatar_url = AuthAvatar.fleek.value

hypeTitle = input("请输入单品标题:(默认Supreme Automobile Tee White):")
if hypeTitle == "":
	hypeTitle = "Supreme Automobile Tee White"
print(hypeTitle)
addseptag()

hypeSize = input("请输入单品尺码(默认Medium):")
if hypeSize == "":
	hypeSize = "Medium"
print(hypeSize)
addseptag()

profileName = input("请输入Profile名称(默认Test008):")
if profileName == "":
	profileName = "Test008"
print(profileName)
addseptag()

hypePicLink = input("请输入单品图片链接(默认Supreme Automobile Tee White图片链接):")
if hypePicLink == "":
	hypePicLink = "https://assets.supremenewyork.com/187799/rs/hQmg8oQK404.jpg"
print(hypePicLink)
addseptag()


webhookLink = input("请输入webhook link(默认https://discordapp.com/api/webhooks/686448285908860930/I3p93IBKwh5Pc6MVaUmW83S3lGo0kA8hr3GuCtAilZJlErhlrtvPUgjs27iro7tr67Pd):")
if webhookLink == "":
	webhookLink = "https://discordapp.com/api/webhooks/686448285908860930/I3p93IBKwh5Pc6MVaUmW83S3lGo0kA8hr3GuCtAilZJlErhlrtvPUgjs27iro7tr67Pd"
print(webhookLink)
addseptag()

authName = input("请输入Auth Name(默认为各个bot):") or auth_name
print(authName)
addseptag()

auth_avatar = input("请输入Auth Avatar链接(默认为各个bot头像):") or avatar_url
print(auth_avatar)
addseptag()

send_webhook(bot,hypeTitle,hypeSize,profileName,hypePicLink,webhookLink,authName,avatar_url)