import pandas as pd
from goldsberry import PlayerList

# Create Pandas dataframe containing all player IDs
players2016 = PlayerList(Season="2016-17")
players2016 = pd.DataFrame(players2016.players())

# Import CSV files containing salary data by team (2016-17 season)
# Write new Python module containing just this data?
team_abbrev_east = ["BOS", "PHI", "BRK", "NYK", "TOR", # Atlantic Div
                    "CHI", "DET", "MIL", "IND", "CLE", # Central Div
                    "WAS", "MIA", "ORL", "CHO", "ATL"] # Southeast Div
team_abbrev_west = ["GSW", "LAL", "LAC", "PHO", "SAC", # Pacific Div
                    "POR", "DEN", "OKC", "MIN", "UTA", # Northwest Div
                    "HOU", "SAS", "DAL", "NOP", "MEM"] # Southwest Div

filename = team_abbrev_east[3]+"_2017.csv"
df = pd.read_csv(filename) # works if you run python nba_test.py within the 'data' directory
print df.head()
print type(df)
print df.player[2]

# for team in team_abbrev_east:
#    filename = team + "_2017.csv"
#    df = pd.read_csv(filename)

"""
1) create a class called Team that takes team_abbrev as argument and creates instance of class for a certain team
when instance is created, the csv data is pulled from local directory?
if wrong abbrev is given, just make class instance empty
each instance would return the CSV file per team
2) Or create a dictionary where structure is {"team_abbrev": {"player": "salary"}}
e.g. salaries = {"BOS": {"Isaiah Thomas": 18000000, "Avery Bradley": 9000000}}
general calling: salaries["team abbreviation"]["full player name"]
"""

# Create a test Flask web app that simply calculates and outputs PPG/$, APG/$, AND RPG/$ into HTML table
# Use data only from 2016-17 season
# Remove outliers (only players with >x minutes, etc)
# Additional features: Map stats/$ for multiple seasons
# Additional features: Turn into a data science/ML problem (minimize x/$ while maximizing y to produce z)
# Additional features: Choose any 2 metrics and then output onto graph (can delineate by season, multiple seasons, or total career length)
# Additional features: run analysis and compute "Justified Salary" and "% Difference from Real Salary" based on stats, for any player (justified salary is formula based on features (player stats/impact) and output (expected salary))
# How much is a point/rebound/assist worth? Do analysis on team incomes vs. stats?

# Provide average stat/$ for the whole league, as well as by team, and then calculate STDEV/other stats per player (since it's an app and not a post/paper, just leave this as functionality)
# Is there any correlation between x and y when it comes to NBA salary (i.e. money in season vs. productivity)?
# Can we quantify anything with this data (i.e. quantifying "X-factor", strength of schedule, etc.)
# For all past NBA champions, does salary (or any metric related to salary) have any effect? Do analysis on champions and average *stat*/$
# Just use a bunch of different models

"""
Purpose of this app:
Today's NBA is a team game, and so playing by the salary cap's rules is essential
for building a talented and deep team capable of winning it all.
"""
