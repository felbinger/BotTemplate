import requests

VERSION = 0.1
MORPHEUS_ICON = "https://cdn.discordapp.com/avatars/686299664726622258/cb99c816286bdd1d988ec16d8ae85e15.png"
CONTRIBUTORS = [
]
GITHUB_LINK = "https://github.com/felbinger/bottemplate"
AVATAR_URL = "https://github.com/felbinger.png"
GITHUB_DESCRIPTION = requests.get("https://api.github.com/repos/felbinger/bottemplate").json().get("description")
