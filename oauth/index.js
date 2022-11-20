const express = require('express');
const { port, token, appId } = require('./config.json');
const path = require('path');
const { fetch } = require('undici');
const perms = require('./perms');
const bodyParser = require('body-parser');


const jsonParser = bodyParser.json()
const app = express();

app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname + '/public')));

app.post('/config/update/:info', jsonParser, function (request, response) {
  updateCommands(request.body);
});

app.get('/config/:id', async (request, response) => {
  let configData = await getGuildCommands(request.params.id);
  let guild = await getBotGuilds(request.params.id);
  response.render('config', {
    data: configData,
    guild: guild
  });
});

const updateCommands = async (info) => {
  let command = {
    "name": info.name,
    "type": 2
  };
  const response = await fetch(
    `https://discord.com/api/v10/applications/1029120022980857867/commands/${info.id}`,
    {
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bot ${token}`,
        },
        method: "PATCH", //'PUT' -> DELETE'S ALL OTHER COMMANDS AND REPLACES WITH COMMANDS SENT IN BODY
        body: JSON.stringify(command),
    })
      .then(response => {
        console.log(`Command Response: ${response.status}`);
      })
      .catch(console.error);

  return;
};

const getBotGuilds = async (id) => {
  const response = await fetch('https://discord.com/api/users/@me/guilds', {
    headers: {
      authorization: `Bot ${token}`,
    },
  })
  let guilds = await response.json();
  for(let i=0; i < guilds.length; i++) {
    if(guilds[i]['id'] == id) {
      return guilds[i];
    }
  }
  return;
};

const getGuildCommands = async (id) => {
  const response = await fetch(`https://discord.com/api/v10/applications/${appId}/commands`, {
    headers: {
      authorization: `Bot ${token}`,
    },
  });
  return response.json();
};

app.listen(port, () => console.log(`App listening at http://localhost:${port}`));
