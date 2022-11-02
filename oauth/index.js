const express = require('express');
const { port, token } = require('./config.json');
const path = require('path');
const { fetch } = require('undici');

const app = express();

app.use(express.static(path.join(__dirname + '/public')));

app.get('/config/:id', async (request, response) => {
  let guild = await getGuild(request.params.id);
  console.log(guild);
  response.send(`${guild.name}`);
});

const getGuild = async (id) => {
  console.log(id);
  const res = await fetch('https://discord.com/api/v10/oauth2/applications/@me', {
    headers: {
      authorization: `Bot ${token}`,
    },
  });
  return res.json();

}

app.listen(port, () => console.log(`App listening at http://localhost:${port}`));
