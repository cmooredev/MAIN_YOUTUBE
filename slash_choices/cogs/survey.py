import discord
from discord import app_commands
from discord.ext import commands

class Survey(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Survey cog loaded.')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(
          f"Synced {len(fmt)} commands to the current guild."
        )
        return

    @app_commands.command(name="choosecolor", description="color selector")
    #new code
    @app_commands.describe(colors='Colors to choose from')
    @app_commands.choices(colors=[
        discord.app_commands.Choice(name='Red', value=1),
        discord.app_commands.Choice(name='Blue', value=2),
        discord.app_commands.Choice(name='Green', value=3),
    ])
    #end new code
    async def choosecolor(self, interaction: discord.Interaction, colors: discord.app_commands.Choice[int]):
        await interaction.response.send_message('Hey')

async def setup(bot):
    await bot.add_cog(Survey(bot), guilds=[discord.Object(id=997204563612401684)])
