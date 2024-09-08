import requests, json
from pprint import pprint 
import pandas as pd 
from tqdm.auto import tqdm
tqdm.pandas()

## find players
# find points
# plot trajectories 

pd.set_option('display.max_columns', None)
base_url = 'https://fantasy.premierleague.com/api/'

r = requests.get(base_url+'bootstrap-static/').json() 

players = pd.json_normalize(r['elements'])
teams = pd.json_normalize(r['teams'])
positions = pd.json_normalize(r['element_types'])

df = pd.merge(
    left=players,
    right=teams,
    left_on='team',
    right_on='id'
)

df = df.merge(
    positions,
    left_on='element_type',
    right_on='id'
)


df = df.rename(
    columns={'name':'team_name', 'singular_name':'position_name'}
)


print(df.loc[df['first_name']=='Gabriel'])
 # show joined result
# r = requests.get(base_url + 'element-summary/4/').json()
# print(list(r.keys()))
# # pprint(r['fixtures'])

# def get_gameweek_history(player_id):
#     '''get all gameweek info for a given player_id'''
    
#     # send GET request to
#     # https://fantasy.premierleague.com/api/element-summary/{PID}/
#     r = requests.get(
#             base_url + 'element-summary/' + str(player_id) + '/'
#     ).json()
    
#     # extract 'history' data from response into dataframe
#     df = pd.json_normalize(r['history'])
    
#     return df


# # show player #4's gameweek history
# print(get_gameweek_history(4)[
#     [
#         'round',
#         'total_points',
#         'minutes',
#         'goals_scored',
#         'assists'
#     ]
# ].head())

# def get_season_history(player_id):
#     '''get all past season info for a given player_id'''
    
#     # send GET request to
#     # https://fantasy.premierleague.com/api/element-summary/{PID}/
#     r = requests.get(
#             base_url + 'element-summary/' + str(player_id) + '/'
#     ).json()
    
#     # extract 'history_past' data from response into dataframe
#     df = pd.json_normalize(r['history_past'])
    
#     return df


# # show player #1's gameweek history
# get_season_history(1)[
#     [
#         'season_name',
#         'total_points',
#         'minutes',
#         'goals_scored',
#         'assists'
#     ]
# ].head(10)

# # select columns of interest from players df
# players = players[
#     ['id', 'first_name', 'second_name', 'web_name', 'team',
#      'element_type']
# ]
# positions = pd.json_normalize(r['element_type'])
# # join team name
# players = players.merge(
#     teams[['id', 'name']],
#     left_on='team',
#     right_on='id',
#     suffixes=['_player', None]
# ).drop(['team', 'id'], axis=1)

# # join player positions
# players = players.merge(
#     positions[['id', 'singular_name_short']],
#     left_on='element_type',
#     right_on='id'
# ).drop(['element_type', 'id'], axis=1)

# players.head()


# # get gameweek histories for each player
# points = players['id_player'].progress_apply(get_gameweek_history)

# # combine results into single dataframe
# points = pd.concat(df for df in points)

# # join web_name
# points = players[['id_player', 'web_name']].merge(
#     points,
#     left_on='id_player',
#     right_on='element'
# )

# # get top scoring players
# points.groupby(
#     ['element', 'web_name']
# ).agg(
#     {'total_points':'sum', 'goals_scored':'sum', 'assists':'sum'}
# ).reset_index(
# ).sort_values(
#     'total_points', ascending=False
# ).head()