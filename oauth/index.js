const express = require('express');
const { port } = require('./config.json');
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
      authorization: `Bot OTk5MzMzMzcyODAxMzI3MTg0.G1BawX.9PzVVwItWH4f8sDvty_JtejSeV_GrFN9HwM8zk`,
    },
  });
  return res.json();

}

app.listen(port, () => console.log(`App listening at http://localhost:${port}`));
