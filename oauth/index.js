const express = require('express');
const { port, token, appId } = require('./config.json');
const path = require('path');
const { fetch } = require('undici');

const app = express();

app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname + '/public')));

app.get('/config/:id', async (request, response) => {
  let configData = await getGuildCommands(request.params.id);
  console.log(configData);
  response.render('config', {
    data: configData
  });
});

const getGuildCommands = async (id) => {
  console.log(id);
  const response = await fetch(`https://discord.com/api/v10/applications/${appId}/commands`, {
    headers: {
      authorization: `Bot ${token}`,
    },
  });
  return response.json();
};


app.listen(port, () => console.log(`App listening at http://localhost:${port}`));
