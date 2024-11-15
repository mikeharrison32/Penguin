from discord.ext.commands.cog import Cog
from discord.ext.commands import hybrid_group, Context
from discord import app_commands
import discord
from discord.ext import commands

class ModerationCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_warnings = {}

    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} for {reason}')

    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for {reason}')

    @commands.command(name='warn', description='Warns a member')
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        guild_id = ctx.guild.id
        user_id = member.id
        reason = reason or "No reason provided"

        # # Initialize warnings for the guild if not already present
        if guild_id not in self.user_warnings:
            self.user_warnings[guild_id] = {}

        # Initialize warnings for the user if not already present
        if user_id not in self.user_warnings[guild_id]:
            self.user_warnings[guild_id][user_id] = []

        # Add the warning
        self.user_warnings[guild_id][user_id].append(reason)

        # Send feedback message
        warning_count = len(self.user_warnings[guild_id][user_id])
        await ctx.send(f'{member.mention} has been warned for {reason}. They now have {warning_count} warning(s).')
   
    @commands.command(name='warnings', description='Lists all warnings for a member')
    @commands.has_permissions(kick_members=True)
    async def warnings(self, ctx, member: discord.Member):
        """Check the number of warnings for a member."""
        guild_id = ctx.guild.id
        user_id = member.id

        # Fetch warnings, or indicate if there are none
        user_warnings = self.user_warnings.get(guild_id, {}).get(user_id, [])
        if user_warnings:
            warnings_text = "\n".join([f"{idx+1}. {warn}" for idx, warn in enumerate(user_warnings)])
            await ctx.send(f'{member.mention} has the following warnings:\n{warnings_text}')
        else:
            await ctx.send(f'{member.mention} has no warnings.')

    @commands.command(name="mute")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mute_role = discord.utils.get(guild.roles, name="Muted")

        if not mute_role:
            mute_role = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False)

        await member.add_roles(mute_role, reason=reason)
        await ctx.send(f'Muted {member.mention} for {reason}')
        

    @commands.command(name="unmute")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mute_role)
        await ctx.send(f'Unmuted {member.mention}')

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        
        embed = discord.Embed(title=f"{member.name}'s Info", description=f"Here is {member.mention}'s info", color=discord.Color.blue())
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Name", value=member.name, inline=True)
        embed.add_field(name="Top Role", value=member.top_role, inline=True)
        embed.add_field(name="Status", value=member.status, inline=True)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        embed.set_thumbnail(url=member.avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
   await bot.add_cog(ModerationCog(bot))