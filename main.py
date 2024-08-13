import requests
from config import teamid

print()
team_response = requests.get('https://fantasy.premierleague.com/api/entry/{teamid}/'.format(teamid=teamid))

data = team_response.json()

print(data)  # This will give you all the available data