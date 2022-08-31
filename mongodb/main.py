import pymongo
import discord
from discord.ext import commands
from discord import app_commands
import asyncio

#NEW
import secrets

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

#--update


@tree.context_menu(name='store', guild=discord.Object(id=997204563612401684))
async def store(interaction: discord.Interaction, message: discord.Message):
    ticket = secrets.token_hex(5)
    db.server_message_log.insert_one(
        {
            "ticket" : ticket,
            "message": message.content,
            "author": message.author.id,
        }
    )

    await interaction.response.send_message("Message stored!")

#--update

# --- NEW

@tree.context_menu(name='findmes', guild=discord.Object(id=997204563612401684))
async def findmes(interaction: discord.Interaction, message: discord.Message):
    author = message.author.id
    key = {'author': author}
    mes = ''
    for m in db.server_message_log.find(key):
        mes = mes + '\n' + m['message']
    print(mes)
    await interaction.response.send_message(f"Messages found!\n{mes}")


# --- NEW

client.run('OTk5MzMzMzcyODAxMzI3MTg0.G4ystb.8ZVAl2HgPzEj7kxgl74CsvZTsubMG2bQLa1UWg')
