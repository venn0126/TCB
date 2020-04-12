from discord_webhook import DiscordWebhook, DiscordEmbed


def cyber(hypeTitle,hypeSize,profileName,hypePicLink,webhookLink):
	profileNameHidden = "||{}||".format(profileName)

	webhook = DiscordWebhook(url=webhookLink, username='CyberAIO',avatar_url='https://cdn.cybersole.io/media/discord-logo.png')
	# embed
	embed = DiscordEmbed(title='**Successfully checked out!** :rocket:', description=hypeTitle, color=65280)
	embed.add_embed_field(name='Store', value='Supreme US')
	embed.add_embed_field(name='Size', value=hypeSize)
	embed.add_embed_field(name='Profile', value=profileNameHidden)
	embed.add_embed_field(name='Order', value='||123456||')
	embed.add_embed_field(name='Proxy List', value='Test001')
	embed.add_embed_field(name='Color', value='Black')
	embed.add_embed_field(name='Category', value='T-Shirts')
	embed.add_embed_field(name='Captcha Bypass', value='Enabled')
	embed.add_embed_field(name='Mode', value='Safe')
	embed.set_footer(text='CyberAIO',icon_url='https://cdn.cybersole.io/media/discord-logo.png')
	embed.set_timestamp()
	embed.set_thumbnail(url=hypePicLink)
	webhook.add_embed(embed)
	response = webhook.execute()
	print("数据发送中,请稍后...")
	if response.status_code == 204:
		print('恭喜🎉!!!您自定义的cyber bot web hook发送成功!')
	else:
		print('很遗憾😭...您自定义的cyber bot web hook发送失败,请检查输入参数.')

	