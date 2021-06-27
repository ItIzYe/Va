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
import glob
import time
import re
import threading
import glob
from time import *
from googletrans import Translator

intents=discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True,bans=True,voice_states=True)
client= commands.Bot(command_prefix=['#'], intents=intents)
client.remove_command("help")

class game(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command(aliases=["game", "Game", "GAME"])
  async def spiel(self, ctx):
    await ctx.send("@" + str(ctx.author) + " Die Funktion ist noch in entwicklung...")

def setup(bot):
  bot.add_cog(game(bot))
