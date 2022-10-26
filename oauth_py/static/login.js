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
      guilds.innerText = 'GUILD';
      guilds.classList.add('container');
      document.body.appendChild(guilds);
      for(const guild of response){
        if(guild.owner == true){
          let title =  document.createElement('p');
          let g = document.createElement('a');
          g.href = "/next";
          g.classList.add('card');
          title.innerText += `${guild.name}`;
          if(guild.icon != null){
            let img = document.createElement('img');
            let src = `https://cdn.discordapp.com/icons/${guild.id}/${guild.icon}.png`;
            img.src = src;
            g.appendChild(img);
          }
          guilds.appendChild(title);
          guilds.appendChild(g);


        }
      }
    })
    .catch(console.error);





};
