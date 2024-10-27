import discord
from discord.ext import commands
import random
import asyncio

class UserPhoneCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.call_queue = []  # Queue to hold users waiting for a call
        self.active_calls = {}  # Dictionary to store active call pairs

    @commands.command()
    async def call(self, ctx):
        """Initiates an anonymous call to a random user."""
        user = ctx.author

        # Check if user is already in a call
        if user.id in self.active_calls:
            await ctx.send("📞 You’re already in a call! Use `!end` to end the current call.")
            return

        # Check if there's someone in the queue
        if self.call_queue:
            partner = self.call_queue.pop(0)
            # Establish the call connection
            self.active_calls[user.id] = partner
            self.active_calls[partner.id] = user

            # Notify both users
            await user.send("📞 Connected! You’re now talking to a random user. Type your messages here to chat.")
            await partner.send("📞 Connected! You’re now talking to a random user. Type your messages here to chat.")
        else:
            # Add user to the queue if no one else is waiting
            self.call_queue.append(user)
            await ctx.send("🔍 Looking for someone to connect you with. Hang tight!")

    @commands.command()
    async def end(self, ctx):
        """Ends the current call."""
        user = ctx.author

        # Check if user is in a call
        if user.id not in self.active_calls:
            await ctx.send("🚫 You’re not in a call.")
            return

        # End the call for both users
        partner = self.active_calls[user.id]
        await user.send("📴 You ended the call.")
        await partner.send("📴 The other user ended the call.")

        # Remove users from active calls
        del self.active_calls[user.id]
        del self.active_calls[partner.id]

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore bot messages and non-DM messages
        if message.author.bot or not isinstance(message.channel, discord.DMChannel):
            return

        user = message.author

        # Check if user is in an active call
        if user.id in self.active_calls:
            partner = self.active_calls[user.id]
            # Relay the message to the partner
            await partner.send(f"📞 {message.content}")
        else:
            await message.channel.send("🚫 You’re not in an active call. Use `/call` to start one!")

async def setup(bot):
    await bot.add_cog(UserPhoneCog(bot))
