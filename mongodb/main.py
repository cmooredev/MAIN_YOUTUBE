import pymongo
import discord
from discord import app_commands
import asyncio

client = pymongo.MongoClient("mongodb+srv://root:toor@cluster0.eswaoor.mongodb.net/?retryWrites=true&w=majority")
db = client.users



print(db)

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await tree.sync(guild = discord.Object(id=997204563612401684))
        print('Online')

client = MyClient(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)


@tree.context_menu(name='hi', guild=discord.Object(id=997204563612401684))
async def translate(interaction: discord.Interaction, message: discord.Message):

    db.server_message_log.insert_one(
        {
            "message": message.content,
            "author": message.author.id,
        }
    )

    await interaction.response.send_message("Hey!")


client.run('OTk5MzMzMzcyODAxMzI3MTg0.Glwouy.HdaB13RvRWTvHLkGgBhUQlXoqePZ12lFJSiq6E')
