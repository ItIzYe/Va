import discord
import random
from discord.ext import commands, tasks
import os
import glob
import asyncio

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True, bans=True,
						  voice_states=True)
client = commands.Bot(command_prefix=['#'], intents=intents)


class tuningtreff(commands.Cog):
	def __init__(self, client):
		self.client = client

	@tasks.loop(hours=27 * 14)
	async def Abstimmung(self):
		channel1 = self.client.get_channel(851183821612777513)
		try:
			await channel1.send("Tuning Treffen Timing wurde gestartet... ")
      
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
			await asyncio.sleep(60*60*24*7)

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
              await channel1.send('Tut uns leid, das Tuningtreffen kann nicht stattdfinden, da sich zu wenige angemeldet haben. Du kannst dich in einer Woche wieder anmelden.')
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

			await asyncio.sleep(60*60*24*7)
		except Exception as detail:
			await channel1.send("Tuning Treffen Timing konnte nicht gestartet werden. Grund: " + str(detail))

	@commands.command(aliases=['start-tt'])
	@commands.has_any_role("Venom Aimz", "Owner", "Admin Leitung", "Admin", "Moderator Leitung",
						   "Chef Developer",
						   "『🤖』Developer", "Tuning Treffen Team")
	async def starten(self, ctx):
		try:
			self.Abstimmung.start()
			return await ctx.send("Tuning Treffen wurde gestartet...")
		except Exception as detail:
			ctx.send("Tuning Treffen konnte nicht gestartet werden! Grund: ", str(detail))

	@commands.command(aliases=["teilnehmen", "Teilnehmen", "TEILNEHMEN"])
	async def tuning_treffen(self, ctx):
		# guild = client.get_guild(714829455826354228)
		# channel2 = self.client.get_channel(851183821612777513)
		if tuningtreffen == True:
			try:

				if os.path.exists("tuning_treffen/%s" % ctx.author):
					await ctx.send("Du bist bereits angemendet... ")

				else:
					t = open("tuning_treffen/%s" % ctx.author, "x")
					t.close()
					await ctx.send("Du wurdest hinzugefügt... ")
			except Exception:
				pass
		else:
			await ctx.send("Die Anmeldung ist gerade nicht geöffnet!")

	@commands.command(aliases=["abmelden", "Abmelden", "ABMELDEN"])
	async def abmeldungfunc(self, ctx):
		# guild = self.client.get_guild(714829455826354228)

		# channel3 = self.client.get_channel(851183821612777513)
		if abmeldung == True:
			try:
				if os.path.exists("tuning_treffen/%s" % ctx.author):
					os.remove("tuning_treffen/%s" % ctx.author)
					await ctx.send("Du wurdest abgemeldet")
				else:
					await ctx.send('Du bist nicht angemeldet. Tippe "#teilnehmen" um dich anzumelden.')
			except Exception:
				pass
		else:
			await ctx.send("Du kannst dich gerade nicht abmelden, weil die Anmeldung gerade geschlossen ist.")

	@commands.command(aliases=['ttlist', 'TTlist', 'TTLIST', 'Ttlist'])
	@commands.has_any_role("Venom Aimz", "Owner", "Admin Leitung", "Admin", "Moderator Leitung",
						   "Chef Developer",
						   "『⚒』Moderator", "『⚜️』Server-Sicherheits-Team", "『🤖』Developer", "『🔨』Test Mod",
						   "『♻️』Team/Supporter", "『♥️』Familie", "『🔰』Test-Team/Supporter",
						   "Tuning Treffen Team")
	async def tt_list(self, ctx):
		a = "tuning_treffen/*"
		await ctx.send(str(glob.glob(a)) + " sind angemeldet")

	@commands.command(aliases=['stop-tt'])
	@commands.has_any_role("Venom Aimz", "Owner", "Admin Leitung", "Admin", "Moderator Leitung",
						   "Chef Developer", "『🤖』Developer", "Tuning Treffen Team")
	async def stop_tt(self, ctx):
		global timing
		timing = False
		global abstimmung
		abstimmung = False
		global tuningtreffen
		tuningtreffen = False
		global abmeldung
		abmeldung = False
		global gerade
		gerade = False
		global ungerade
		ungerade = False
		await ctx.send("Die Tuning Treffen wurden beendet... ")
		self.Abstimmung.cancel()


def setup(bot):
	bot.add_cog(tuningtreff(bot))