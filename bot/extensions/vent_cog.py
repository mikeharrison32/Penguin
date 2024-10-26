import discord
from discord.ext import commands
from loguru import logger

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
        if isinstance(interaction.channel, discord.DMChannel):
            guild = self.bot.get_guild(SERVER_ID)  
            vent_channel = guild.get_channel(self.vent_channel_id)

            if vent_channel:
                decorated_message = (
                    f"## Anonymous Confession #{str(interaction.id)[-3:]} \n"
                    f">>> {message}\n"
                    f"-# ❗ If this confession is ToS-breaking or overtly hateful, you can report it using **/report {str(interaction.id)[-3:]}** \n"
                    f"-# 💖 To reply and show support you can use **/reply** "
                )
                await vent_channel.send(decorated_message)

                await interaction.response.send_message("✅ Your anonymous message has been sent to the vent channel.", ephemeral=True)
                logger.info("Anonymous message sent to vent channel.")
            else:
                await interaction.response.send_message("❌ Vent channel not found. Please try again later.", ephemeral=True)
                logger.error("Vent channel not found.")
        else:
            await interaction.response.send_message("🚫 This command can only be used in DMs!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(VentCog(bot))

