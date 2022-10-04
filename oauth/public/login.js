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
      const { username, discriminator } = response;
      document.getElementById('info').innerText = `Hello, ${username}#${discriminator}\n`;
    })
    .catch(console.error);
};
