import requests

url = 'https://discord.com/api/webhooks/1020517560388689961/FJ8xgYyG0tFdqyMn4tUpKuS6mKBSPEqAyufD5KQwnlS3FowzN8JoCgMb7PYolaKmPKtT'
data = {
    "avatar_url": "https://media.istockphoto.com/vectors/thumb-up-emoticon-vector-id157030584?k=20&m=157030584&s=612x612&w=0&h=TsRUZrgOW19D1f3WMleDrgGL-xfI6g0ZYhJDp58lS0E=",
    "username": "test",
    "content": "Hey this is from inside python.",
    "embeds": [{
    "title": "Hello!",
    "description": "Hi! :grinning:"
    }]
}
x = requests.post(url, json = data)

print(x)
