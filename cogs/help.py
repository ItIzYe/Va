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
prefix='#'
class help(commands.Cog):
	def __init__(self, client):
		self.client=client

	@commands.group(invoke_without_command=True,aliases=['Help','HELP'])
	async def help(self,ctx):
		em=discord.Embed(title='Hilfe',description=f'Hier findest du die Kategorien, in die der Hilfe Command aufgeteilt ist. Schreibe einfach {prefix}help [Kategorie] um die jeweiligen Commands zu sehen')
		em.add_field(name='Kategorien:',value=f'-Moderation \n-Info \n-Fun')
		await ctx.send(embed=em)


	@help.command(aliases=['Moderation','MODERATION'])
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def moderation(self,ctx):
		em=discord.Embed(title='Moderation',description='Hier siehst du, welche Cmds alle zu dieser Kategorie gehören')
		em.add_field(name='Commands:',value=f'-`Clear` \n-`Kick` \n-`Mute` \n-`Unmute` \n-`Tempmute` \n-`Bann` \n-`Nuke` ')
		em.set_footer(text=f'Benutze {prefix}help [Command] um nähere Infos zu erhalten')
		await ctx.send(embed=em)

	@help.command(aliases=['Info','INFO'])
	async def info(self,ctx):
		em=discord.Embed(title='Info',description='Hier siehst du, welche Cmds alle zu dieser Kategorie gehören')
		em.add_field(name='Commands:',value=f'-`Userinfo` \n-`Serverinfo` \n-`Link` \n-`Boost` \n-`Roles` \n-`Botinfo` \n-`Ping` \n-`Pick` \n-`Ad`')
		em.set_footer(text=f'Benutze {prefix}help [Command] um nähere Infos zu erhalten')
		await ctx.send(embed=em)

	@help.command(aliases=['Fun','FUN'])
	async def fun(self,ctx):
		em=discord.Embed(title='Fun',description='Hier siehst du, welche Cmds alle zu dieser Kategorie gehören')
		em.add_field(name='Commands:',value=f'-`Meme`')
		em.set_footer(text=f'Benutze {prefix}help [Command] um nähere Infos zu erhalten')
		await ctx.send(embed=em)

	@help.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def clear(self,ctx):
		em=discord.Embed(title='Clear',description='Damit kannst du eine von dir angegebene Anzahl an Nachrichten löschen')
		em.add_field(name='Syntax',value=f'`{prefix}clear [Anzahl]`')
		await ctx.send(embed=em)

	@help.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def kick(self,ctx):
		em=discord.Embed(title='Kick',description='Damit kannst du einen Member vom Server kicken')
		em.add_field(name='Syntax',value=f'`{prefix}kick [Member] [Grund]`')
		await ctx.send(embed=em)

	@help.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def mute(self,ctx):
		em=discord.Embed(title='Mute',description='Damit kannst du einen Member muten')
		em.add_field(name='Syntax',value=f'`{prefix}mute [Member] [Grund]`')
		await ctx.send(embed=em)

	@help.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def unmute(self,ctx):
		em=discord.Embed(title='Unmute',description='Damit kannst du einen Member entmuten')
		em.add_field(name='Syntax',value=f'`{prefix}unmute [Member]`')
		await ctx.send(embed=em)

	@help.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def tempmute(self,ctx):
		em=discord.Embed(title='Tempmute',description='Damit kannst du einen Member für eine von dir angegebene Zeit Muten. ACHTUNG: die Zeit wird automatisch in Stunden gemessen. Schreibe also nur die Zahl.')
		em.add_field(name='Syntax',value=f'`{prefix}tempmute [Member] [Zeit] [Grund]`')
		await ctx.send(embed=em)

	@help.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def ban(self,ctx):
		em=discord.Embed(title='Bann',description='Damit kannst du einen Member vom Server bannen')
		em.add_field(name='Syntax',value=f'`{prefix}ban [Member] [Grund]`')
		await ctx.send(embed=em)

	@help.command()
	@commands.has_any_role("Venom Aimz","Owner") 
	async def nuke(self,ctx):
		em=discord.Embed(title='Nuke',description='Damit kannst du einen Kanal löschen und direkt neu erstellen. Das ist hilfreich, wenn ein ganzer Kanal gecleared werden soll')
		em.add_field(name='Syntax',value=f'`{prefix}nuke [Kanal]`')
		await ctx.send(embed=em)


	@help.command()
	async def userinfo(self,ctx):
		em=discord.Embed(title='Userinfo',description='Damit kannst du ein paar Infos von einem bestimmten Member abrufen')
		em.add_field(name='Syntax',value=f'`{prefix}userinfo [Member]`') 
		await ctx.send(embed=em)

	@help.command()
	async def serverinfo(self,ctx):
		em=discord.Embed(title='Serverinfo',description='Damit kannst du ein paar Infos vom Server abrufen')
		em.add_field(name='Syntax',value=f'`{prefix}Serverinfo`') 
		await ctx.send(embed=em)

	@help.command()
	async def boost(self,ctx):
		em=discord.Embed(title='Boost',description='Damit kannst du erfahren, welche Vorteile du erhälst, wenn du diesen Server boostest')
		em.add_field(name='Syntax',value=f'`{prefix}boost`') 
		await ctx.send(embed=em)

	@help.command()
	async def botinfo(self,ctx):
		em=discord.Embed(title='Info',description='Damit kannst du ein paar Infos zum Bot abrufen')
		em.add_field(name='Syntax',value=f'`{prefix}info`') 
		await ctx.send(embed=em)

	@help.command()
	async def ping(self,ctx):
		em=discord.Embed(title='Ping',description='Damit erfährst du den Ping')
		em.add_field(name='Syntax',value=f'`{prefix}ping`') 
		await ctx.send(embed=em)

	@help.command()
	async def link(self,ctx):
		em=discord.Embed(title='Link',description="Damit erhälst du die Links zu Venom Aimz' Social Medias")
		em.add_field(name='Syntax',value=f'`{prefix}link`') 
		await ctx.send(embed=em)

	@help.command()
	async def meme(self,ctx):
		em=discord.Embed(title='Meme',description='Damit erhälst du Memes')
		em.add_field(name='Syntax',value=f'`{prefix}meme`') 
		await ctx.send(embed=em)

	@help.command()
	async def pick(self,ctx):
		em=discord.Embed(title='Pick',description='Damit kannst du anderen schnell zeigen, wie/wo sie ihre Plattformen auswählen können')
		em.add_field(name='Syntax',value=f'{prefix}pick')
		await ctx.send(embed=em)

	@help.command()
	async def ad(self,ctx):
		em=discord.Embed(title='Ad',description='Damit kannst du andern schnell zeigen, warum sie ihre Werbung im Werbung Kanal posten sollen')
		em.add_field(name='Syntax', value=f'{prefix}ad')
		await ctx.send(embed=em)

		
def setup(bot):
	bot.add_cog(help(bot))