const fragment = new URLSearchParams(window.location.hash.slice(1));
const [accessToken, tokenType] = [fragment.get('access_token'), fragment.get('token_type')];

let updateCommand = async (id) => {
  let commandId = id.innerText;
  let name = document.getElementById('command_name');
  let commandName = name.textContent;
  let commandOptions = {
    name: commandName,
    id: commandId,
  }

  const response = await fetch(`http://localhost:53134/config/update/${commandId}`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(commandOptions)
  });
  const content = await response.json();

};

window.onload = () => {

};
