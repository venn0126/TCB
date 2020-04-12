from discord_webhook import DiscordWebhook, DiscordEmbed


def kodai(hypeTitle,hypeSize,profileName,hypePicLink,webhookLink):
	profileNameHidden = "||{}||".format(profileName)
	kodai_url = 'https://i.imgur.com/Z1ALPb8.png'
	webhook = DiscordWebhook(url=webhookLink, username='KodaiAIO',avatar_url=kodai_url)
	# embed
	embed = DiscordEmbed(title=':rocket:  **Kodai Success**  :rocket:', description=hypeTitle, color=9763487)
	embed.add_embed_field(name='Store', value='Supreme US')
	embed.add_embed_field(name='Checkout Speed', value='8.537s')
	embed.add_embed_field(name='Product', value=hypeTitle,inline=False)
	embed.add_embed_field(name='Size', value=hypeSize)
	embed.add_embed_field(name='Profile', value=profileNameHidden)
	embed.add_embed_field(name='Order Number', value='||12345||')
	embed.add_embed_field(name='Slot Info', value='||Test-001||')
	embed.set_footer(text='CyberAIO',icon_url=kodai_url)
	embed.set_timestamp()
	embed.set_thumbnail(url=hypePicLink)
	webhook.add_embed(embed)
	response = webhook.execute()
	print("数据发送中,请稍后...")
	if response.status_code == 204:
		print('恭喜🎉!!!您自定义的kodai bot web hook发送成功!')
	else:
		print('很遗憾😭...您自定义的kodai bot web hook发送失败,请检查输入参数.')

	