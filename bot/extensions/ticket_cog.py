import discord
from discord.ext import commands

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ticket")
    async def ticket(self, ctx):
        category = discord.utils.get(ctx.guild.categories, name="Tickets")
        if not category:
            category = await ctx.guild.create_category("Tickets")

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            ctx.author: discord.PermissionOverwrite(view_channel=True)
        }
        ticket_channel = await ctx.guild.create_text_channel(f"ticket-{ctx.author.name}", category=category, overwrites=overwrites)

        await ticket_channel.send(f"{ctx.author.mention}, your ticket has been created. Please describe your issue here.")

    @commands.command()
    async def closeticket(self, ctx):
        # Ensure the user is in a ticket channel
        if ctx.channel.category.name != "Tickets":
            await ctx.send("You can only use this command in a ticket channel.")
            return

        await ctx.channel.delete()

# Add the cog to your bot
bot = commands.Bot(command_prefix="!")
bot.add_cog(TicketCog(bot))