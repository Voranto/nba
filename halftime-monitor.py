from nba_api.live.nba.endpoints import scoreboard
from win11toast import toast
import time


def getGamesById(id):
    games_dict = scoreboard.ScoreBoard().get_dict()
    games = []
    for game in games_dict["scoreboard"]["games"]:
        if game["gameId"] == id:
            games.append(game)
    return games


games = scoreboard.ScoreBoard()
games_dict = games.get_dict()
print("Pick the games to monitor, separated by commas: ")
for i, game in enumerate(games_dict["scoreboard"]["games"]):
    print(f"[{i}]: {game['homeTeam']['teamName']} vs {game['awayTeam']['teamName']} ")

games_idx = [int(x) for x in input("Your games to monitor: ").split(",")]

games_id = [
    games_dict["scoreboard"]["games"][game_idx]["gameId"] for game_idx in games_idx
]

games = getGamesById(games_id)
periods = [game["period"] if "period" in game else -1 for game in games]
while True:
    games = scoreboard.ScoreBoard()
    periods_new = []
    for i, period in enumerate(periods):
        periods_new = [
            g["period"] if "period" in g else -1 for g in getGamesById(games_id)
        ]
        if period == 2 and periods_new[i] == 3:
            toast(
                "Halftime is done for game",
                games_dict["scoreboard"]["games"][i]["homeTeam"]["teamName"],
                "vs",
                games_dict["scoreboard"]["games"][i]["awayTeam"]["teamName"],
                "!",
            
            )
        if period == -1 and periods_new[i] != -1:
            toast(
                "Tracked game has started!",
                games_dict["scoreboard"]["games"][i]["homeTeam"]["teamName"],
                "vs",
                games_dict["scoreboard"]["games"][i]["awayTeam"]["teamName"],
                  )
        periods = periods_new
    time.sleep(20)
