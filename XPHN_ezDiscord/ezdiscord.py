import requests 
from discord import Webhook,RequestsWebhookAdapter
import discord
class ezWebhook:
	def Send(url,user,message):
		webhook = Webhook.from_url(url,adapter=RequestsWebhookAdapter())
		webhook.send(message,username=user)

class ezBot:
	def Respond(token,trigger,reply):
		client = discord.Client()
		@client.event
		async def on_ready():
			print('logged in as {0.user}'.format(client))
		@client.event
		async def on_message(message):
		          		if message.author == client.user:
		          			return
		          		if message.content==trigger:
		          			await message.channel.send(reply)
		client.run(token)