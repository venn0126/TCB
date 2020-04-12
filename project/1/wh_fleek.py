from discord_webhook import DiscordWebhook, DiscordEmbed


def fleek(hypeTitle,hypeSize,profileName,hypePicLink,webhookLink):
	profileNameHidden = "||{}||".format(profileName)


	fleek_url = "https://gblobscdn.gitbook.com/assets%2F-M1zBlQKkRH0oc66WnA9%2F-M2-H8mZ_mtoD7BQF5e8%2F-M2-HkEYLT98t5VCJCES%2Fimage.png?alt=media&token=aca1e4c3-782f-4dea-b433-f657fc0c420f"
	
	webhook = DiscordWebhook(url=webhookLink, username='Fleek',avatar_url=fleek_url)
	# embed
	embed = DiscordEmbed(title='**Successfully checked **out!:zap:',color=7535101)
	embed.add_embed_field(name='Website', value='FootpatrolFE')
	embed.add_embed_field(name='Product', value=hypeTitle)
	embed.add_embed_field(name='Size', value=hypeSize)
	embed.add_embed_field(name='Price', value='£140.00')
	embed.add_embed_field(name='Payment', value='PayPal')
	embed.add_embed_field(name='Complete Payment', value='[Click here](https://google.com)')
	embed.set_footer(text='Fleek Framework',icon_url=fleek_url)
	embed.set_timestamp()
	embed.set_thumbnail(url=hypePicLink)
	webhook.add_embed(embed)
	response = webhook.execute()
	print("数据发送中,请稍后...")
	if response.status_code == 204:
		print('恭喜🎉!!!您自定义的fleek bot web hook发送成功!')
	else:
		print('很遗憾😭...您自定义的fleek bot web hook发送失败,请检查输入参数.')

	