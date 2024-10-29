import discord
from discord.ext import commands
from loguru import logger
import random
from discord.utils import get

class VentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vent_channel_name = "vent"  

    @discord.app_commands.command()
    async def reply(self, interaction: discord.Interaction, id: int, message: str):
        try:
            await interaction.user.send(f"{message}")
            await interaction.response.send_message("I've sent you a DM 📩", ephemeral=True)  
        except discord.Forbidden:
            await interaction.response.send_message("I can't DM you! Please check your DM settings. 🚫", ephemeral=True)
    
    @discord.app_commands.command()
    async def vent(self, interaction: discord.Interaction, message: str):
        guild = interaction.guild 
        vent_channel = get(guild.text_channels, name=self.vent_channel_name) 
        
       
        colors = [
            0xff5733, 0x33ff57, 0x3357ff, 0xff33a1, 0xffae33, 
            0x8e44ad, 0x3498db, 0xe74c3c, 0x2ecc71, 0xf39c12, 
            0xd35400, 0x1abc9c, 0xc0392b, 0x9b59b6, 0x16a085, 
            0x2980b9, 0xe67e22, 0xf1c40f, 0x7f8c8d, 0x95a5a6
        ]

        if vent_channel:
            embed = discord.Embed(
                description=message,
                color=random.choice(colors)
            )
            embed.set_author(name="Anonymous", icon_url="https://img.freepik.com/premium-photo/illustration-super-cute-kawaii-adorable-sweet-baby-penguin-yel_945369-33938.jpg")
            embed.set_footer(text=f"❗ If this confession is ToS-breaking or overtly hateful, you can report it using /report {str(interaction.id)[-3:]}")

            await vent_channel.send(embed=embed)
            await interaction.response.send_message("✅ Your anonymous message has been sent to the vent channel.", ephemeral=True)
            logger.info("Anonymous message sent to vent channel.")
        else:
            await interaction.response.send_message("❌ Vent channel not found. Please try again later.", ephemeral=True)
            logger.error("Vent channel not found.")

async def setup(bot):
    await bot.add_cog(VentCog(bot))
