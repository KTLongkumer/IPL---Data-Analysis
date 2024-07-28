#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset
matches_path = 'IPL Matches 2008-2020.csv'  # Ensure the file is in the same directory as this script
matches_data = pd.read_csv(matches_path)

# Extract the 'season' column and count the number of matches per season
matches_per_season = matches_data['date'].apply(lambda x: x.split('-')[0]).value_counts().sort_index()

# Display the count of matches per season
print(matches_per_season)



# In[2]:


import pandas as pd

# Load the datasets
matches_path = 'IPL Matches 2008-2020.csv'
ball_by_ball_path = 'IPL Ball-by-Ball 2008-2020.csv'

matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Extract the season information from the matches dataset
matches_df['season'] = matches_df['date'].apply(lambda x: x.split('-')[0])

# Merge the ball-by-ball data with the season information from the matches data
merged_df = ball_by_ball_df.merge(matches_df[['id', 'season']], left_on='id', right_on='id', how='left')

# Aggregate the total runs scored in each season
runs_per_season = merged_df.groupby('season')['total_runs'].sum().sort_index()

# Display the total runs scored in each season
print(runs_per_season)


# In[3]:


import pandas as pd

# Load the datasets
matches_path = 'IPL Matches 2008-2020.csv'
ball_by_ball_path = 'IPL Ball-by-Ball 2008-2020.csv'

matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Extract the season information from the matches dataset
matches_df['season'] = matches_df['date'].apply(lambda x: x.split('-')[0])

# Merge the ball-by-ball data with the season information from the matches data
merged_df = ball_by_ball_df.merge(matches_df[['id', 'season']], left_on='id', right_on='id', how='left')

# Calculate the total runs for each match
total_runs_per_match = merged_df.groupby('id')['total_runs'].sum().reset_index()

# Merge total runs with season information
total_runs_per_match = total_runs_per_match.merge(matches_df[['id', 'season']], on='id', how='left')

# Calculate the average runs per match for each season
average_runs_per_season = total_runs_per_match.groupby('season')['total_runs'].mean().sort_index()

# Display the average runs per match for each season
print(average_runs_per_season)


# In[4]:


import pandas as pd

# Load the dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Combine umpire1 and umpire2 columns to count total matches officiated
umpire1_counts = matches_df['umpire1'].value_counts()
umpire2_counts = matches_df['umpire2'].value_counts()

# Combine both counts
total_umpire_counts = umpire1_counts.add(umpire2_counts, fill_value=0).sort_values(ascending=False)

# Display the umpire with the most matches officiated
most_umpired = total_umpire_counts.head(1)
print(most_umpired)


# In[5]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Count the number of times each team has won the toss
toss_winner_counts = matches_df['toss_winner'].value_counts()

# Display the team that has won the most tosses
print(toss_winner_counts.head(10))


# In[6]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Count the number of times each decision is made after winning the toss
toss_decision_counts = matches_df.groupby('toss_winner')['toss_decision'].value_counts().unstack().fillna(0)

# Display the decisions made by teams after winning the toss
print(toss_decision_counts)


# In[7]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Extract the season information
matches_df['season'] = matches_df['date'].apply(lambda x: x.split('-')[0])

# Count the number of times each decision is made after winning the toss for each season
toss_decision_season_counts = matches_df.groupby('season')['toss_decision'].value_counts().unstack().fillna(0)

# Display the decisions made by teams after winning the toss across seasons
print(toss_decision_season_counts)


# In[8]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Create a new column to indicate if the toss winner is the same as the match winner
matches_df['toss_winner_is_match_winner'] = matches_df['toss_winner'] == matches_df['winner']

# Calculate the number of matches won by the toss winner and the team that lost the toss
toss_impact = matches_df['toss_winner_is_match_winner'].value_counts(normalize=True) * 100

# Display the results
print(toss_impact)


# In[9]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Identify the team that batted second
matches_df['team_batting_second'] = matches_df.apply(lambda row: row['team2'] if row['toss_decision'] == 'bat' else row['team1'], axis=1)

# Compare the match winner with the team that batted second
matches_df['chasing_team_won'] = matches_df['winner'] == matches_df['team_batting_second']

# Count the number of times the chasing team won the match
chasing_team_wins = matches_df['chasing_team_won'].sum()

# Display the result
print(f'The chasing team won {chasing_team_wins} matches.')


# In[10]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Extract the season information
matches_df['season'] = matches_df['date'].apply(lambda x: x.split('-')[0])

# Identify the final match of each season
final_matches = matches_df[matches_df['season'].isin(matches_df['season'].unique()) & matches_df['date'].apply(lambda x: x.endswith('05-30') or x.endswith('05-31'))]

# Extract the winners of the final matches
tournament_winners = final_matches[['season', 'winner']].drop_duplicates().sort_values(by='season')

# Display the tournament winners
print(tournament_winners)


# In[11]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Count the number of matches played by each team as 'team1'
team1_counts = matches_df['team1'].value_counts()

# Count the number of matches played by each team as 'team2'
team2_counts = matches_df['team2'].value_counts()

# Sum the counts to get the total number of matches played by each team
total_matches_played = team1_counts.add(team2_counts, fill_value=0).sort_values(ascending=False)

# Display the team that has played the most matches
print(total_matches_played.head(10))


# In[12]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Count the number of matches won by each team
matches_won_counts = matches_df['winner'].value_counts()

# Display the team that has won the most matches
print(matches_won_counts.head(10))


# In[13]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Count the number of matches played by each team as 'team1'
team1_counts = matches_df['team1'].value_counts()

# Count the number of matches played by each team as 'team2'
team2_counts = matches_df['team2'].value_counts()

# Sum the counts to get the total number of matches played by each team
total_matches_played = team1_counts.add(team2_counts, fill_value=0)

# Count the number of matches won by each team
matches_won_counts = matches_df['winner'].value_counts()

# Calculate the winning percentage for each team
winning_percentage = (matches_won_counts / total_matches_played) * 100

# Sort the winning percentages in descending order
winning_percentage = winning_percentage.sort_values(ascending=False)

# Display the teams with the highest winning percentage
print(winning_percentage.head(10))


# In[14]:


import pandas as pd

# Load the matches dataset
matches_path = 'IPL Matches 2008-2020.csv'
matches_df = pd.read_csv(matches_path)

# Count the number of matches played by each team at each venue
matches_played_at_venue = matches_df.groupby(['venue', 'team1']).size().add(
    matches_df.groupby(['venue', 'team2']).size(), fill_value=0).reset_index(name='matches_played')

# Count the number of matches won by each team at each venue
matches_won_at_venue = matches_df[matches_df['winner'].notna()].groupby(['venue', 'winner']).size().reset_index(name='matches_won')

# Merge the dataframes to calculate winning percentage
venue_stats = pd.merge(matches_played_at_venue, matches_won_at_venue, left_on=['venue', 'team1'], right_on=['venue', 'winner'], how='left').fillna(0)

# Calculate the winning percentage
venue_stats['winning_percentage'] = (venue_stats['matches_won'] / venue_stats['matches_played']) * 100

# Find the venues where each team has the highest winning percentage
lucky_venues = venue_stats.sort_values(by=['team1', 'winning_percentage'], ascending=[True, False]).drop_duplicates(subset=['team1'])

# Display the results
print(lucky_venues[['team1', 'venue', 'winning_percentage']])


# In[15]:


import pandas as pd

# Load the datasets
matches_path = 'IPL Matches 2008-2020.csv'
ball_by_ball_path = 'IPL Ball-by-Ball 2008-2020.csv'
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Merge the matches dataset with ball-by-ball dataset to get team information
merged_df = ball_by_ball_df.merge(matches_df[['id', 'team1', 'team2']], left_on='id', right_on='id', how='left')

# Create a new column to indicate the batting team for each ball
merged_df['batting_team'] = merged_df.apply(lambda row: row['team1'] if row['inning'] % 2 != 0 else row['team2'], axis=1)

# Calculate total runs scored in each innings for each match
innings_runs = merged_df.groupby(['id', 'inning', 'batting_team'])['total_runs'].sum().reset_index()

# Calculate the number of wickets lost in each innings for each match
# Exclude non-wicket deliveries (such as extras)
wickets = merged_df[merged_df['dismissal_kind'].notna()]
innings_wickets = wickets.groupby(['id', 'inning', 'batting_team']).size().reset_index(name='wickets')

# Merge the runs and wickets dataframes
innings_stats = pd.merge(innings_runs, innings_wickets, on=['id', 'inning', 'batting_team'], how='left').fillna(0)

# Summarize the statistics by team
team_stats = innings_stats.groupby('batting_team').agg({
    'total_runs': ['sum', 'mean', 'median'],
    'wickets': ['sum', 'mean', 'median']
}).reset_index()

# Flatten the multi-level columns
team_stats.columns = ['batting_team', 'total_runs_sum', 'total_runs_mean', 'total_runs_median', 'wickets_sum', 'wickets_mean', 'wickets_median']

# Display the team-wise summary statistics
print(team_stats)


# In[16]:


import pandas as pd

# Load the datasets
matches_path = 'IPL Matches 2008-2020.csv'
ball_by_ball_path = 'IPL Ball-by-Ball 2008-2020.csv'
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Merge the matches dataset with ball-by-ball dataset to get team information
merged_df = ball_by_ball_df.merge(matches_df[['id', 'team1', 'team2']], left_on='id', right_on='id', how='left')

# Create a new column to indicate the batting team for each ball
merged_df['batting_team'] = merged_df.apply(lambda row: row['team1'] if row['inning'] % 2 != 0 else row['team2'], axis=1)

# Calculate total runs scored in each innings for each match
innings_runs = merged_df.groupby(['id', 'inning', 'batting_team'])['total_runs'].sum().reset_index()

# Filter the innings where the total runs are 200 or more
high_scores = innings_runs[innings_runs['total_runs'] >= 200]

# Count the number of 200+ scores for each team
team_high_scores = high_scores['batting_team'].value_counts().reset_index()
team_high_scores.columns = ['team', '200+ scores']

# Display the team with the most number of 200+ scores
print(team_high_scores)


# In[17]:


import pandas as pd

# Load the datasets
matches_path = 'IPL Matches 2008-2020.csv'
ball_by_ball_path = 'IPL Ball-by-Ball 2008-2020.csv'
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Merge the matches dataset with ball-by-ball dataset to get team information
merged_df = ball_by_ball_df.merge(matches_df[['id', 'team1', 'team2']], left_on='id', right_on='id', how='left')

# Create a new column to indicate the bowling team for each ball
merged_df['bowling_team'] = merged_df.apply(lambda row: row['team2'] if row['inning'] % 2 != 0 else row['team1'], axis=1)

# Calculate total runs scored in each innings for each match
innings_runs = merged_df.groupby(['id', 'inning', 'bowling_team'])['total_runs'].sum().reset_index()

# Filter the innings where the total runs are 200 or more
high_scores_conceded = innings_runs[innings_runs['total_runs'] >= 200]

# Count the number of 200+ scores conceded for each team
team_high_scores_conceded = high_scores_conceded['bowling_team'].value_counts().reset_index()
team_high_scores_conceded.columns = ['team', '200+ scores conceded']

# Display the team with the most number of 200+ scores conceded
print(team_high_scores_conceded)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


import os

# List the files in the current working directory
current_directory = os.getcwd()
file_list = os.listdir(current_directory)
print(f"Current Directory: {current_directory}")
print("Files in current directory:")
print(file_list)


# In[19]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Display the first few rows of each dataframe to confirm successful loading
print("Matches DataFrame:")
print(matches_df.head())

print("\nBall-by-Ball DataFrame:")
print(ball_by_ball_df.head())


# In[ ]:





# In[20]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Display the first few rows of each dataframe to confirm successful loading
print("Matches DataFrame:")
print(matches_df.head())

print("\nBall-by-Ball DataFrame:")
print(ball_by_ball_df.head())

# Group the ball-by-ball data by id and batting team, then sum up the runs scored
runs_scored = ball_by_ball_df.groupby(['id', 'batting_team'])['total_runs'].sum().reset_index()

# Find the highest run scored by a team in a single match
highest_run = runs_scored.loc[runs_scored['total_runs'].idxmax()]

print("\nHighest run scored by a team in a single match:")
print(highest_run)


# In[21]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'

# Load the dataset
matches_df = pd.read_csv(matches_path)

# Filter matches won by runs and find the match with the maximum run margin
biggest_win = matches_df[matches_df['result'] == 'runs'].loc[matches_df['result_margin'].idxmax()]

print("Biggest win in terms of run margin:")
print(biggest_win)


# In[22]:


import pandas as pd

# File paths
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the dataset
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Group by batsman and count the number of balls faced
balls_faced = ball_by_ball_df.groupby('batsman')['ball'].count().reset_index()

# Rename the columns for clarity
balls_faced.columns = ['batsman', 'balls_faced']

# Sort the dataframe by balls faced in descending order
balls_faced = balls_faced.sort_values(by='balls_faced', ascending=False)

# Display the top batsmen who have played the most number of balls
print("Batsmen who have played the most number of balls:")
print(balls_faced.head(10))


# In[23]:


import pandas as pd

# File paths
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the dataset
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Group by batsman and sum the total runs scored
total_runs = ball_by_ball_df.groupby('batsman')['batsman_runs'].sum().reset_index()

# Rename the columns for clarity
total_runs.columns = ['batsman', 'total_runs']

# Sort the dataframe by total runs in descending order
total_runs = total_runs.sort_values(by='total_runs', ascending=False)

# Display the top batsmen who have scored the most runs
print("Leading run-scorers of all time in the IPL:")
print(total_runs.head(10))


# In[24]:


import pandas as pd

# File paths
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the dataset
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Filter for deliveries that resulted in fours
fours = ball_by_ball_df[ball_by_ball_df['batsman_runs'] == 4]

# Group by batsman and count the number of fours
fours_count = fours.groupby('batsman')['batsman_runs'].count().reset_index()

# Rename the columns for clarity
fours_count.columns = ['batsman', 'number_of_fours']

# Sort the dataframe by number of fours in descending order
fours_count = fours_count.sort_values(by='number_of_fours', ascending=False)

# Display the top batsmen who have hit the most number of fours
print("Batsmen who have hit the most number of fours in the IPL:")
print(fours_count.head(10))


# In[25]:


import pandas as pd

# File paths
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the dataset
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Filter for deliveries that resulted in sixes
sixes = ball_by_ball_df[ball_by_ball_df['batsman_runs'] == 6]

# Group by batsman and count the number of sixes
sixes_count = sixes.groupby('batsman')['batsman_runs'].count().reset_index()

# Rename the columns for clarity
sixes_count.columns = ['batsman', 'number_of_sixes']

# Sort the dataframe by number of sixes in descending order
sixes_count = sixes_count.sort_values(by='number_of_sixes', ascending=False)

# Display the top batsmen who have hit the most number of sixes
print("Batsmen who have hit the most number of sixes in the IPL:")
print(sixes_count.head(10))


# In[26]:


import pandas as pd

# File paths
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the dataset
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Group by batsman and sum the total runs and count the number of balls faced
batsman_stats = ball_by_ball_df.groupby('batsman').agg({
    'batsman_runs': 'sum',
    'ball': 'count'
}).reset_index()

# Calculate the strike rate
batsman_stats['strike_rate'] = (batsman_stats['batsman_runs'] / batsman_stats['ball']) * 100

# Sort the dataframe by strike rate in descending order
batsman_stats = batsman_stats.sort_values(by='strike_rate', ascending=False)

# Display the batsmen with the highest strike rate
print("Batsmen with the highest strike rate in the IPL:")
print(batsman_stats.head(10))


# In[27]:


import pandas as pd

# File paths
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the dataset
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Filter for deliveries that resulted in a wicket
wickets = ball_by_ball_df[ball_by_ball_df['is_wicket'] == 1]

# Group by bowler and count the number of wickets
wickets_count = wickets.groupby('bowler')['is_wicket'].count().reset_index()

# Rename the columns for clarity
wickets_count.columns = ['bowler', 'wickets']

# Sort the dataframe by number of wickets in descending order
wickets_count = wickets_count.sort_values(by='wickets', ascending=False)

# Display the top bowlers who have taken the most number of wickets
print("Leading wicket-takers in the IPL:")
print(wickets_count.head(10))


# In[28]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'

# Load the dataset
matches_df = pd.read_csv(matches_path)

# Group by venue and count the number of matches
venue_count = matches_df.groupby('venue')['id'].count().reset_index()

# Rename the columns for clarity
venue_count.columns = ['venue', 'number_of_matches']

# Sort the dataframe by number of matches in descending order
venue_count = venue_count.sort_values(by='number_of_matches', ascending=False)

# Display the stadiums that have hosted the most number of matches
print("Stadiums that have hosted the most number of matches in the IPL:")
print(venue_count.head(10))


# In[29]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'

# Load the dataset
matches_df = pd.read_csv(matches_path)

# Group by player_of_match and count the number of awards
mom_count = matches_df.groupby('player_of_match')['id'].count().reset_index()

# Rename the columns for clarity
mom_count.columns = ['player_of_match', 'number_of_awards']

# Sort the dataframe by number of awards in descending order
mom_count = mom_count.sort_values(by='number_of_awards', ascending=False)

# Display the players with the most MOM awards
print("Players with the most MOM awards in the IPL:")
print(mom_count.head(10))


# In[30]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Merge ball-by-ball data with matches data to get the season information
merged_df = pd.merge(ball_by_ball_df, matches_df, on='id')

# Extract the year from the date column to identify the season
merged_df['season'] = pd.to_datetime(merged_df['date']).dt.year

# Filter for deliveries that resulted in fours
fours = merged_df[merged_df['batsman_runs'] == 4]

# Group by season and count the number of fours
fours_count_per_season = fours.groupby('season')['batsman_runs'].count().reset_index()

# Rename the columns for clarity
fours_count_per_season.columns = ['season', 'number_of_fours']

# Sort the dataframe by season
fours_count_per_season = fours_count_per_season.sort_values(by='season')

# Display the count of fours hit in each season
print("Count of fours hit in each IPL season:")
print(fours_count_per_season)


# In[31]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Merge ball-by-ball data with matches data to get the season information
merged_df = pd.merge(ball_by_ball_df, matches_df, on='id')

# Extract the year from the date column to identify the season
merged_df['season'] = pd.to_datetime(merged_df['date']).dt.year

# Filter for deliveries that resulted in sixes
sixes = merged_df[merged_df['batsman_runs'] == 6]

# Group by season and count the number of sixes
sixes_count_per_season = sixes.groupby('season')['batsman_runs'].count().reset_index()

# Rename the columns for clarity
sixes_count_per_season.columns = ['season', 'number_of_sixes']

# Sort the dataframe by season
sixes_count_per_season = sixes_count_per_season.sort_values(by='season')

# Display the count of sixes hit in each season
print("Count of sixes hit in each IPL season:")
print(sixes_count_per_season)


# In[32]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Merge ball-by-ball data with matches data to get the season information
merged_df = pd.merge(ball_by_ball_df, matches_df, on='id')

# Extract the year from the date column to identify the season
merged_df['season'] = pd.to_datetime(merged_df['date']).dt.year

# Filter for deliveries that resulted in fours or sixes
boundaries = merged_df[merged_df['batsman_runs'].isin([4, 6])]

# Calculate the total runs from boundaries in each season
boundary_runs_per_season = boundaries.groupby('season')['batsman_runs'].sum().reset_index()

# Rename the columns for clarity
boundary_runs_per_season.columns = ['season', 'boundary_runs']

# Sort the dataframe by season
boundary_runs_per_season = boundary_runs_per_season.sort_values(by='season')

# Display the count of runs scored from boundaries in each season
print("Count of runs scored from boundaries in each IPL season:")
print(boundary_runs_per_season)


# In[33]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Merge ball-by-ball data with matches data to get the season information
merged_df = pd.merge(ball_by_ball_df, matches_df, on='id')

# Extract the year from the date column to identify the season
merged_df['season'] = pd.to_datetime(merged_df['date']).dt.year

# Calculate the total runs scored in each season
total_runs_per_season = merged_df.groupby('season')['total_runs'].sum().reset_index()

# Filter for deliveries that resulted in fours or sixes
boundaries = merged_df[merged_df['batsman_runs'].isin([4, 6])]

# Calculate the total runs from boundaries in each season
boundary_runs_per_season = boundaries.groupby('season')['batsman_runs'].sum().reset_index()

# Rename the columns for clarity
total_runs_per_season.columns = ['season', 'total_runs']
boundary_runs_per_season.columns = ['season', 'boundary_runs']

# Merge the total runs and boundary runs dataframes
runs_contribution_df = pd.merge(total_runs_per_season, boundary_runs_per_season, on='season')

# Calculate the percentage contribution of boundary runs to the total runs
runs_contribution_df['boundary_runs_percentage'] = (runs_contribution_df['boundary_runs'] / runs_contribution_df['total_runs']) * 100

# Sort the dataframe by season
runs_contribution_df = runs_contribution_df.sort_values(by='season')

# Display the run contribution from boundaries in each season
print("Run contribution from boundaries in each IPL season:")
print(runs_contribution_df)


# In[34]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Filter for the first 6 overs of each inning
powerplay_overs = ball_by_ball_df[ball_by_ball_df['over'] <= 6]

# Group the data by match_id and batting_team, then sum up the runs scored
powerplay_runs = powerplay_overs.groupby(['id', 'batting_team'])['total_runs'].sum().reset_index()

# Find the team with the highest total runs scored in the first 6 overs across all matches
most_runs_powerplay = powerplay_runs.groupby('batting_team')['total_runs'].sum().reset_index()

# Sort the dataframe by total runs in descending order
most_runs_powerplay = most_runs_powerplay.sort_values(by='total_runs', ascending=False)

# Display the team with the most runs scored in the first 6 overs
print("Teams with the most runs scored in the first 6 overs:")
print(most_runs_powerplay)


# In[35]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Assuming IPL matches have a maximum of 20 overs, filter for the last 4 overs (i.e., overs 17 to 20)
death_overs = ball_by_ball_df[ball_by_ball_df['over'] >= 17]

# Group the data by match_id and batting_team, then sum up the runs scored in the last 4 overs
death_over_runs = death_overs.groupby(['id', 'batting_team'])['total_runs'].sum().reset_index()

# Find the team with the highest total runs scored in the last 4 overs across all matches
most_runs_death_overs = death_over_runs.groupby('batting_team')['total_runs'].sum().reset_index()

# Sort the dataframe by total runs in descending order
most_runs_death_overs = most_runs_death_overs.sort_values(by='total_runs', ascending=False)

# Display the team with the most runs scored in the last 4 overs
print("Teams with the most runs scored in the last 4 overs:")
print(most_runs_death_overs)


# In[36]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Filter for the first 6 overs of each inning
powerplay_overs = ball_by_ball_df[ball_by_ball_df['over'] <= 6]

# Group the data by match_id and batting_team, then sum up the runs scored and count the number of balls faced
powerplay_stats = powerplay_overs.groupby(['id', 'batting_team']).agg({'total_runs': 'sum', 'ball': 'count'}).reset_index()

# Calculate the total balls faced in the first 6 overs
powerplay_stats['total_overs'] = powerplay_stats['ball'] / 6

# Calculate the run rate for each match in the first 6 overs
powerplay_stats['run_rate'] = powerplay_stats['total_runs'] / powerplay_stats['total_overs']

# Calculate the average run rate for each team
average_run_rate = powerplay_stats.groupby('batting_team')['run_rate'].mean().reset_index()

# Sort the dataframe by run rate in descending order
average_run_rate = average_run_rate.sort_values(by='run_rate', ascending=False)

# Display the team with the best scoring run rate in the first 6 overs
print("Teams with the best scoring run rate in the first 6 overs:")
print(average_run_rate)


# In[37]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Assuming IPL matches have a maximum of 20 overs, filter for the last 4 overs (i.e., overs 17 to 20)
death_overs = ball_by_ball_df[ball_by_ball_df['over'] >= 17]

# Group the data by match_id and batting_team, then sum up the runs scored and count the number of balls faced
death_over_stats = death_overs.groupby(['id', 'batting_team']).agg({'total_runs': 'sum', 'ball': 'count'}).reset_index()

# Calculate the total overs faced in the last 4 overs
death_over_stats['total_overs'] = death_over_stats['ball'] / 6

# Calculate the run rate for each match in the last 4 overs
death_over_stats['run_rate'] = death_over_stats['total_runs'] / death_over_stats['total_overs']

# Calculate the average run rate for each team
average_run_rate = death_over_stats.groupby('batting_team')['run_rate'].mean().reset_index()

# Sort the dataframe by run rate in descending order
average_run_rate = average_run_rate.sort_values(by='run_rate', ascending=False)

# Display the team with the best scoring run rate in the last 4 overs
print("Teams with the best scoring run rate in the last 4 overs:")
print(average_run_rate)


# In[38]:


import pandas as pd

# File paths
matches_path = './IPL Matches 2008-2020.csv'
ball_by_ball_path = './IPL Ball-by-Ball 2008-2020.csv'

# Load the datasets
matches_df = pd.read_csv(matches_path)
ball_by_ball_df = pd.read_csv(ball_by_ball_path)

# Display the columns in the matches_df to ensure correct column names
print("Columns in Matches DataFrame:")
print(matches_df.columns)

# Extract the season from the date column
matches_df['season'] = pd.to_datetime(matches_df['date']).dt.year

# Perform analysis only if the required columns are present
if 'result_margin' in matches_df.columns and 'winner' in matches_df.columns:
    # 1. Highest Run Scored by a Team in a Single Match
    highest_run = matches_df.loc[matches_df['result_margin'].idxmax()]
    print(f"Highest run scored by a team in a single match: {highest_run['result_margin']} by {highest_run['winner']}")
    
    # 2. Biggest Win in Terms of Run Margin
    biggest_win = matches_df.loc[matches_df['result_margin'].idxmax()]
    print(f"Biggest win in terms of run margin: {biggest_win['result_margin']} runs by {biggest_win['winner']}")
else:
    print("Required columns 'result_margin' or 'winner' not found in the matches DataFrame.")

# 3. Batsmen with Most Balls Faced
most_balls_faced = ball_by_ball_df.groupby('batsman')['ball'].count().idxmax()
print(f"Batsman with the most number of balls faced: {most_balls_faced}")

# 4. Leading Run-Scorers of All Time
leading_run_scorer = ball_by_ball_df.groupby('batsman')['batsman_runs'].sum().idxmax()
print(f"Leading run-scorer of all time: {leading_run_scorer}")

# 5. Most Number of Fours Hit
most_fours = ball_by_ball_df[ball_by_ball_df['batsman_runs'] == 4].groupby('batsman')['batsman_runs'].count().idxmax()
print(f"Batsman with the most number of fours: {most_fours}")

# 6. Most Number of Sixes Hit
most_sixes = ball_by_ball_df[ball_by_ball_df['batsman_runs'] == 6].groupby('batsman')['batsman_runs'].count().idxmax()
print(f"Batsman with the most number of sixes: {most_sixes}")

# 7. Highest Strike Rate
batsman_stats = ball_by_ball_df.groupby('batsman').agg({'ball': 'count', 'batsman_runs': 'sum'}).reset_index()
batsman_stats['strike_rate'] = (batsman_stats['batsman_runs'] / batsman_stats['ball']) * 100
highest_strike_rate = batsman_stats.sort_values(by='strike_rate', ascending=False).iloc[0]
print(f"Batsman with the highest strike rate: {highest_strike_rate['batsman']} with a strike rate of {highest_strike_rate['strike_rate']}")

# 8. Leading Wicket-Taker
leading_wicket_taker = ball_by_ball_df[ball_by_ball_df['is_wicket'] == 1].groupby('bowler')['is_wicket'].count().idxmax()
print(f"Leading wicket-taker of all time: {leading_wicket_taker}")

# 9. Stadium with Most Matches Hosted
most_matches_hosted = matches_df['venue'].value_counts().idxmax()
print(f"Stadium with most matches hosted: {most_matches_hosted}")

# 10. Most Man of the Match Awards
most_mom_awards = matches_df['player_of_match'].value_counts().idxmax()
print(f"Player with the most Man of the Match awards: {most_mom_awards}")

# 11. Count of Fours Hit in Each Season
merged_df = ball_by_ball_df.merge(matches_df[['id', 'season']], left_on='id', right_on='id')
fours = merged_df[merged_df['batsman_runs'] == 4]
fours_count_per_season = fours.groupby('season')['batsman_runs'].count().reset_index()
fours_count_per_season.columns = ['season', 'number_of_fours']
print("Count of fours hit in each season:")
print(fours_count_per_season)

# 12. Count of Sixes Hit in Each Season
sixes = merged_df[merged_df['batsman_runs'] == 6]
sixes_count_per_season = sixes.groupby('season')['batsman_runs'].count().reset_index()
sixes_count_per_season.columns = ['season', 'number_of_sixes']
print("Count of sixes hit in each season:")
print(sixes_count_per_season)

# 13. Runs Scored from Boundaries in Each Season
boundaries = merged_df[merged_df['batsman_runs'].isin([4, 6])]
boundary_runs_per_season = boundaries.groupby('season')['batsman_runs'].sum().reset_index()
boundary_runs_per_season.columns = ['season', 'runs_from_boundaries']
print("Runs scored from boundaries in each season:")
print(boundary_runs_per_season)

# 14. Run Contribution from Boundaries in Each Season
total_runs_per_season = merged_df.groupby('season')['total_runs'].sum().reset_index()
run_contribution_from_boundaries = pd.merge(total_runs_per_season, boundary_runs_per_season, on='season')
run_contribution_from_boundaries['boundary_contribution_percentage'] = (run_contribution_from_boundaries['runs_from_boundaries'] / run_contribution_from_boundaries['total_runs']) * 100
print("Run contribution from boundaries in each season:")
print(run_contribution_from_boundaries)

# 15. Team with Most Runs in First 6 Overs
powerplay_runs = ball_by_ball_df[ball_by_ball_df['over'] <= 6]
powerplay_runs_team = powerplay_runs.groupby('batting_team')['total_runs'].sum().idxmax()
print(f"Team with the most runs in the first 6 overs: {powerplay_runs_team}")

# 16. Team with Most Runs in Last 4 Overs
death_overs = ball_by_ball_df[ball_by_ball_df['over'] >= 17]
death_overs_runs_team = death_overs.groupby('batting_team')['total_runs'].sum().idxmax()
print(f"Team with the most runs in the last 4 overs: {death_overs_runs_team}")

# 17. Best Scoring Run Rate in First 6 Overs
powerplay_stats = powerplay_runs.groupby('batting_team').agg({'total_runs': 'sum', 'ball': 'count'}).reset_index()
powerplay_stats['total_overs'] = powerplay_stats['ball'] / 6
powerplay_stats['run_rate'] = powerplay_stats['total_runs'] / powerplay_stats['total_overs']
best_powerplay_run_rate_team = powerplay_stats.sort_values(by='run_rate', ascending=False).iloc[0]
print(f"Team with the best scoring run rate in the first 6 overs: {best_powerplay_run_rate_team['batting_team']} with a run rate of {best_powerplay_run_rate_team['run_rate']}")

# 18. Best Scoring Run Rate in Last 4 Overs
death_overs_stats = death_overs.groupby('batting_team').agg({'total_runs': 'sum', 'ball': 'count'}).reset_index()
death_overs_stats['total_overs'] = death_overs_stats['ball'] / 6
death_overs_stats['run_rate'] = death_overs_stats['total_runs'] / death_overs_stats['total_overs']
best_death_overs_run_rate_team = death_overs_stats.sort_values(by='run_rate', ascending=False).iloc[0]
print(f"Team with the best scoring run rate in the last 4 overs: {best_death_overs_run_rate_team['batting_team']} with a run rate of {best_death_overs_run_rate_team['run_rate']}")


# In[ ]:




