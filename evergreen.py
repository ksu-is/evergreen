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

# Sprint 2: !next and Some Basic Storyline

# This tracks if there's a prologue in progress. There were issues without this component because anyone in my server was able to use the bot.
active_prologues = {}

# Basic function for the player to type !next
@bot.command(name="next", help="Move forward in the prologue")
async def next(ctx):
    user_id = ctx.author.id

    if user_id not in active_prologues:
        active_prologues[user_id] = {'step': 0}

    step = active_prologues[user_id]['step']
    
    if step == 0:
        await ctx.send(embed=discord.Embed(
            description=(
                "You are in an empty classroom with your friends, Eric and Stacie, working on your computer science project. The room is quiet, and you can hear thunder outside."
            ),
            color=discord.Color.blue()
        ))
        active_prologues[user_id]['step'] += 1
# Dialogue needs steps so players don't receive a full block of text (I had this issue the first time I was creating it).
    elif step == 1:
        await ctx.send(embed=discord.Embed(
            description=(
                "**Eric**: \"We just need to commit the code, and we'll be done.\"\n\n"
                "**Stacie**: \"I can't believe we're still here at 1:00 AM. If we don't get an A, I'll consider dropping out.\""
            ),
            color=discord.Color.green() # Colors are going to represent the level of danger the players have. A scene with no immediate threat will be green, orange, red, etc.
        ))
        active_prologues[user_id]['step'] += 1
    elif step == 2:
        await ctx.send(embed=discord.Embed(
            description=(
                "Suddenly, the lights shut off. You hear footsteps echoing in the hallway.\n\n"
                "**Eric**: \"Did you hear that?\"\n\n"
                "**Stacie**: \"I'm going to check the door.\""
            ),
            color=discord.Color.orange()
        ))
        active_prologues[user_id]['step'] += 1
    elif step == 3:
        await ctx.send(embed=discord.Embed(
            description=(
                "Stacie walks towards the door, and as she opens it slightly, a masked figure lunges at her but misses, blocking the main door.\n\n"
                "What do you want to do?\n\n"
                "**1**: Fight the masked figure\n"
                "**2**: Run out the other door\n"
                "**3**: Slam and barricade the door\n"
                "**4**: Try and hide"
            ),
            color=discord.Color.red()
        ))
        active_prologues[user_id]['step'] += 1

# From here it's pretty much copy and pasting and changing dialogue / making unique messages and interactions for every choice, and although I have a longer dialogue made, I'm probably only going to include a smaller portion.


# I use my unique ID through my Discord account to run the bot with a token (for privacy purposes I will not be putting it in my code, since anybody with the unique token can use it and make a malicious bot).
bot.run('YOUR_BOT_TOKEN')

