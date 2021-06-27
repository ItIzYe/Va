import discord
import random
import aiohttp
import json
import os
import time
import asyncio

from discord.utils import get
from discord.ext import commands, tasks
from itertools import cycle

class moderation(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command(aliases=['Clear', 'CLEAR'])
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def clear(self, ctx, amount: int):
		await ctx.channel.purge(limit=amount)
		emb = discord.Embed(title="Erfolg",description=f" {amount} Nachrichten wurden erfolgreich gelöscht :white_check_mark: ")
		await ctx.send(embed=emb)

	@clear.error
	async def clear_error(self,ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(':x: Bitte gebe an, wieviele Nachrichten gelöscht werden sollen :x:')
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(' :x: Dir fehlen die Berechtigungen um diesen Befehl auszuführen :x:')

	@commands.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『♻️』Team/Supporter","『♥️』Familie") 
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		await member.kick(reason=reason)
		channel=self.client.get_channel(718456003817111563)
		await channel.send(f"{member.mention} wurde erfolgreich gekickt.")

	@kick.error
	async def kick_error(self,ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(':x: Bitte gebe an, wer gekickt werden soll, und warum :x:')

	@commands.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def mute(self,ctx,member:discord.Member,reason):
		channel=self.client.get_channel(718456003817111563)
		role=discord.utils.get(ctx.guild.roles, id=795764343962206218)
		member= member or ctx.author
		em=discord.Embed(title='Gemutet',description=f'{member.mention} wurde von {ctx.author.mention} gemutet',color=discord.Color.red())
		em.add_field(name='Grund:',value=reason)
		emb=discord.Embed(title='Gemutet',description='Du wurdest von {ctx.author.mention} gemutet',color=discord.Color.red())
		emb.add_field(name='Grund:',value=reason)
		await channel.send(embed=em)
		await member.add_roles(role)
		await member.send(embed=emb)

	@mute.error
	async def mute_error(slef,ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Bitte gebe an, wer gemutet werden soll, und warum')

	@commands.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def tempmute(self,ctx,member:discord.Member,zeit:int,*,reason):
		channel=self.client.get_channel(718456003817111563)
		role=discord.utils.get(ctx.guild.roles, id=795764343962206218)
		zeit=zeit
		em=discord.Embed(title='Gemutet',decription=f'{member.mention} wurde von {ctx.author.mention} für {zeit} Stunden gemutet')
		em.add_field(name='Grund',value=reason)
		emb=discord.Embed(title='Gemutet',decription=f'Du wurdest von {ctx.author.mention} für {zeit} Stunden gemutet')
		emb.add_field(name='Grund',value=reason)

		member=member or ctx.author
		await channel.send(embed=em)
		await member.send(embed=emb)
		await member.add_roles(role)
		await asyncio.sleep(zeit *60 *60)
		await member.remove_roles(role)

	@tempmute.error
	async def tempmute_error(self,ctx,error):
		if isinstance(error, commands.MissingRequiredArugment):
			await ctx.send(':x: Bitte gebe an, wer gemutet werden soll, wie lange er/sie gemutet sein soll und warum :x:')

	@commands.command()
	@commands.has_role('Owner')
	async def nuke(self,ctx, channel:discord.TextChannel):
		await channel.clone()
		await channel.delete()

	@nuke.error
	async def nuke_error(self,ctx,error):
		if isinstance(error,commands.MissingPermissions):
			await ctx.send(':x: Dir fehlen die Berechtigungen um diesen Command auszuführen :x:')

	@commands.command()
	@commands.has_any_role("Venom Aimz","Owner","Admin Leitung","Admin","Moderator Leitung","Chef Developer","『⚒』Moderator","『⚜️』Server-Sicherheits-Team","『🤖』Developer","『🔨』Test Mod","『♻️』Team/Supporter","『♥️』Familie","『🔰』Test-Team/Supporter" ) 
	async def unmute(self,ctx,member:discord.Member):
		channel=self.client.get_channel(718456003817111563)
		role=discord.utils.get(ctx.guild.roles,id=795764343962206218)
		member= member or ctx.author
		em=discord.Embed(title='Entmutet',description=f':speaker: {member.mention} wurde erfolgreich entmutet :speaker:')
		await member.remove_roles(role)
		await channel.send(embed=em)

	@unmute.error
	async def unmute_error(self,ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Bitte gebe an, wer entmutet werden soll!')


	@commands.command(aliases=['Ban', 'BAN']) 
	@commands.has_permissions(ban_members=True)
	async def ban(self,ctx, member: discord.Member, *, reason):
		channel=self.client.get_channel(718456003817111563)
		await member.send(f"Du wurdest gebannt. \n Grund: {reason}")
		await member.send("Entbannungsserver:")
		await member.send('https://discord.gg/GUMQjgs')
		await member.ban(reason=reason)
		await ctx.send(f' {member.mention} wurde erfolgreich gebannt')
		await channel.send(f'{member.mention} wurde erfolgreich gebannt')


	@ban.error
	async def ban_error(self,ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(' :x: Bitte gebe an, wer gebannt werden soll :x: ')

def setup(bot):
	bot.add_cog(moderation(bot))
