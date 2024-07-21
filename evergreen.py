# Sprint 1: Bot Setup

import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)

# When loading this up through Visual Studio Code, it basically tells discord the bot is ready.
@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready.')

# After the bot is added to the server, players can use !play to run the game
@bot.command(name="play", help="Start the prologue")
async def play(ctx):
    await ctx.send(embed=discord.Embed(
        title="Prologue: The Dark Night at Evergreen High",
        description=(
            "Welcome to Evergreen High School! Tonight, you will be playing as Devante, "
            "a college student graduating this year. Your classmates, Eric and Stacie, will be joining you, "
            "as you work on a computer science project.\n\n"
            "**Note**: You are temporarily playing as a student for this prologue. Your choices will determine the outcome of this night."
        ),
        color=discord.Color.dark_red()
    ))
    await ctx.send(embed=discord.Embed(
        description="Type `next` to move forward.",
        color=discord.Color.dark_red()
    ))

# I use my unique ID through my Discord account to run the bot with a token (for privacy purposes I will not be putting it in my code, since anybody with the unique token can use it and make a malicious bot).
bot.run('YOUR_BOT_TOKEN')

