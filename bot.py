
import asyncio
import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="=", intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot jest online!")
    
@bot.tree.command(name="ping", description="Wyświetla aktualne opóźnienie bota")
async def ping(interaction: discord.Interaction):
    bot_latency = round(bot.latency * 1000)
    await interaction.response.send_message(
        embed=discord.Embed(description=f"Aktualne opóźnienie bota wynosi `{bot_latency}ms.`", color=discord.Color.from_rgb(47, 49, 54)))

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start("MTA2ODk4MjExNDcyMjI1OTE0NQ.GWJ9k3.XJIDGMmg_XxGf3QYAs7B0TybYCt6LZk0eegRGE")

asyncio.run(main())