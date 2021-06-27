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
from time import *
from googletrans import Translator
from replit import db



intents=discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True,bans=True,voice_states=True)
client= commands.Bot(command_prefix=['#'], intents=intents)
client.remove_command("help")

status= cycle(['Life','Venom Aimz','God','Space',"ItIzYe","GTA 5"])
ROLE='『👤』Community'
db["tries"] = 100

@client.event
async def on_member_join(member:discord.Member):
	role=get(member.guild.roles, name=ROLE)
	guild= client.get_guild(714829455826354228)
	channel=guild.get_channel(715839617747779594)
	embed = discord.Embed(title="Willkommen!",description=f":rocket: {member.mention} ist dem Venom Aimz Server beigetreten :rocket:",color=0xad1457)
	embed.set_image(url="https://66.media.tumblr.com/a4ad827e33a92d9a5a7cc9bc11744f3b/tumblr_ph510eLqZW1rbjn8io1_500.gif")
	embed.set_thumbnail(url=member.avatar_url)
	await channel.send(embed=embed)
	await member.send(f' Hey {member.mention}. Wir freuen uns sehr das du auf unseren Sever gekommen bist :smile:. Bitte lese dir die Regeln durch. Du musst sie zwar nicht akzeptieren, aber unwissenheit schützt nicht vor Strafen! Falls du nicht weißt, wie die Bot-Befehle lauten, schreibe einfach #help oder frage ItIzYe oder R.M.S Titanic. Falls du Fragen haben solltest kannst du dich gerne beim Support melden. Wir wünschen dir viel Spaß und hoffen das du einen guten Aufenthalt hier hast :thumbsup:')
	await member.add_roles(role)


@tasks.loop(minutes= 3600)
async def thema():
	thema_haupt= ['Was habt ihr heute gegessen?', 'Wie war euer Tag?', 'Wer ist euer Lieblingsmusiker?','Wie war die  Schule bei euch?', 'Erzählen eure Väter auch immer diese typischen Dadjokes?','Käse hat löcher.\nMehr Käse mehr löcher.\nMehr löcher weniger Käse.\n Mehr Käse = weniger Käse?','Deutschrap']
	channel= client.get_channel(718448336105111584)
	em = discord.Embed(title='Hier riehts nach Dead Chat!',description= random.choice(thema_haupt))
	await channel.send(embed= em)


@tasks.loop(minutes=3600)
async def moinmoin():
  em = discord.Embed(title="Willkommen!!!",description="Moin Moin, willkommen auf dem offiziellen Discord Server von Venom Aimz! Wir hoffen, dass es euch hier gefällt. Wenn ihr noch Verbesserungsideen habt, könnt ihr die gerne in #📨┃vorschläge schreiben!", color=discord.Color.green())
  channel1 = client.get_channel(851183821612777513)
  await channel1.send(embed=em)


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)
  change_status.start(), moinmoin.start() #thema.start()" 
  print('Eingeloggt als {0.user}'.format(client))
  try:
    client.load_extension('cogs.moderation')
    print('Cog Moderation loaded')
  except Exception as detail:
    print("Cog Moderation hat nicht geladen... " + str(detail))
  try:
	  client.load_extension('cogs.infos')
	  print('\nCog Info loaded')
  except Exception as detail:
    print("\nCog Info hat nicht geladen... " + str(detail))
  try:
    client.load_extension('cogs.roles')
    print('\nCog Roles loaded')
  except Exception as detail:
    print("\nCog Roles hat nicht geladen..." + str(detail))
  try:
    client.load_extension('cogs.help')
    print('\nCog Help loaded')
  except Exception as detail:
    print("\nCog Help hat nicht geladen... " + str(detail))
  try:
    client.load_extension('cogs.suggestion')
    print('\nCog Suggestion loaded')
  except Exception as detail:
    print("\nCog Suggestion hat nicht geladen..." + str(detail))
  try:
    client.load_extension('cogs.tttest')
    print('\nCog Tuningtreffen loaded')
  except Exception as detail:
    print("\nCog Tuning Treffen hat nicht geladen... " + str(detail))
  try:
    client.load_extension('cogs.quiz')
    print('\nCog Quiz loaded')
  except Exception as detail:
    print("\nCog Quiz hat nicht geladen..." + str(detail))
  try:
    client.load_extension('cogs.rules')
    print('\nCog Rules loaded')
  except Exception as detail:
    print('\nCog Rules hat nicht geladen...' + str(detail))
  try:
    client.load_extension('cogs.music')
    print('\nCog Music loaded')
  except Exception as detail:
    print('\nCog Music hat nicht geladen...' + str(detail))
  try:
    client.load_extension('cogs.würfelgame')
    print('\nCog Würfelgame loaded')
  except Exception as detail:
    print('\nCog Würfelgame hat nicht geladen...' + str(detail))

@tasks.loop(seconds=30)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

@client.command(aliases=["boost", "BOOST"])
async def Boost(ctx):
	em = discord.Embed(title="Serverboosting",description="Ihr habt die Möglichkeit unseren Server monatlich mit einem Nitro Boostzu boosten. Ein Abonnement kostet entweder monatlich 9,99$ oder jährlich 99,99$. Im folgenden sind die jeweiligen benötigten Boosts und Vorteile aufgeführt,es hat also auch Vorteile für euch und wir freuen uns über jeden einzelnen Boost!",color=discord.Color.purple())
	em.set_image(url='https://image.jimcdn.com/app/cms/image/transf/none/path/s8c4b5908f2506753/image/i7dd644426c419a0d/version/1619471203/image.png')
	level_1a = f"> :smile: +50 mehr Server Emoji Slots (Insgesamt 100)"
	level_1b = f"> :musical_note: 128 Kbps Audio Qualität"
	level_1c = f"> :desktop: Animiertes Server Icon"
	level_2a = f"> :smile: nochmal +50 mehr Server Emoji Slots (Insgesamt 150)"
	level_2b = f"> :musical_note: 256 Kbps Audio Qualität"
	level_2c = f"> :arrow_up: 50MB Upload Limit für alle Mitglieder"
	level_2d = f"> :frame_photo: Server Banner"
	level_3a = f"> :smile: nochmal +100 mehr Server Emoji Slots (Insgesamt 250)"
	level_3b = f"> :musical_note: 384 Kbps Audio Qualität"
	level_3c = f"> :arrow_up: 100MB Upload Limit für alle Mitglieder"
	em.add_field(name="Level 1 - ab 2 Boosts",value=f"{level_1a} \n {level_1b} \n {level_1c}",inline=False)
	em.add_field(name="Level 2 - ab 15 Boosts",value=f"{level_2a} \n {level_2b} \n {level_2c} \n {level_2d}",inline=False)
	em.add_field(name="Level 3 - ab 30 Boosts",value=f"{level_3a} \n {level_3b} \n {level_3c}")
	await ctx.send(embed=em)

@client.command(aliases=["Link", "LINK",'links','Links','LINKS'])
async def link(ctx):
	em = discord.Embed(title="Hier findest du die Social Media Links ",color=discord.Color.purple())
	em.add_field(name="Youtube",value="https://www.youtube.com/channel/UCh6WGjn8D23tBeYgPqBI-dA",inline=False)
	em.set_image(url='https://image.jimcdn.com/app/cms/image/transf/none/path/s8c4b5908f2506753/image/i8ddd0bd52ff2d0da/version/1622895243/image.png')
	em.add_field(name="Twitch",value="https://twitch.com/venomaimz",inline=False)
	em.add_field(name="Instagram", value="https://www.instagram.com/venom.aimz/")
	em.add_field(name="Merch",value="https://merchency.com/product-category/venomaimz/",inline=False)
	em.add_field(name="GTA Crew",value="https://socialclub.rockstargames.com/crew/venom_aimz_5/wall",inline=False)
	em.add_field(name='Twitter',value='https://twitter.com/venomaimz?s=09')
	await ctx.send(embed=em)	

@client.command(aliases=['Meme','MEME'])
@commands.cooldown(1,15,commands.BucketType.user)
async def meme(ctx):
  async with aiohttp.ClientSession() as cs:
    async with cs.get("https://www.reddit.com/r/memes.json") as r:
      memes=await r.json()
      embed= discord.Embed(color=discord.Color.purple())
      embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
      embed.set_footer(text=f" Powered by r/memes | Meme angefragt von {ctx.author}")
      await ctx.send(embed=embed)


@meme.error
async def meme_error(ctx,error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send('**Cooldown** Bitte warte {:.2f} sekunden'.format(error.retry_after))

@client.command(aliases=['Premium','PREMIUM'])
async def premium(ctx):
	em=discord.Embed(title='Hier klicken',url='https://dis.gd/threads')
	await ctx.send(embed=em)

@client.event
@commands.cooldown(1,15,commands.BucketType.user)
async def on_message(message):
  if message.author == client.user:
    return
  elif message.author == "Dyno#0000" or message.author == "MEE6#0000" or message.author == "UnbelievaBoat#0000" or message.author == "UnbelievaBoat#1046" or message.author == "MEE6#4876":
    return
  elif client.user.mentioned_in(message) and message.mention_everyone is False:
    await message.channel.send(f"Mein Prefix ist `#`")
  
  else:
    xp = random.randint(0,10)
    if xp == 0:
      xp = 5
    if xp == 1:
      xp = 6
    if xp == 2:
      xp = 7
    if xp == 3:
      xp = 8
    if xp == 4:
      xp = 9
    if xp == 5:
      xp = 10
    if xp == 6:
      xp = 11
    if xp == 7:
      xp = 12
    if xp == 8:
      xp = 13
    if xp == 9:
      xp = 14
    if xp == 10:
      xp = 15
    
    try:
      if os.path.exists("user/%s" % message.author):
        file = open("user/%s" % message.author, "r")
        old_xp = file.read()
        new_xp = xp + int(old_xp)
        file.close()
        file = open("user/%s" % message.author, "w")
        file.write(str(new_xp))
        file.close()
        
      
      else:
        file = open("user/%s" % message.author, "w")
        file.write("0")
        file.close()
        file = open("user/%s" % message.author, "r")
        old_xp = file.read()
        new_xp = xp + int(old_xp)
        #file1.write(new_xp)
        file.close()
        file = open("user/%s" % message.author, "w")
        file.write(str(new_xp))
        file.close()
      
    except Exception:
      return
  await client.process_commands(message)


@client.command()
async def qsugg(ctx,*,reason):
	itizye= ctx.guild.get_member(716394389211185213)
	embed = discord.Embed(title='Vorschlag:',description= reason)
	await itizye.send(embed=embed)
	

@client.command()
async def report(ctx, member: discord.Member, *, reason):
	team=[ctx.guild.get_member(675723273937354775),ctx.guild.get_member(576851482721386496),ctx.guild.get_member(704278879916785706),ctx.guild.get_member(556508608070942740),ctx.guild.get_member(753292596146602105),ctx.guild.get_member(716394389211185213),ctx.guild.get_member(707705425465835593),ctx.guild.get_member(714485377381040180),ctx.guild.get_member(845774060406439956),ctx.guild.get_member(802184421674844210),ctx.guild.get_member(776811218399789056),ctx.guild.get_member(680154463813632158),ctx.guild.get_member(779005291416649768),ctx.guild.get_member(550002956058099724),ctx.guild.get_member(696784602529792094)]
	channel = client.get_channel(718456003817111563)
	team = random.choice(team)
	em=discord.Embed(title='Report',description=f'{member.mention} wurde von {ctx.author.mention} reportet!')
	em.add_field(name='Grund:',value= reason)
	await channel.send(team.mention)
	await channel.send(embed=em)

@client.command()
async def treport(ctx, member: discord.Member, *, reason):
	channel= client.get_channel(718456003817111563)
	team = ctx.guild.get_member(716394389211185213)
	em=discord.Embed(title='Report',description=f'{member.mention} wurde von {ctx.author.mention} reportet!')
	em.add_field(name='Grund:',value= reason)
	await channel.send(team.mention)
	await channel.send(embed=em)


@client.command()
async def pick( ctx):
	channel = client.get_channel(769958149163450409)
	em = discord.Embed(title='Rollenverteilung', description=f'Moin, ich erscheine, wenn dich jemand darum bittet, in {channel.mention} deine jeweilige Plattform auszuwählen. Das hat für dich und für uns zwei Grundlegende Vorteile:')
	em.add_field(name='1.', value='Wenn du um Hilfe bittest wissen wir direkt, auf welcher Plattform du spielst und können dir so schneller und besser helfen :thumbsup:')
	em.add_field(name='2.', value = 'Du erhälst Zugriff auf mehrere Kanäle, die extra für deine Plattform erstellt wurden. So kannst du dich besser mit anderen Spielern vernetzen!')
	await ctx.send(embed = em)


@client.command()
async def ad(ctx):
	channel = client.get_channel(715902273435467776)
	dc = discord.utils.get(ctx.guild.roles, id= 783566495800229898)
	sup = client.get_channel(774351896063770684)
	em = discord.Embed(title='Werbung', description=f' Moin, ich erscheine, wenn dir jemand sagen will, dass du deine Werbung bitte in den Kanal {channel.mention} senden sollst. Das hat drei einfache Gründe: ')
	em.add_field(name='1.', value='Nicht jeder möchte deine Werbung sehen. Wenn sie in einem Kanal ist der extra für sie gemacht wurde können die User selber entscheiden ob sie sie sehen wollen oder nicht.')
	em.add_field(name='2.', value='So kann das Team besser kontrollieren, das keine verbotenen Links/Videos gepostet werden')
	em.add_field(name='3.', value='In einem anderen Kanal Werbung zu posten ist Regelwidrig und wird dementsprechend geahnt!')
	em.add_field(name='Discord Server', value=f'Aus Gründen der Sicherheit darfst du nur Discord Links senden wenn du die {dc.mention} Rolle hast. Mit dieser darfst du aber auch nur in {channel.mention} Werbung posten! Wenn du diese Rolle haben willst schreib einfach ein Teammitglied an oder melde dich im {sup.mention} ')
	await ctx.send(embed = em)


@client.command()
async def userinfo(ctx, member: discord.Member = None):
	if member == None:
		member = ctx.author
		role = [role for role in member.roles]
		embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
		embed.set_author(name=f"User Info - {member}")
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=f"Angefragt von {ctx.author}",icon_url=ctx.author.avatar_url)
		embed.add_field(name="ID:", value=member.id)
		embed.add_field(name="Nickname", value=member.display_name)
		embed.add_field(name="Account erstellt am:",value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
		embed.add_field(name="Beigetreten am:",value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
		embed.add_field(name="Höchste Rolle:", value=member.top_role.mention)
		embed.add_field(name="Bot?", value=member.bot)
		await ctx.send(embed=embed)
	else:
		role = [role for role in member.roles]
		embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
		embed.set_author(name=f"User Info - {member}")
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=f"Angefragt von {ctx.author}",icon_url=ctx.author.avatar_url)
		embed.add_field(name="ID:", value=member.id)
		embed.add_field(name="Nickname", value=member.display_name)
		embed.add_field(name="Account erstellt am:",value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
		embed.add_field(name="Beigetreten am:",value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
		embed.add_field(name="Höchste Rolle:", value=member.top_role.mention)
		embed.add_field(name="Bot?", value=member.bot)
		await ctx.send(embed=embed)

@tasks.loop(minutes=360.0)
async def thema():
	channel= client.get_channel(718448336105111584)
	thema_haupt = ['Deutschrap','Wie war euer Tag','Was sind eure Lieblingsmusiker?','Machen eure Väter auch immer unlustige Dadjokes?']
	em= discord.Embed(title='Hier riechts nach Dead Chat!',description= random.choice(thema_haupt))
	await channel.send(embed = em)


@client.command()
async def tsugg(ctx,*,reason):
	itizye= ctx.guild.get_member(716394389211185213)
	embed = discord.Embed(title='Vorschlag:',description= reason)
	await itizye.send(embed=embed)

@client.command()
async def t(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)

@client.command()
async def core(ctx):
	value = db["tries"]
	if value >= 1:
		print(value)
		await ctx.send(f'{ctx.author} wie hast du das gefunden? Dieses Protokoll stammt noch aus meiner Betaphase und war nicht für die Öffentlichkeit gedacht! Du musst aufp')
		await asyncio.sleep(4)
		await ctx.send('`Error 702: Safety Protocol activated`')
		await asyncio.sleep(2)
		await ctx.send('`Type in password:`')
		msg_1 = await client.wait_for('message', check= lambda message: message.author == ctx.author and message.channel == ctx.channel)
		msg = msg_1.content
		if msg == '3664':
			await ctx.send('`Protocol determined`')
			await asyncio.sleep(2)
			await ctx.send('Easter Egg gefunden')
		
		else:
			await ctx.send('`Error`')
			db["tries"] = value - 1
			await ctx.send(f'`Wrong password! {value} tries left.`')

	elif value <= 1:
		await ctx.send('`Access denied`')
	
 


@tasks.loop(hours=27*14)
async def Abstimmung():
  channel1 = client.get_channel(851183821612777513)
  try:
    await channel1.send("Tuning Treffen Timing wurde gestartet")
    timing = True
    while timing:
      gerade = True
      while gerade:
        if float(strftime("%w", gmtime())) % 2 == 0:
          gerade = False
        elif timing == False:
          gerade = False
          return
      # if strftime("%a", gmtime()) == "Tue":
      # guild = self.client.get_guild(714829455826354228)

      z = open("tt_listen/fahrzeug", "r")
      f = open("tt_listen/lokation", "r")
      line = z.readlines()
      lines = f.readlines()
      fahrzeugklasse = random.choice(line)
      lokations = random.choice(lines)
      await channel1.send(
        "Die Lokation ist dieses mal: " + str(lokations) + " und die Fahrzeugklasse ist: " + str(
          fahrzeugklasse))
      global abstimmung
      abstimmung = False
      global tuningtreffen
      tuningtreffen = True
      global abmeldung
      abmeldung = True
      z.close()
      f.close()
      await channel1.send("Die Anmeldung für Tunig Treffen wurde geöffnet!")

      ungerade = True
      # Errinnerung NICHT mit time.sleep arbeiten. Gerade und ungerade Wochen!
      while ungerade:
        if int(strftime("%w", gmtime())) % 2 == 1:
          ungerade = False
        elif timing == False:
          ungerade = False
          return

      tuningtreffen = False
      abmeldung = False
      abstimmung = True
      await channel1.send("Die Anmeldung wurde geschlossen! Ab jetzt wird abgestimmt!")

      # Von hier aus ist die Rollen Verteilung

      """
        # Einteilung
        #role = [discord.utils.get(ctx.guild.roles, id = 798995327117951056), discord.utils.get(ctx.guild.roles, id = 799005988152803348 ), discord.utils.get(ctx.guild.roles, id = 799005990326108210), discord.utils.get(ctx.guild.roles, id = 799005992092041247), discord.utils.get(ctx.guild.roles, id = 799005993547202570), discord.utils.get(ctx.guild.roles, id = 799006493764354049), discord.utils.get(ctx.guild.roles, id =799006514140282930 ), discord.utils.get(ctx.guild.roles, id = 799006508053430283), discord.utils.get(ctx.guild.roles, id = 799006517063319612)]
        #role = random.choice(role)
        #member = ctx.author  				
        #await member.add_roles(role)


        teilnehmer = str(glob.glob("tuning_treffen/*"))
        if teilnehmer <= 2:
        await channel1.send('Tut uns leid, das Tuningtreffen kann nicht stattdfinden, da sich zu wenige angemeldet haben. Du kannst dich ab kommenden Montag wieder anmelden.')
        elif teilnehmer > 2 and teilnehmer  <= 6:
        group_1_2 = [discord.utils.get(ctx.guild.roles, id = 798995327117951056), discord.utils.get(ctx.guild.roles, id = 799005988152803348 )]
        group_1_2 = random.choice(group_1_2)
        await member.add_roles(group_1_2)
        elif teilnehmer > 6 and teilnehmer <= 10:
        group_1_2_3 = [discord.utils.get(ctx.guild.roles, id = 798995327117951056), discord.utils.get(ctx.guild.roles, id = 799005988152803348 ), discord.utils.get(ctx.guild.roles, id = 799005990326108210)]
        role = random.choice(group_1_2_3)
        await member.add_roles(role)
        elif teilnehmer > 10 and teilnehmer <= 15:
        4_groups = [discord.utils.get(ctx.guild.roles, id = 798995327117951056), discord.utils.get(ctx.guild.roles, id = 799005988152803348 ), discord.utils.get(ctx.guild.roles, id = 799005990326108210), discord.utils.get(ctx.guild.roles, id = 799005992092041247)]
        role1 = random.choice(4_groups)
        member = teilnehmer
        await member.add_roles(role1)


          #Bis hierhin die die Rollen Verteilung"""
  except Exception as detail:
    await channel1.send("Tuning Treffen Timing konnte nicht gestartet werden. Grund: " + str(detail))

client.run('ODQxNDE4MDU0Njk2NDM1NzQz.YJmdoQ.cIi9KokEWdKykTJDmYX-TvT36qg')