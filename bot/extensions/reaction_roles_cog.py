import discord
from discord.ext.commands import Cog, Context


class ReactionRolesCog(Cog):
 
    def on_reaction(self, ctx: Context):
        ctx.author.add_roles()
        pass




