import requests, json
from pprint import pprint 
import pandas as pd 


pd.set_option('display.max_columns', None)

base_url = 'https://fantasy.premierleague.com/api/'

r = requests.get(base_url+'bootstrap-static/').json() 

# pprint(r, indent=2, depth=1, compact=True)

players = pd.json_normalize(r['elements'])

p = players[['id', 'web_name', 'team', 'element_type']].head()
teams = pd.json_normalize(r['teams'])

# print(teams.head())

# get position information from 'element_types' field
positions = pd.json_normalize(r['element_types'])

positions.head()

# join players to teams
df = pd.merge(
    left=players,
    right=teams,
    left_on='team',
    right_on='id'
)

# show joined result
r = requests.get(base_url + 'element-summary/4/').json()
print(list(r.keys()))
pprint(r['fixtures'])

