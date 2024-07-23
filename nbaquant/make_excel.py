import pandas as pd
import json

with open("file.json", "r") as f:
    data = json.load(f)

data = {
    "data": [game for game in data["data"] if game["min"] != "00"],
    "meta": data["meta"]
}

games_rebounds = [{"game_id": game["game"]["id"], "rebounds": game["reb"]} for game in data["data"]]

# Convert the list to a Pandas DataFrame
df = pd.DataFrame(games_rebounds)

# Save the Pandas Series to an Excel file
df.to_excel("giannis_rebounds.xlsx", index=False)

print("Rebounds have been saved to giannis_rebounds.xlsx")
