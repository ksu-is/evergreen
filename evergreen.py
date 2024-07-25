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
        color=discord.Color.dark_red() # Colors are going to represent the level of danger the players have. A scene with no immediate threat will be green, orange, red, etc.
    ))
    await ctx.send(embed=discord.Embed(
        description="Type `next` to move forward.",
        color=discord.Color.dark_red()
    ))

# Sprint 2: !next and Some Basic Storyline

# This tracks if there's a prologue in progress. There were issues without this component because anyone in my server was able to use the bot.
active_prologues = {}

import discord
from discord.ext import commands

# Set up intents to receive message content
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready.')

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

@bot.command(name="next", help="Move forward in the prologue")
async def next(ctx):
    await ctx.send(embed=discord.Embed(
        description=(
            "You are in an empty classroom with your friends, Eric and Stacie, working on your computer science project. The room is quiet, and you can hear thunder outside.\n\n"
            "Suddenly, the lights shut off. You hear footsteps echoing in the hallway.\n\n"
            "**Eric**: \"Did you hear that?\"\n\n"
            "**Stacie**: \"I'm going to check the door.\""
        ),
        color=discord.Color.blue()
    ))
    await ctx.send(embed=discord.Embed(
        description=(
            "Stacie walks towards the door. A masked figure lunges at her but misses, blocking the main door.\n\n"
            "What do you want to do?\n\n"
            "**1**: Fight the masked figure\n"
            "**2**: Run out the other door\n"
            "**3**: Slam and barricade the door\n"
            "**4**: Try and hide"
        ),
        color=discord.Color.red()
    ))

# From here it's pretty much copy and pasting and changing dialogue / making unique messages and interactions for every choice, and although I have a longer dialogue made, I'm probably only going to include a smaller portion.

# Sprint 3: Continuing the input/output process, handing number messages, and creating unique feedback for each selection.
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    user_id = message.author.id

    # This handles the choices and immediately leads to game over
    if message.content in ['1', '2', '3', '4']:
        await handle_choice(message.channel, message.author, message.content)
        return  # Ensure that process_commands is not called after handling the choice

    await bot.process_commands(message)

async def handle_choice(channel, user, choice):
    if choice == '1':
        await channel.send(embed=discord.Embed(
            description=(
                "You decide to fight the masked figure, but they overpower you quickly.\n\n"
                "**Game Over**"
            ),
            color=discord.Color.dark_red()
        ))
    elif choice == '2':
        await channel.send(embed=discord.Embed(
            description=(
                "You try to run out the other door, but another masked figure appears and catches you. You can't escape.\n\n"
                "**Game Over**"
            ),
            color=discord.Color.dark_red()
        ))
    elif choice == '3':
        await channel.send(embed=discord.Embed(
            description=(
                "You slam the door shut and try to barricade it, but the figure breaks through and attacks you.\n\n"
                "**Game Over**"
            ),
            color=discord.Color.dark_red()
        ))
    elif choice == '4':
        await channel.send(embed=discord.Embed(
            description=(
                "You try to hide, but the figure finds you quickly. There's no place left to run.\n\n"
                "**Game Over**"
            ),
            color=discord.Color.dark_red()
        ))

                                           
# I use my unique ID through my Discord account to run the bot with a token (for privacy purposes I will not be putting it in my code, since anybody with the unique token can use it and make a malicious bot).
bot.run()

