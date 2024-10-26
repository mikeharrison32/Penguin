from discord.ext.commands.cog import Cog
from discord.ext import commands
import discord
import random

class FunCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hug", description="Give someone a hug!")
    async def hug(self, ctx, member: discord.Member):
        hugs = [
            "https://tenor.com/view/hug-warm-hug-depressed-hug-gif-4585064738068342394",
            "https://tenor.com/view/hug-squeeze-cute-cuddle-love-gif-14468054645685403541",
            "https://tenor.com/view/bobitos-mimis-michis-gif-943529865427663588",
        ]
        await ctx.send(f"{ctx.author.mention} gives a hug to {member.mention} 🤗 \n {random.choice(hugs)}")

    @commands.command(name="kiss", description="Send a kiss to someone!")
    async def kiss(self, ctx, member: discord.Member):
        kisses = [
            "https://tenor.com/view/kiss-gif-11816971814746635421",
            "https://tenor.com/view/kiss-gif-11242446777802165567",
            "https://tenor.com/view/peach-and-goma-gif-16302490032000255283",
        ]
        await ctx.send(f"{ctx.author.mention} gives a sweet kiss to {member.mention} 😘 \n {random.choice(kisses)}")

    @commands.command(name="slap", description="Slap someone playfully!")
    async def slap(self, ctx, member: discord.Member):
        slaps = [
            "https://tenor.com/view/dungeong-gif-3654754744145897317",
            "https://tenor.com/view/orange-cat-cat-hitting-cat-cat-punching-cat-cat-slapping-cat-orange-cat-hitting-cat-gif-6585435513579432745",
            "https://tenor.com/view/alarm-clock-gif-13113283966983760126",
        ]
        await ctx.send(f"{ctx.author.mention} slaps {member.mention} \n {random.choice(slaps)}")

    @commands.command(name="kill", description="Pretend to kill someone (all in good fun)!")
    async def kill(self, ctx, member: discord.Member):
        kills = [
            "https://tenor.com/view/kill-stab-thinking-arya-got-gif-14033550",
            "https://tenor.com/view/aham-sithi-peace-sithi-sithi-sarker-gif-21717956",
            "https://tenor.com/view/kill-you-chuckie-dog-murder-costume-gif-15089259",
        ]
        await ctx.send(f"{ctx.author.mention} kills {member.mention}... in the worst way possible! ☠️ \n  {random.choice(kills)}")

# Add this cog to your bot setup
async def setup(bot):
    await bot.add_cog(FunCog(bot))
