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

class rules(commands.Cog):
	def __init__(self, client):
		self.client=client

	@commands.command(aliases=['1'])
	async def one(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§1' ,value='Ein freundlicher Umgang ist Pflicht!')
		await ctx.send(embed = em)


	@commands.command(aliases=['2'])
	async def two(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§2' ,value='Spamnachrichten sind nicht erlaubt! (Warn bis zu 3h Mute)')
		await ctx.send(embed = em)

	@commands.command(aliases=['3'])
	async def three(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§3' ,value='Unangemessene Namen oder Bilder, sowie Profilbilder sind nicht erlaubt! (Kick oder Bann)')
		await ctx.send(embed = em)

	@commands.command(aliases=['4'])
	async def four(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§4' ,value='Wer andere User belästigt oder nervt, wird mit einem Kick oder Bann bestraft.')
		await ctx.send(embed = em)

	@commands.command(aliases=['5'])
	async def five(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§5' ,value='Screenshots von Konversationen machen und diese hochladen ist nicht erlaubt.Screenshots von Konversationen machen und diese hochladen ist nicht erlaubt. Ausnahme besteht bei der Meldung eines Users. (Warn, Mute, Kick oder Tempbann)')
		await ctx.send(embed = em)

	@commands.command(aliases=['6'])
	async def six(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§6' ,value='Das Aufnehmen in Sprachräumen ist nur erlaubt, wenn alle sich im Raum befindenden User damit einverstanden sind! (Warn, Mute, Kick oder Bann)')
		await ctx.send(embed = em)

	@commands.command(aliases=['7'])
	async def seven(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§7' ,value='Das Hochladen oder teilen von Viren,Trojanern und sonstiger Malware ist strengstens verboten! (sofortiger unaufhebbarer Bann)')
		await ctx.send(embed = em)

	@commands.command(aliases=['8'])
	async def eight(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§8' ,value='Das Hochladen oder teilen von pornografischen Inhalten ist ebenfalls strengstens verboten! (Bann)')
		await ctx.send(embed = em)

	@commands.command(aliases=['9'])
	async def nine(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§9' ,value='Wer sich fälschlich als großen YouTuber ausgibt, wird von diesem Server permanent gebannt!')
		await ctx.send(embed = em)

	@commands.command(aliases=['10'])
	async def ten(self,ctx):
		mod = discord.utils.get(ctx.guild.roles, id =715907035493040148)
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§10' ,value=f'Das ausgeben als eine andere Person (Identitätsdiebstahl) ist verboten! Dazu gehören schon die selben Namen wie von einem {mod.mention}  oder höher! (3 Warns, Kick oder Bann)')
		await ctx.send(embed = em)

	@commands.command(aliases=['11'])
	async def eleven(self,ctx):
		dc = discord.utils.get(ctx.guild.roles, id=783566495800229898)
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§11' ,value=f'Das Abwerben dieses Servers ist nicht gestattet! Nur mit der Rolle {dc.mention} ist diese Regel außer Kraft gesetzt. (Discord-Server-Links) (Mute, Kick oder Bann)')
		await ctx.send(embed = em)

	@commands.command(aliases=['12'])
	async def twelve(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§12' ,value='Reflinks (bspw. von Amazon) sind nicht erlaubt. (Warn, Mute oder Kick)')
		await ctx.send(embed = em)

	@commands.command(aliases=['13'])
	async def thirteen(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§13' ,value='Keine Falschmeldungen verbreiten. (3h Mute)')
		await ctx.send(embed = em)

	@commands.command(aliases=['14'])
	async def fourteen(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§14' ,value=' Kein Emoji-Spam. (Warn oder 1h Mute)')
		await ctx.send(embed = em)

	@commands.command(aliases=['15'])
	async def fiveteen(self,ctx):
		admin = discord.utils.get(ctx.guild.roles, id=715997333086666813)
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§15' ,value=f'Die Leitung und damit die {admin.mention} haben das Sagen, egal was in den Regeln steht!')
		await ctx.send(embed = em)

	@commands.command(aliases=['16'])
	async def sixteen(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§16' ,value='Discord ist laut den AGB ab 13 Jahren erlaubt! Sollte der Verdacht bestehen dieses Alter nicht zu erfüllen, kann es zu einem Report und Kick kommen!')
		await ctx.send(embed = em)

	@commands.command(aliases=['17'])
	async def seventeen(self,ctx):
		channel = self.client.get_channel(715902273435467776)
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§17' ,value=f'Das Teilen von Social Media-Links ist nur unter {channel.mention} gestattet! In diesem Chat dürft ihr auch für eure Videos werben! (Videospam und das Betteln nach Abos ist nicht erlaubt.) ( 6h/12h Mute oder Kick)')
		await ctx.send(embed = em)

	@commands.command(aliases=['18'])
	async def eighteen(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§18' ,value='Keine beleidigenden Emotes verwenden. (Warn, 3h Mute oder Kick)')
		await ctx.send(embed = em)

	@commands.command(aliases=['19'])
	async def nineteen(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§19' ,value='Keine Stimmenverzerrer oder Soundboards verwenden (Kick oder Bann)')
		await ctx.send(embed = em)


	@commands.command(aliases=['20'])
	async def twenty(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§20' ,value='Private so auch psychische Probleme haben hier nichts zu suchen. Wir sind keine Psychologenpraxis!')
		await ctx.send(embed = em)

	@commands.command(aliases=['21'])
	async def twenty_one(self,ctx):
		channel = self.client.get_channel(726170999468326933)
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§21' ,value=f'Auch die Moderatoren dürfen NICHT gegen die Regeln verstoßen, außer sie haben einen guten Grund!!! Die Regeln stehen dazu in {channel.mention} (Ausstoß aus dem Team)')
		await ctx.send(embed = em)

	@commands.command(aliases=['22'])
	async def twenty_two(self,ctx):
		venom = discord.utils.get(ctx.guild.roles, id=714829993632596029 )
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§22' ,value=f'{venom.mention} zu erwähnen ist verboten! (Mute, Kick)')
		await ctx.send(embed = em)

	@commands.command(aliases=['23'])
	async def twenty_three(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§23' ,value='Wir behalten uns das Recht vor die Namen einzelner oder mehrerer Mitglieder zu ändern.')
		await ctx.send(embed = em)

	@commands.command(aliases=['24'])
	async def twenty_four(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§24' ,value='Das Venom Aimz Discord Team muss sich in keinerlei Hinsicht gegenüber den Nutzern rechtfertigen!')
		await ctx.send(embed = em)

	@commands.command(aliases=['25'])
	async def twenty_five(self,ctx):
		channel = self.client.get_channel(769978204898983956)
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§25' ,value=f'Musik-Bots dürfen NUR mit der Einwilligung ALLER Nutzer in einem Sprach-Kanal genutzt werden. Befehle für den Bot bitte nur in {channel.mention}  . (1h Mute)')
		await ctx.send(embed = em)

	@commands.command(aliases=['26'])
	async def twenty_six(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§26' ,value='Das ist keine Regel, aber sehr wichtig. Wir sind KEINE Sekte, sondern die Community eines GTA YouTubers!')
		await ctx.send(embed = em)

	@commands.command(aliases=['27'])
	async def twenty_seven(self,ctx):
		mod = discord.utils.get(ctx.guild.roles, id =715907035493040148)
		admin = discord.utils.get(ctx.guild.roles, id=715997333086666813)
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§27' ,value=f'Die Nachrichten von {mod.mention}  und {admin.mention} sind zu beachten!!! (24h Mute oder Kick)')
		await ctx.send(embed = em)

	@commands.command(aliases=['28'])
	async def twenty_eight(self,ctx):
		channel = self.client.get_channel(740476324824612874)
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§28' ,value=f'Die Regeln für {channel.mention}   stehen in der Kanalbeschreibung. (Warn oder 1h Mute)')
		await ctx.send(embed = em)

	@commands.command(aliases=['29'])
	async def twenty_nine(self,ctx):
		owner = discord.utils.get(ctx.guild.roles, id =753661768865153174)
		venom =discord.utils.get(ctx.guild.roles, id=714829993632596029 )
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§29' ,value=f'Keiner aus dem Team kann für einen oder mehrere Accounts verantwortlich gemacht werden. Diese Regel kann nur durch den {owner.mention} oder venom.mention aufgehoben werden, wenn es einen guten Grund gibt. ')
		await ctx.send(embed = em)

	@commands.command(aliases=['30'])
	async def thirty(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§30' ,value='Wir behalten uns das Recht vor diese Regeln jeder Zeit zu ändern!')
		await ctx.send(embed = em)

	@commands.command(aliases=['31'])
	async def thirty_one(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§31' ,value='Der rechtliche Weg bei einem Bann ist nicht möglich. (Entbannungsanträge können aber erstellt werden.)')
		await ctx.send(embed = em)

	@commands.command(aliases=['32'])
	async def thirty_two(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§32' ,value='Die Sprache dieses Servers ist Deutsch. Bitte schreibt daher auch in Deutsch, so gut ihr es könnt. Alternativ wird auch Englisch noch akzeptiert. Allerdings gibt es dann nur einen eingeschränkten Support. ')
		await ctx.send(embed = em)

	@commands.command(aliases=['33'])
	async def thirty_three(self,ctx):
		owner = discord.utils.get(ctx.guild.roles, id =753661768865153174)
		venom =discord.utils.get(ctx.guild.roles, id=714829993632596029 )
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§33' ,value=f'Der rechtliche Weg gegen diesen Server ist nicht möglich. Nur von {venom.mention}  und dem {owner.mention} !')
		await ctx.send(embed = em)

	@commands.command(aliases=['34'])
	async def thirty_four(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§34' ,value='Wir behalten uns das Recht vor automatisch alle gelöschten Nachrichten und hinzugefügten Rollen zu Protokoll zu nehmen.')
		await ctx.send(embed = em)

	@commands.command(aliases=['35'])
	async def thirty_five(self,ctx):
		em= discord.Embed(title='Regeln', description='Moin, mein `Regeln` Protokoll wurde ausgeführt, damit ich dir zeige, gegen welche Regeln du verstoßen hast.')
		em.add_field(name='§35' ,value='Hier gelten die allgemeinen Community Richtlinien https://discord.com/new/guidelines')
		await ctx.send(embed = em)



def setup(bot):
	bot.add_cog(rules(bot))