import discord
from discord import app_commands
from discord.ext import commands


async def setup(bot):
        await bot.add_cog(Ogólne(bot))

class Ogólne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['help'])
    async def pomoc(self, ctx):
        embed=discord.Embed(description="**Ogólne** \n`=pomoc` - Wyświetla wszystkie dostępne komendy. \n`=serwer` - Wyświetla informacje o serwerze. \n`=user` - Wyświetla informacje o użytkowniku.", color=discord.Color.from_rgb(47, 49, 54))
        await ctx.send(embed=embed)  
    
    @commands.command(aliases=['serverinfo', 'server'])
    async def serwer(self, ctx, *, user:discord.Member = None):
        if user is None:
            user = ctx.author
        owner = ctx.guild.owner.id
        osoby = (len([member for member in ctx.guild.members if not member.bot]))
        id = ctx.guild.id
        data = ctx.guild.created_at.strftime("%d-%m-%Y")
        embed=discord.Embed(color=discord.Color.from_rgb(47, 49, 54))
        embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon.url)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text=f'Komenda wywołana przez {ctx.author}', icon_url=user.avatar.url)
        embed.add_field(name = '`🆔` ID serwera', value= f'`{id}`', inline=False)
        embed.add_field(name = '`📆` Data utworzenia serwera', value= f'`{data}`', inline=False)
        embed.add_field(name = '`👑` Właściciel serwera', value = f'<@{owner}>', inline=False)
        embed.add_field(name = '`👥` Członkowie', value = f'{osoby}', inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['userinfo', 'whois'])
    async def user(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        id = user.id
        zalo = user.created_at.strftime("%d-%m-%Y")
        dolo = user.joined_at.strftime("%d-%m-%Y")
        embed=discord.Embed(color=discord.Color.from_rgb(47, 49, 54), timestamp=None)
        embed.set_author(name=f"{user}", icon_url=user.avatar.url)
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(text=f'Komenda wywołana przez {ctx.author}', icon_url=ctx.author.avatar.url)
        embed.add_field(name = '`🆔` ID użytkownika', value= f'`{id}`', inline= False)
        embed.add_field(name = '`📌` Data założenia konta', value=f'`{zalo}`', inline= False)
        embed.add_field(name = '`🏡` Data dołączenia na serwer', value=f'`{dolo}`')
        await ctx.send(embed=embed)