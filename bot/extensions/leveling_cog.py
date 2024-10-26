from discord.ext import commands
from discord.ext.commands import Cog
import discord
import random
from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')

class LevelingCog(Cog):
    def __init__(self, bot):
        self.bot = bot

        # Connect to MongoDB
        mongo_url = CONNECTION_STRING
        self.client = MongoClient(mongo_url)
        self.db = self.client["leveling_database"]
        self.collection = self.db["user_data"]

    def add_xp(self, user_id, guild_id, xp):
        # Initialize or update user data
        user_data = self.collection.find_one({"user_id": user_id, "guild_id": guild_id})
        if not user_data:
            user_data = {"user_id": user_id, "guild_id": guild_id, "xp": 0, "level": 1}
            self.collection.insert_one(user_data)
        else:
            user_data["xp"] += xp

        # Calculate required XP for leveling up
        required_xp = user_data["level"] * 100
        leveled_up = False

        if user_data["xp"] >= required_xp:
            user_data["level"] += 1
            user_data["xp"] = 0
            leveled_up = True

        # Update user data in MongoDB
        self.collection.update_one(
            {"user_id": user_id, "guild_id": guild_id},
            {"$set": {"xp": user_data["xp"], "level": user_data["level"]}}
        )
        
        return leveled_up

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
                                                                                                                                                                
        xp_gained = random.randint(5, 15)
        leveled_up = self.add_xp(message.author.id, message.guild.id, xp_gained)

        if leveled_up:
            user_level = self.collection.find_one({"user_id": message.author.id, "guild_id": message.guild.id})["level"]
            await message.channel.send(f"🎉 Congrats {message.author.mention}, you've leveled up to level {user_level}!")

    @commands.command(name="rank", description="Check your level and XP.")
    async def rank(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        user_data = self.collection.find_one({"user_id": member.id, "guild_id": ctx.guild.id})

        if not user_data:
            await ctx.send(f"{member.mention} has no XP yet.")
            return

        level = user_data["level"]
        xp = user_data["xp"]
        await ctx.send(f"{member.mention} is at level {level} with {xp} XP!")

# Add this cog to your bot setup
async def setup(bot):
    await bot.add_cog(LevelingCog(bot))
