from discord.ext.commands.cog import Cog
from discord.ext import commands
import discord
import random

class FunCog(Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="hug", description="Give someone a hug!")
    async def hug(self, ctx, member: discord.Member = None): # Set a default value for the member pramter if it was not passed
        hugs = [
            "https://tenor.com/view/hug-warm-hug-depressed-hug-gif-4585064738068342394",
            "https://tenor.com/view/hug-squeeze-cute-cuddle-love-gif-14468054645685403541",
            "https://tenor.com/view/bobitos-mimis-michis-gif-943529865427663588",
        ]

        if member:
            await ctx.send(f"{ctx.author.mention} gives a hug to {member.mention} 🤗 \n {random.choice(hugs)}")
        
        else:
            await ctx.reply("You can't hug air, can't you? 😅, Mention someone you want to hug.")


    @commands.command(name="kiss", description="Send a kiss to someone!")
    async def kiss(self, ctx, member: discord.Member = None):
        kisses = [
            "https://tenor.com/view/kiss-gif-11816971814746635421",
            "https://tenor.com/view/kiss-gif-11242446777802165567",
            "https://tenor.com/view/peach-and-goma-gif-16302490032000255283",
        ]


        if member:
            await ctx.send(f"{ctx.author.mention} gives a sweet kiss to {member.mention} 😘 \n {random.choice(kisses)}")

        else:
            await ctx.reply("You are kissing no one 😅, Mention someone you want to kiss.")



    @commands.command(name="slap", description="Slap someone playfully!")
    async def slap(self, ctx, member: discord.Member = None):
        slaps = [
            "https://tenor.com/view/dungeong-gif-3654754744145897317",
            "https://tenor.com/view/orange-cat-cat-hitting-cat-cat-punching-cat-cat-slapping-cat-orange-cat-hitting-cat-gif-6585435513579432745",
            "https://tenor.com/view/alarm-clock-gif-13113283966983760126",
        ]

        
        if member:
            await ctx.send(f"{ctx.author.mention} slaps {member.mention} \n {random.choice(slaps)}")

        else:
            await ctx.reply("Slapping no one? thats new 🙂, Mention someone you want to SLAP 😈")


    @commands.command(name="kill", description="Pretend to kill someone (all in good fun)!")
    async def kill(self, ctx, member: discord.Member = None):
        kills = [
            "https://tenor.com/view/kill-stab-thinking-arya-got-gif-14033550",
            "https://tenor.com/view/aham-sithi-peace-sithi-sithi-sarker-gif-21717956",
            "https://tenor.com/view/kill-you-chuckie-dog-murder-costume-gif-15089259",
        ]

        if member:
            await ctx.send(f"{ctx.author.mention} kills {member.mention}... in the worst way possible! ☠️ \n  {random.choice(kills)}")
        
        else:
            await ctx.send(f"You want to kill someone in the worst way possible? Mention them! 😈")
            
            
    @commands.command(name='ship')
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member):
        compatibility_score = random.randint(0, 100)
        
        hearts = "❤️" * (compatibility_score // 10)
        empty_hearts = "♡" * (10 - (compatibility_score // 10))
        
        embed = discord.Embed(
            title="💘 Ship Compatibility 💘",
            description=f"**{user1.mention}** and **{user2.mention}** are {compatibility_score}% compatible!",
            color=discord.Color.pink()
        )
        
        embed.add_field(name="Love Meter", value=f"{hearts}{empty_hearts}", inline=False)
        
        if compatibility_score > 80:
            embed.set_footer(text="A match made in heaven! 💞")
        elif compatibility_score > 50:
            embed.set_footer(text="There's some chemistry here! 💫")
        elif compatibility_score > 30:
            embed.set_footer(text="Could work with some effort! 😅")
        else:
            embed.set_footer(text="Hmm... maybe just friends? 👀")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(FunCog(bot))
