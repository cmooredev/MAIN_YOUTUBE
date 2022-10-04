const express = require('express');
const { port } = require('./config.json');
const path = require('path');

const app = express();

app.use(express.static(path.join(__dirname + '/public')));

app.get('/', (request, response) => {
  console.log(`The access code is: ${request.query.code}`);
  return response.sendFile('index.html', { root: '.'});
});

app.listen(port, () => console.log(`App listening at http://localhost:${port}`));
