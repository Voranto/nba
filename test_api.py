import requests

url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

# Use a requests.Session to maintain cookies across requests
session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
}

print("Step 1: Warming up session by visiting nba.com...")
try:
    # Hit the main homepage first to pick up Akamai security cookies
    session.get("https://www.nba.com/", headers=headers, timeout=10)

    print("Step 2: Requesting scoreboard JSON with session cookies...")
    response = session.get(url, headers=headers, timeout=10)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        print("Success! Bypassed Akamai protection.")
        data = response.json()
        print(f"Total games found: {len(data['scoreboard']['games'])}")
    else:
        print("Blocked. Response preview:")
        print(response.text[:300])

except Exception as e:
    print(f"An error occurred: {e}")
