from discord_webhook import DiscordWebhook, DiscordEmbed
from enum import Enum

def addsepline():
    print("-----------------------------------------------------------------------------------------------")

def addseptag():
    print("##################################################################")



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


def send_webhook(bot,title,color,hypeTitle,hypeSize,profileName,hypePicLink,webhookLink,authName,avatar_url):
	
	profileNameHidden = "||{}||".format(profileName)
	store = 'Store'
	value = 'Supreme US'
	if bot == 'Fleek':
		store = 'Website'
		value = 'FootpatrolFE'

	# dc bot
	webhook = DiscordWebhook(url=webhookLink, username=authName,avatar_url=avatar_url)

	#embed
	embed = DiscordEmbed(title=title,color=color)
	embed.set_footer(text=bot,icon_url=avatar_url)
	embed.set_timestamp()
	embed.add_embed_field(name=store, value=value)

	# set up diff type
	if bot == 'Cyber':
		embed = DiscordEmbed(title=title, description=hypeTitle, color=color)
		embed.add_embed_field(name='Store', value='Supreme US')
		embed.add_embed_field(name='Size', value=hypeSize)
		embed.add_embed_field(name='Profile', value=profileNameHidden)
		embed.add_embed_field(name='Order', value='||123456||')
		embed.add_embed_field(name='Proxy List', value='Test001')
		embed.add_embed_field(name='Color', value='Black')
		embed.add_embed_field(name='Category', value='T-Shirts')
		embed.add_embed_field(name='Captcha Bypass', value='Enabled')
		embed.add_embed_field(name='Mode', value='Safe')

	elif bot == 'Kodai':
		embed.add_embed_field(name='Checkout Speed', value='8.537s')
		embed.add_embed_field(name='Product', value=hypeTitle,inline=False)
		embed.add_embed_field(name='Size', value=hypeSize)
		embed.add_embed_field(name='Profile', value=profileNameHidden)
		embed.add_embed_field(name='Order Number', value='||12345||')
		embed.add_embed_field(name='Slot Info', value='||Test-001||')

	else:
		embed.add_embed_field(name='Product', value=hypeTitle)
		embed.add_embed_field(name='Size', value=hypeSize)
		embed.add_embed_field(name='Price', value='£140.00')
		embed.add_embed_field(name='Payment', value='PayPal')
		embed.add_embed_field(name='Complete Payment', value='[Click here](https://google.com)')


	embed.set_thumbnail(url='https://assets.supremenewyork.com/187799/rs/hQmg8oQK404.jpg')
	webhook.add_embed(embed)
	response = webhook.execute()
	print("数据发送中,请稍后...")
	if response.status_code == 204:
		print("恭喜🎉!!!您自定义的{} bot web hook发送成功!".format(authName))
	else:
		print("很遗憾😭...您自定义的{} bot web hook发送失败,请检查输入参数.")

# main 
auth_name = ""
avatar_url = ""
title = ""
color = 0
bot = input("请选择bot(1:Cyber,2:Kodai,3:Fleek(默认Fleek)):")
if bot == "1":
    bot = BotType.cyber.value
    auth_name = AuthName.cyber.value
    avatar_url = AuthAvatar.cyber.value
    title = "**Successfully checked out!** :rocket:"
    color = 65280
elif bot == "2":
    bot = BotType.kodai.value 
    auth_name = AuthName.kodai.value
    avatar_url = AuthAvatar.kodai.value
    title = ":rocket:  **Kodai Success**  :rocket:"
    color = 9763487

else:
    bot = BotType.fleek.value
    auth_name = AuthName.fleek.value
    avatar_url = AuthAvatar.fleek.value
    title = "**Successfully checked **out!:zap:"
    color = 7535101


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

send_webhook(bot,title,color,hypeTitle,hypeSize,profileName,hypePicLink,webhookLink,authName,avatar_url)

