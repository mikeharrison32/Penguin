from discord.ext.commands.cog import Cog
from discord.ext.commands import hybrid_group, Context
from discord.ext import commands
from discord import app_commands
import discord


class BasicCog(Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name="invites")
    async def get_active_invites(self, ctx: Context):
        invites = ctx.guild.invites()
        await ctx.author.send(invites)


async def setup(bot):
    await bot.add_cog(BasicCog(bot))


