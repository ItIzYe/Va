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

class infos(commands.Cog):
  def __init__(self, client):
    self.client=client


  @commands.command(aliases=['INFO', 'info'])
  async def Info(self,ctx):
    em = discord.Embed(tite="Info",description=" Hier sind ein paar Bot-infos",color=0x1f8b4c)
    em.set_thumbnail(url="https://data.whicdn.com/images/298586557/original.gif")
    em.add_field(name="Name", value="Venom Aimz Bot#5683",inline=False)
    em.add_field(name="Authoren", value="ItIzYe#7590 \n R.M.S Titanic#7956",inline=False)
    em.add_field(name="Version", value="1.0.0",inline=False)
    em.add_field(name="Letztes Update",value=" 05.06.2021 23:04p.m.",inline=False)
    em.set_footer(text=f"Information angefragt von {ctx.author.mention}")
    await ctx.send(embed=em)  #zeigt ein paar Infos zu dem Bot


  @commands.command()
  async def serverinfo(self,ctx):
	  owner = str(ctx.guild.owner)
	  mbed = discord.Embed(color=discord.Color(0xffff),title=f"{ctx.guild.name}")
	  mbed.set_thumbnail(url=f"{ctx.guild.icon_url}")
	  mbed.add_field(name="Owner", value=owner, inline=False)
	  mbed.add_field(name="Region", value=f"`{ctx.guild.region}`", inline=False)
	  mbed.add_field(name="Mitgliederzahl",value=f"`{ctx.guild.member_count}`",inline=False)
	  mbed.set_footer(icon_url=f"{ctx.guild.icon_url}",text=f"GUILD ID: {ctx.guild.id}")
	  await ctx.send(embed=mbed)

  @commands.command(aliases=['Ping', 'PING'])
  async def ping(self,ctx):
	  embed = discord.Embed(title="Pong!",description=f"{round(self.client.latency * 1000)} ms",color=0xFF5733)
	  await ctx.send(embed=embed)




def setup(bot):
	bot.add_cog(infos(bot)) 