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

class roles(commands.Cog):
	def __init__(self, client):
		self.client=client
	
	
	@commands.group(invoke_without_command=True,aliases=['ROLES','Roles'])
	async def roles(self,ctx):
		em=discord.Embed(title="Rollen",description='Hier Siehst du die Kategorien, in denen die Rollen eingeteilt sind. Mach einfach "role [Kategorie] um die Rollen angezeigt zu bekommen(Kategorien sind ggf. durch Bindestriche getrennt)',color=discord.Color.blue())
		em.add_field(name='Kategorien:',value=f'-unable(nicht erhältlich) \n-Team \n-Stream \n-Anderes \n-Abonnements \n-Plattform \n-Casino Crews \n-Crew Items \n-Casino Ränge \n-Community')
		await ctx.send(embed=em)


	@roles.command(aliases=['nicht-erhältlich','Unable','UNABLE','Nicht-erhältlich'])
	async def unable(self,ctx):
		va= discord.utils.get(ctx.guild.roles, id=714829993632596029)
		own= discord.utils.get(ctx.guild.roles,id=753661768865153174)
		ttt= discord.utils.get(ctx.guild.roles, id=798995539949387816)
		bot= discord.utils.get(ctx.guild.roles, id=717088469930737696)

		venomaimz=f'{va.mention}  -> Diese Rolle hat nur Venom Aimz!'
		owner=f'{own.mention}  -> Diese Rolle hat nur der Server Owner (R.M.S Titanic)'
		ttteam=f'{ttt.mention}  -> Member mit dieser Rolle kümmern sich um die Discord Tuningtreffen'
		bot=f'{bot.mention}  ->Diese Rolle haben nur Bots'
		
		em=discord.Embed(title='nicht Erhältlich:',description=f'{venomaimz} \n{owner} \n{ttteam} \n {bot}',color=discord.Color.purple())
		await ctx.send(embed=em)

	@roles.command(aliases=['Team','TEAM'])
	async def team(self,ctx):
		adm= discord.utils.get(ctx.guild.roles, id=715997333086666813)
		mod= discord.utils.get(ctx.guild.roles, id=715907035493040148)
		sup= discord.utils.get(ctx.guild.roles, id=715907035493040148)
		bot= discord.utils.get(ctx.guild.roles, id=717088469930737696)
		sht= discord.utils.get(ctx.guild.roles, id=769945616872374292)
		dev= discord.utils.get(ctx.guild.roles, id=767455334658736148)

		admin=f'{adm.mention}'
		moderator=f'{mod.mention}'
		support=f'{sup.mention}'
		bot=f'{bot.mention}'
		sicherheit=f'{sht.mention}'
		developer=f'{dev.mention}'

		em=discord.Embed(title='Team',description=f'{admin} \n{moderator} \n{support} \n{bot} \n{sicherheit} \n{developer}',color=discord.Color.purple())
		em.add_field(name='->',value=' Member mit diesen Rollen kümmern sich um den Server und dessen Mitglieder')
		await ctx.send(embed=em)

	@roles.command(aliases=['Stream','STREAM'])
	async def stream(self,ctx):
		yt= discord.utils.get(ctx.guild.roles, id=740122678056452136)
		ttv= discord.utils.get(ctx.guild.roles, id=762402331928428564)

		ytmod=f'{yt.mention}'
		ttvmod=f'{ttv.mention}'

		em=discord.Embed(title='Stram',description=f'{ytmod} \n{ttvmod}',color=discord.Color.purple())
		em.add_field(name='->',value="Member mit diesen Rollen moderieren Venom Aimz' Streams")
		await ctx.send(embed=em)

	@roles.command(aliases=['Anderes','ANDERES'])
	async def anderes(self,ctx):
		fam= discord.utils.get(ctx.guild.roles, id=772539827219333141)
		part= discord.utils.get(ctx.guild.roles, id=782719541754593290)
		yt= discord.utils.get(ctx.guild.roles, id=714829823759089764)
		liv= discord.utils.get(ctx.guild.roles, id=746070152532983879)
		aufn= discord.utils.get(ctx.guild.roles, id=720197580197330965)

		familie=f'{fam.mention} -> Diese Rolle haben nur Familienmitglieder von Venom Aimz'
		partner=f'{part.mention} ->Diese Rolle haben nur Partner von Venom Aimz'
		youtuber=f'{yt.mention} -> Diese Rolle erhälst du, wenn du mehr als 10.000 Abos auf Youtube hast'
		live=f'{liv.mention} -> Diese Rolle erhälst du, wenn du in einem Stream von Venom Aimz mitgemacht hast'
		aufnahme=f'{aufn.mention} -> Diese Rolle erhälst du, wenn du in einem Video von Venom Aimz mitgemacht hast'

		em=discord.Embed(title='Anderes',description=f'{familie} \n{partner} \n{youtuber} \n{live} \n{aufnahme}',color=discord.Color.purple())
		await ctx.send(embed=em)

	@roles.command(aliases=['Abos','ABOS','Abonnements','abonnements','ABONNEMENTS'])
	async def abos(self,ctx):
		vipb= discord.utils.get(ctx.guild.roles, id=747039949265829932)
		sb= discord.utils.get(ctx.guild.roles, id=743933747417841696)
		kvip= discord.utils.get(ctx.guild.roles, id=747039949265829931)
		ttv3= discord.utils.get(ctx.guild.roles, id=766410052323115031)
		ttv2= discord.utils.get(ctx.guild.roles, id=766410052323115030)
		evip= discord.utils.get(ctx.guild.roles, id=747039949265829930)
		ttv1= discord.utils.get(ctx.guild.roles, id=766410052323115029)
		vip= discord.utils.get(ctx.guild.roles, id=747039949265829929)
		mg= discord.utils.get(ctx.guild.roles, id=773457836189024267)
		ttv= discord.utils.get(ctx.guild.roles, id=766410052323115028)
		kmg= discord.utils.get(ctx.guild.roles, id=747039949265829928)

		vipboss=f'{vipb.mention} '
		serverbooster=f'{sb.mention} '
		krasservip=f'{kvip.mention} '
		tier3=f'{ttv3.mention} '
		tier2=f'{ttv2.mention} '
		ehrenhaftervip=f'{evip.mention}'
		tier1=f'{ttv1.mention} '
		vip=f'{vip.mention} '
		mitglied=f'{mg.mention} '
		sup=f'{ttv.mention} '
		kanalmitglied=f'{kmg.mention}'

		em=discord.Embed(title='Abonnements',description=f'{vipboss} \n{serverbooster} \n{krasservip} \n{tier3} \n{tier2} \n{ehrenhaftervip} \n{tier1} \n{vip} \n{mitglied} \n{sup} \n{kanalmitglied}',color=discord.Color.purple())
		em.add_field(name='->',value='Diese Rollen erhälst du, wenn du ein jeweiliges Abonnement auf Youtube oder TwitchTV hast')
		await ctx.send(embed=em)

	@roles.command(aliases=['plattform','Plattform','PLATTFORM','Plattformen','PLATTFORMEN'])
	async def plattformen(self,ctx):
		pc= discord.utils.get(ctx.guild.roles, id=777477675606343681)
		ps5= discord.utils.get(ctx.guild.roles, id=781231005947396106)
		ps4= discord.utils.get(ctx.guild.roles, id=777477677488668682)
		xbox= discord.utils.get(ctx.guild.roles, id=777477683968868352)

		pc=f'{pc.mention}'
		ps5=f'{ps5.mention}'
		ps4=f'{ps4.mention}'
		xbox=f'{xbox.mention}'
		channel=self.client.get_channel(769958149163450409)

		em=discord.Embed(title='Plattformen',description=f'{pc} \n{ps5} \n{ps4} \n{xbox}')
		em.add_field(name='->',value=f'Diese Rollen zeigen an, aufd welcher Plattform du spielst. Du kannst sie dir in {channel} zuweisen')
		await ctx.send(embed=em)

	@roles.command(aliases=['Crews','CREWS','casino-crews','Casino-crews'])
	async def crews(self,ctx):
		fam= discord.utils.get(ctx.guild.roles, id=836176620708036629)
		lib= discord.utils.get(ctx.guild.roles, id=835496466398707782)
		afg= discord.utils.get(ctx.guild.roles, id=841037605734842408)
		canc= discord.utils.get(ctx.guild.roles, id=792407206633013270)

		families=f'{fam.mention} '
		libatz=f'{lib.mention} '
		affengeil=f'{afg.mention} '
		cancer=f'{canc.mention} '

		em=discord.Embed(title='Casino Crews',description=f'{families} \n{libatz} \n{affengeil} \n{cancer}',color=discord.Color.purple())
		em.add_field(name='->',value='Schreibe die Crew CEOs an, um einer Crew beitreten zu können. Crews bringen dir Casino Vorteile')
		await ctx.send(embed=em)

	@roles.command(aliases=['Items','ITEMS','Crew-items','crew-items'])
	async def items(self,ctx):
		aus= discord.utils.get(ctx.guild.roles, id=788504936886829129)
		gel= discord.utils.get(ctx.guild.roles, id=788130989242449920)

		ausweis=f'{aus.mention}'
		geld=f'{gel.mention}'

		em=discord.Embed(title='Casino Ränge',description=f'{ausweis} \n{geld}',color=discord.Color.purple())
		em.add_field(name='->',value='Diese Rollen kann nur ein Crew CEO kaufen. Sie bringen erbringen dir ein Einkommen')
		await ctx.send(embed=em)


	@roles.command(aliases=['Ranks','RANKS','Ränge','ränge','RÄNGE','casino-ränge','Casino-ränge'])
	async def ranks(self,ctx):
		ls= discord.utils.get(ctx.guild.roles, id= 816733615139848252)
		de= discord.utils.get(ctx.guild.roles, id=816730980638916618)
		mr= discord.utils.get(ctx.guild.roles, id=816366350783086613)
		ya= discord.utils.get(ctx.guild.roles, id=771083462915653652)
		ra= discord.utils.get(ctx.guild.roles, id=771071025155801108)
		fl= discord.utils.get(ctx.guild.roles, id=771071063530012703)
		vi= discord.utils.get(ctx.guild.roles, id=771071035960590407)
		ka= discord.utils.get(ctx.guild.roles, id=771071054234779679)
		ha= discord.utils.get(ctx.guild.roles, id=771070428755394580)
		haf= discord.utils.get(ctx.guild.roles, id=771071045809602660)
		ze= discord.utils.get(ctx.guild.roles, id=771070428583821323)
		mi= discord.utils.get(ctx.guild.roles, id=771070445918355487)


		los=f'{ls.mention} '
		deluxo=f'{de.mention} '
		mond=f'{mr.mention} '
		yacht=f'{ya.mention} '
		rakete=f'{ra.mention} '
		flugzeug=f'{fl.mention} '
		villa=f'{vi.mention} '
		karabiner=f'{ka.mention} '
		haus=f'{ha.mention} '
		haftbombe=f'{haf.mention} '
		zentorno=f'{ze.mention} '
		mikro=f'{mi.mention} '

		em=discord.Embed(title='Casino Ränge',description=f'{los} \n{deluxo} \n{mond} \n{yacht} \n{rakete} \n{flugzeug} \n{villa} \n{karabiner} \n{haus} \n{haftbombe} \n{zentorno} \n{mikro} ',color=discord.Color.purple())
		em.add_field(name='->',value='Diese Rollen erbringen dir ein Einkommen. Du kannst sie im Casino Kaufen')
		await ctx.send(embed=em)

	@roles.command(aliases=['Community','COMMUNITY','com','Com','COM'])
	async def community(self,ctx):
		eh= discord.utils.get(ctx.guild.roles, id=718231832306647120)
		dc= discord.utils.get(ctx.guild.roles, id=783566495800229898)
		co= discord.utils.get(ctx.guild.roles, id=777273859312320512)
		so= discord.utils.get(ctx.guild.roles, id=772157871315615754)

		ehre=f'{eh.mention} -> Diese Rolle erhälst du, wenn du bei MEE6 Level 10 erreicht hast'
		werbung=f'{dc.mention} -> Mit dieser Rolle darfst du Serverlinks in #Werbung senden. Frage ein Teammitglied nach dieser Rolle'
		community=f'{co.mention} -> Diese Rolle hat jedes Servermitglied. Damit wirst du gepingt wenn Venom Aimz ein neues Video veröffentlicht'
		social=f'{so.mention} ->Mit dieser Rolle wirst du bei Rockstar News gepingt. Du kannst diese Rolle in #Rolle-entfernen entfernen'

		em=discord.Embed(title='Community',description=f'{ehre} \n{werbung} \n{community} \n{social}',color=discord.Color.purple())
		await ctx.send(embed=em)


def setup(bot):
	bot.add_cog(roles(bot))