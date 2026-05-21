from nba_api.live.nba.endpoints import scoreboard
from win11toast import toast
import time

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
}

def getGameById(id):
    games = scoreboard.ScoreBoard(headers=headers).get_dict()
    for game in games["scoreboard"]["games"]:
        if game["gameId"] == id:
            return game

games = scoreboard.ScoreBoard(headers=headers)

games_dict = games.get_dict()
print(games.get_json())
print("Pick the game to monitor: ")
for i,game in enumerate(games_dict["scoreboard"]["games"]):
    print(f"[{i}]: {game["homeTeam"]["teamName"]} vs {game["awayTeam"]["teamName"]} ")

game_idx = int(input("Your game to monitor: "))

game_id = games_dict["scoreboard"]["games"][game_idx]["gameId"]

game = getGameById(game_id)
period = game["period"]
while True:
    games = scoreboard.ScoreBoard(headers=headers)
    period_new = getGameById(game_id)["period"]
    if period == 2 and period_new == 3:
        toast("Halftime is done!")
    
    period = period_new
    time.sleep(5)
    