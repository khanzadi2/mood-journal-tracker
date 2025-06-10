import json
from user_profile import UserProfile

def save_data(user, filename="journal_data.json"):
    with open(filename, "w") as f:
        json.dump({"name": user.name, "entries": user.entries}, f)

def load_data(filename="journal_data.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            user = UserProfile(data["name"])
            user.entries = data["entries"]
            return user
    except FileNotFoundError:
        return None
