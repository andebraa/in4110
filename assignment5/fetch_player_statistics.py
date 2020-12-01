from requesting_urls import get_html
from filter_urls import filter_urls, find_articles

from bs4 import BeautifulSoup 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""
Didnt get your code to run. Here is an example of how this could have been solved with pandas.
"""

def fetch_statistics(url):
    """
    Gets the statistics from nba and plots the top 3
    players from each team

    Args:
        url (string): the url of a nba season wikipedia page
    """
    
    team_names, team_urls = extract_url(url)
    
    all_players = []

    for team, url in zip(team_names, team_urls):
        player_urls = extract_player_urls(url)
        for player_url in player_urls:
            player_stats = extract_player_points(player_url, team)
            if player_stats is not None:
                all_players.append(player_stats)
    
    players_df = pd.DataFrame(all_players, columns=["Name", "Team", "PPG", "BPG", "RPG"])
    top_3_players = find_top_3_players(players_df)
    for column in ["PPG", "BPG", "RPG"]:
        plot_players(players_df, top_3_players, column=column)
    
def extract_url(url):
    """
    Extracting team names from all the teams in semifinals

    Args:
        url (string): 

    Returns:
        team_names: list - of all teams
        team_urls: list - of each teams url
    """
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    soup_table = soup.find("table", attrs={"style":"font-size: 90%; margin:1em 2em 1em 1em;"})
    soup_table_rows = soup_table.find_all("tr")
    soup_table_rows = soup_table_rows[4:]
    soup_table_rows = soup_table_rows[::12]+soup_table_rows[2::12]
    team_cells_html = [str(row.find("a")) for row in soup_table_rows]
    team_names = [row.find("a").text for row in soup_table_rows]
    team_names = [name if len(name.split()) == 1 else name.split()[-1] for name in team_names]
    team_urls = filter_urls(html="\n".join(team_cells_html), base_url="https://en.wikipedia.org")
    return team_names, team_urls

def extract_player_urls(url):
    """
    Finding all the players urls from a nba team page

    Args:
        url (string): 

    Returns:
        list: all player urls
    """
    
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    team_name = soup.find("h1", attrs={"id": "firstHeading"}).text
    team_name = team_name[8:-7]     #Takes away 2019-20 and season from title
    soup_table = soup.find("table", attrs={"class":"toccolours"})
    soup_table_rows = soup_table.find_all("tr")[2].td.table.tbody.find_all("tr")
    column_names = [row.find("td", attrs={"style": "text-align:left;"}) for row in soup_table_rows]
    column_names.remove(None)
    player_cells_html = [str(row.find("a")) for row in column_names]
    player_urls = filter_urls(html="\n".join(player_cells_html), base_url="https://en.wikipedia.org") 

    return player_urls

def extract_player_points(url, team):
    """
    Finding the players points for 2019-20.

    Args:
        url (string): nba player wikipedia site
        team (string): team of player. Used when players has played in two clubs that season.

    Returns:
        list: a list with the players name and points for that season
    """
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    name = soup.find("h1", attrs={"class": "firstHeading"}).text
    
    
    try:
        for soup_table in soup.find_all("table", attrs={"class": "wikitable sortable"}):
            try:
                for row in soup_table.tbody.find_all("tr")[1:]:
                    try:
                        if str(row.find("td").a.text).rstrip() == "2019–20":
                            elms = row.find_all("td")
                            
                            if team in elms[1].text.rstrip():
                                return [name, elms[1].text.rstrip(), float(elms[-1].text.replace("*","")), float(elms[-2].text), float(elms[-5].text)]
                    except Exception:
                        pass
            except Exception:
                        pass
    except Exception:
        pass



def find_top_3_players(all_players):
    """
    Finding the top 3 players from each team

    Args:
        all_players (pandas.df): a dataframe of all the players in semifinals

    Returns:
        pandas.df: a dataframe of each top 3 players of each team
    """
    all_players.Team = all_players.Team.replace("L.A Clippers", "L.A. Clippers")
    
    all_players = all_players.sort_values("PPG", ascending=False)
    teams = all_players.Team.unique()
    top_3_players = []
    for team in teams:
        top_3_team_players = all_players[all_players.Team == team][:3].values
        
        for player in top_3_team_players:
            top_3_players.append(player)
    
    return top_3_players

def plot_players(all_players, top_3_players, column="PPG"):
    """
    Plots the statistics for best players in each team

    Args:
        all_players (pandas.df): 
        top_3_players (pandas.df): 
        column (str, optional): what stats to sort by. Defaults to "PPG".
    """
    teams = all_players.Team.unique()

    top_3_players_df = pd.DataFrame(top_3_players, columns=all_players.columns.values)
    top_3_players_df = top_3_players_df.sort_values(["Team", "Name"])
    #Because there are 3 and 3 players from each team and the players are sorted
    #by team, we only need a list with colors that follows this form
    colorsInUse = ["C"+str(i) for i in range(len(teams))]
    colors = []
    handles = []
    for c, t in zip(colorsInUse, sorted(teams)):
        for _ in range(3):
            colors.append(c)
        handles.append(mpatches.Patch(color=c, label=t))

    top_3_players_df[["Name", column]].plot.bar(x="Name", y=column, color=colors)

    plt.xlabel("Player name")
    plt.ylabel(column)
    plt.legend(handles=handles, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)  

    plt.savefig(f"NBA_player_statistics/players_over_{column.lower()}.jpeg", bbox_inches="tight")


fetch_statistics("https://en.wikipedia.org/wiki/2020_NBA_playoffs")

