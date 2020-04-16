# from discord_webhook import DiscordWebhook, DiscordEmbed
from enum import Enum
import wh_cyber,wh_fleek,wh_kodai

def addsepline():
    print("-----------------------------------------------------------------------------------------------")

def addseptag():
    print("##################################################################")



class BotType(Enum):
    cyber = "Cyber"
    kodai = "Kodai"
    fleek = "Fleek"

# main 
bot = input("请选择bot(1:Cyber,2:Kodai,3:Fleek(默认Fleek)):")
if bot == "1":
    bot = BotType.cyber.value
elif bot == "2":
    bot = BotType.kodai.value 
else:
    bot = BotType.fleek.value


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


webhookLink = input("请输入webhook link(默认xxx):")
if webhookLink == "":
	webhookLink = ""
print(webhookLink)
addseptag()


if bot == 'Cyber':
	wh_cyber.cyber(hypeTitle,hypeSize,profileName,hypePicLink,webhookLink)
elif bot == 'Kodai':
	wh_kodai.kodai(hypeTitle,hypeSize,profileName,hypePicLink,webhookLink)
else:
	wh_fleek.fleek(hypeTitle,hypeSize,profileName,hypePicLink,webhookLink)


