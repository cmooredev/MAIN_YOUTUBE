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


@tree.context_menu(name='store', guild=discord.Object(id=997204563612401684))
async def store(interaction: discord.Interaction, message: discord.Message):
    author = message.author.id
    key = {'author': message.author.id}

    data = {
        "message": message.content,
        "author": message.author.id,
    }

    user_file = {f'ticket_id.{secrets.token_hex(6)}': data}

    db.server_message_log.update_one(key, {'$set': user_file}, True)

    await interaction.response.send_message("Message stored!")


@tree.context_menu(name='findmes', guild=discord.Object(id=997204563612401684))
async def findmes(interaction: discord.Interaction, message: discord.Message):
    author = message.author.id
    key = {'author': author}
    mes = ''
    m = db.server_message_log.find_one(key)
    for ticket in m['ticket_id']:
        mes = mes + '\n'+ 'ticket_id:' + ticket + '\n' + m['ticket_id'][ticket]['message']


    await interaction.response.send_message(f"Messages found!\n{mes}")



client.run('OTk5MzMzMzcyODAxMzI3MTg0.GoSsa1.iyGjh4JAW9ginwwPz9Es8Fanncq43fvXXyyyOw')
