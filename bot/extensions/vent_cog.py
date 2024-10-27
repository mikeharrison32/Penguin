import discord
from discord.ext import commands
from loguru import logger
import random
SERVER_ID = 1297835078399033354


class VentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vent_channel_id = 1299737645852921867  # Replace with your actual vent channel ID


    @discord.app_commands.command()
    async def reply(self, interaction: discord.Interaction, id: int, message: str):
        try:
            await interaction.user.send(f"{message}")
            await interaction.response.send_message("I've sent you a DM 📩", ephemeral=True)  
        except discord.Forbidden:
            await interaction.response.send_message("I can't DM you! Please check your DM settings. 🚫", ephemeral=True)
    
    @discord.app_commands.command()
    async def vent(self, interaction: discord.Interaction, message: str):
        guild = self.bot.get_guild(SERVER_ID)  
        vent_channel = guild.get_channel(self.vent_channel_id)
        colors = [
            0xff5733,  # Bright Orange
            0x33ff57,  # Lime Green
            0x3357ff,  # Bright Blue
            0xff33a1,  # Hot Pink
            0xffae33,  # Light Orange
            0x8e44ad,  # Purple
            0x3498db,  # Light Blue
            0xe74c3c,  # Coral Red
            0x2ecc71,  # Emerald Green
            0xf39c12,  # Sunflower Yellow
            0xd35400,  # Pumpkin Orange
            0x1abc9c,  # Turquoise
            0xc0392b,  # Red
            0x9b59b6,  # Amethyst
            0x16a085,  # Greenish Teal
            0x2980b9,  # Strong Blue
            0xe67e22,  # Carrot Orange
            0xf1c40f,  # Bright Yellow
            0x7f8c8d,  # Neutral Gray
            0x95a5a6,  # Lighter Gray
        ]

        
        if vent_channel:
            embed = discord.Embed(
                description=message,
                color=random.choice(colors)
            )
            embed.set_author(name="Anonymous", icon_url="https://img.freepik.com/premium-photo/illustration-super-cute-kawaii-adorable-sweet-baby-penguin-yel_945369-33938.jpg")
            embed.set_footer(text=f"❗ If this confession is ToS-breaking or overtly hateful, you can report it using /report {str(interaction.id)[-3:]}")

            # Send to vent channel and confirm in the user's current context
            await vent_channel.send(embed=embed)
            await interaction.response.send_message("✅ Your anonymous message has been sent to the vent channel.", ephemeral=True)
            logger.info("Anonymous message sent to vent channel.")
        else:
            await interaction.response.send_message("❌ Vent channel not found. Please try again later.", ephemeral=True)
            logger.error("Vent channel not found.")

async def setup(bot):
    await bot.add_cog(VentCog(bot))

