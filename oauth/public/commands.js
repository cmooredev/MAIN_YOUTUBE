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
  console.log(`here is the name ${name.innerText}`);
  let response = await fetch(`http://localhost:53134/config/update/${JSON.stringify(commandOptions)}`)
    .then(response => {
      console.log(response);
    })
    .catch(console.error);
};

window.onload = () => {

};
