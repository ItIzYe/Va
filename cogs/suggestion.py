import discord
import asyncio
import random
import aiohttp
import json
from discord.utils import get
from discord.voice_client import VoiceClient
from discord.ext import commands, tasks
from itertools import cycle
import os
import time

class suggestion(commands.Cog):
	def __init__(self, client):
		self.client=client

	@commands.command()
	async def suggest(self,ctx, *, reason):
		em = discord.Embed(Title="Vorschlag", description=(reason), color=0xf1c40f)
		em.set_thumbnail(url=ctx.author.avatar_url)
		emb = discord.Embed(Title=" Ihr Vorschlag:",description=ctx.message.author.mention,color=0xf1c40f)
		emb.add_field(name=" Ihr Vorschlag:", value=(reason))
		channel_suggestion = self.client.get_channel(771066263967498273)
		msg = await channel_suggestion.send(embed=em)
		await msg.add_reaction("✅")
		await msg.add_reaction("❌")
		await ctx.message.author.send(embed=emb)
		mbed = discord.Embed(title="Vorschlag",description=f"**{reason}**",color=0xf1c40f)
		mbed.set_thumbnail(url=ctx.author.avatar_url)
		mbed.add_field(name="Einsender", value=ctx.author.mention)
		ID = msg.id
		mbed.set_footer(text=ID)
		await msg.edit(embed=mbed)

	@suggest.error
	async def suggest_error(self,ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(' :x: Bitte gebe einen Wunsch an :x: ')


	@commands.command()
	async def approve(self,ctx, ID, *, reason):
		channel = self.client.get_channel(771066263967498273)
		msg = await channel.fetch_message(ID)
		em = discord.Embed(title='Approved',description=f"Die Suggestion `{msg.embeds[0].description}` wurde angenommen",color=discord.Color.green())
		em.add_field(name="Grund:", value=(reason), inline=False)
		channel_1 = self.client.get_channel(771066263967498273)
		await channel_1.send(embed=em)
		await msg.delete()

	@approve.error
	async def approve_error(self,ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(' :x: Bitte gebe an, welcher Wunsch angenommen werden soll, und warum :x: ')

	@commands.command()
	async def reject(self,ctx, ID, *, reason):
		channel = self.client.get_channel(771066263967498273)
		msg = await channel.fetch_message(ID)
		em = discord.Embed(title='Denied',description=f"Die Suggestion `{msg.embeds[0].description}` wurde abgelehnt",color=discord.Color.red())
		em.add_field(name="Grund:", value=(reason), inline=False)

		channel_1 = self.client.get_channel(771066263967498273)
		await channel_1.send(embed=em)
		await msg.delete()

	@reject.error
	async def reject_error(self,ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(' :x: Bitte gebe an, welcher Wunsch abgelehnt werden soll, und warum :x: ')


def setup(bot):
	bot.add_cog(suggestion(bot))