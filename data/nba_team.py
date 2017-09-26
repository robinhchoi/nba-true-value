import pandas as pd

team_abbrevs = ["BOS", "PHI", "BRK", "NYK", "TOR", # Atlantic Div
                "CHI", "DET", "MIL", "IND", "CLE", # Central Div
                "WAS", "MIA", "ORL", "CHO", "ATL", # Southeast Div
                "GSW", "LAL", "LAC", "PHO", "SAC", # Pacific Div
                "POR", "DEN", "OKC", "MIN", "UTA", # Northwest Div
                "HOU", "SAS", "DAL", "NOP", "MEM"] # Southwest Div

class Team(object):

    def __init__(self, abbrev):
        if abbrev in team_abbrevs:
            # initialize 
        else:
            # return empty object/error

    def get_salary(self, player_name):
        
