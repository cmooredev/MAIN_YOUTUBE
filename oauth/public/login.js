window.onload = () => {
  const fragment = new URLSearchParams(window.location.hash.slice(1));
  const [accessToken, tokenType] = [fragment.get('access_token'), fragment.get('token_type')];

  if (!accessToken) {
    return (document.getElementById('login').style.display = 'block');
  }

  fetch('https://discord.com/api/users/@me', {
    headers: {
      authorization: `${tokenType} ${accessToken}`,
    },
  })
    .then(result => result.json())
    .then(response => {
      const { username, discriminator, id, avatar } = response;
      document.getElementById('info').innerText = `Hello, ${username}#${discriminator}`;
      /**
      ** Load image from id and avatar(hash)
      **/
      let img = document.createElement('img');
      let src = `https://cdn.discordapp.com/avatars/${id}/${avatar}.png`;
      img.src = src;
      document.body.appendChild(img);
    })
    .catch(console.error);

    fetch('https://discord.com/api/users/@me/guilds', {
      headers: {
        authorization: `${tokenType} ${accessToken}`,
      },
    })
      .then(result => result.json())
      .then(response => {
        let guilds = document.createElement('div');
        guilds.innerText = 'GUILDS';
        document.body.appendChild(guilds);
        for(const guild of response){
          let g = document.createElement('p');
          g.innerText += `${guild.name}`;
          guilds.appendChild(g);
        }

      })
      .catch(console.error);
};
