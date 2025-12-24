import requests, os

TARGETS = {
    "fnaf": "https://freddy-fazbears-pizza.fandom.com/api.php",
    "bendy": "https://bendy.fandom.com/api.php"
}

def scout():
    for game, url in TARGETS.items():
        r = requests.get(url, params={"action": "query", "list": "recentchanges", "format": "json"}).json()
        path = f"lore_vault/{game}/auto_updates/"
        os.makedirs(path, exist_ok=True)
        
        for change in r['query']['recentchanges']:
            filename = f"{path}{change['title'].replace(' ', '_')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Scouted Intel: {change['title']} was recently updated on the Wiki.")
        print(f"✅ {game.upper()} archive synced.")

if __name__ == "__main__":
    scout()