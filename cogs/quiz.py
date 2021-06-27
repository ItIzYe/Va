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

class quiz(commands.Cog):
	def __init__(self, client):
		self.client=client

	@commands.command()
	async def quiz(self,ctx):
		quest_a=['Was bedeutet der Name der russischen Raumstation `Mir` ins deutsche übersetzt? \nA) Frieden \nB) Sieg \nC) Raumstation','Wann hat Venom Aimz seinen Yoututbe Kanal gegründet? \n A) 03.03.2020 \n B) 30.02.2020 \n C) 31.06.2020','In welcher Sprache wurde ich geschrieben? \nA) Python \nB) Java \nC) Chinesisch','Von wem wurde der Song Mulberry Street geschrieben? \nA) Twenty one Pilots \nB) Imagine Dragons \nC) Pink Floyd','Welches sind die drei großen monotheistischen Weltreligionen? \nA) Judentum, Islam, Christentum \nB) Judentum, Buddismus, Christentum \nC) Islam, Hinduismus, Atheismus']


		quest_b=['Wer hat den Soundtrack für `Django Unchained` geschrieben? \n A) John Williams \n B) Ennio Morricone \n C) Hans Zimmer','Welches ist der höchste Berg auf unserem Heimatplaneten? \nA) Himalaya \nB) Mount Everest \nC) Olympus Mons','Wann fing der 1. Weltkrieg an? \nA) 1795 \nB) 1914 \nC) 1980','Wieviele kcal hat ein Bic Mac? \nA) 200kcal \nB)503kcal \nC) Stinkstiefel','Wieviele Saiten hat ein Klavier? \nA) 90 \nB) 88 \nC) 70','Was ist AE (AU)? \nA) eine Variabel \nB) Astrononmische Einheit \nC) Gelbanteil in Licht','Vervollständige den Namen der Serie: How I... \nA) ...cooked a Chicken \nB) ...met your Mother \nC) ...fought against Darth Vader','Übersetzte `10001`: \nA) Hallo \nB) 16 \nC) Stift','In welchem Jahr fand der sogenannte "Prager Frühling" statt? \nA) 1966 \nB) 1968 \nC) 1972']

		quest_c=['Wer ist Venom Aimz? \n A) Ein Food-Blogger \n B) Ein Mathematiker \n C) Ein Youtuber','Wann wurden die Beatles gegründet? \nA)1897 \nB) 2001 \nC) 1960','Wie heißt der Ort, der auf der Erde am weitesten von jeglicher Zivilisation entfernt ist? \nA) Olymp \nB) ISS \nC) Point Nemo','Wann ist Bill Clinton Präsident der USA geworden? \nA) 1986 \nB) 1996 \nC) 1992','Wie heißt der neueste amerikanische Marsrover? \nA) Couriosity \nB) Arinane 5 \nC) Perseverance','Wo liegt Alcatraz? \nA) Vor New York \nB) Im Uralgebirge \nC) Vor San Francisco','Wie lang ist ein Geodreieck? \nA) 12cm \nB) 17cm \nC) 14cm']

		next_round=['Willst du weiterspielen?','Noch eine Runde? :)','wenndunocheinerundespielenwillstschreibstdujetztja','Man munkelt du willst nochmal spielen?','Du hast das Ende erreicht....oder doch nicht? In der ferne siehst du ein Netherportal! Machst du dich auf um es zu erunden?','Kevin braucht Hilfe bei einer Matheaufgabe...hilfst du ihm?','Da du keine Hobbys zu haben scheinst wette ich, dass du noch eine Runde spielst']

		comment=['Du hast recht! :tada:','Juhu! Du hast recht :tada:','Du bist wohl ein echter Fanboy :)','Na dass hätte mich gewundert wenn du dass nicht gewusst hättest!','Hast du das studiert?','Arbeitest du für NASA????','Sogar die Sintflut macht vor deinem Wissen halt']

	

		answer_a=['A','a','1']
		answer_b=['B','b','2']
		answer_c=['C','c','3']

		Ja = ['Ja','ja','j','Yes','yes','y']
		Nein = ['Nein','nein','n','no']		

		quest1a = random.choice(quest_a)
		quest1b = random.choice(quest_b)
		quest1c = random.choice(quest_c)

		quest1 = [quest1a, quest1b, quest1c]

		quest1 = random.choice(quest1)

		em=discord.Embed(title='Quiz',description='Hier hast du ein kleines Quiz :)')
		em.add_field(name='Erste Frage:',value= quest1)
		await ctx.send(embed=em)

		msg = await self.client.wait_for("message", check=lambda message: message.author == ctx.author)
		msg = msg.content

		if quest1 in quest_a:
			if msg in answer_a:
				answer = True
			
			else:
				await self.ctx.send('Das war falsch :/')
			
		if quest1 in quest_b:
			if msg in answer_b:
				answer = True
			
			else:
				await self.ctx.send('Das war falsch :/')

		if quest1 in quest_c:
			if msg in answer_c:
				answer = True
			
			else:
				await self.ctx.send('Das war falsch :/')

		if answer == True:
				ctx.send(random.choice(comment))
				ctx.send(random.choice(next_round))

def setup(bot):
	bot.add_cog(quiz(bot))