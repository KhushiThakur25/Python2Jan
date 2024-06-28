import urllib.request as url
import json
import cgi

form = cgi.FieldStorage()
player_name = form.getvalue('name')


req = url.urlopen(f"https://api.cricapi.com/v1/players?apikey=8a9ff01d-521c-490d-b826-b6b9e4266a59&offset=0&search={player_name}")

data = json.load(req)
pid = data["data"][0]["id"]

req = url.urlopen(f"https://api.cricapi.com/v1/players_info?apikey=8a9ff01d-521c-490d-b826-b6b9e4266a59&id={pid}")
data = json.load(req)
name=data["data"]['name']
player_image = data["data"]["playerImg"]
print(
f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Player  : {name}</h1>
    <img src={player_image}>    
</body>
</html>
'''
)