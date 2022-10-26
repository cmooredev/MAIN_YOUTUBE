import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/next")
def next():
    url = "https://discord.com/api/v10/applications/999333372801327184/guilds/1021424936562217001/commands"

    # This is an example USER command, with a type of 2
    json = {
        "name": "High Five",
        "type": 2
    }

    # For authorization, you can use either your bot token
    headers = {
        "Authorization": "Bot OTk5MzMzMzcyODAxMzI3MTg0.G1BawX.9PzVVwItWH4f8sDvty_JtejSeV_GrFN9HwM8zk"
    }

    r = requests.post(url, headers=headers, json=json)
    print(r.content)
    return r.content
