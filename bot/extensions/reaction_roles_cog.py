import discord
from discord.ext.commands import Cog, Context


class ReactionRolesCog(Cog):
    #get message id
    #on reacting on that message depending on the reaction the memeber will get asgined the coressponding role

    def on_reaction(self, ctx: Context):
        ctx.author.add_roles()
        pass




