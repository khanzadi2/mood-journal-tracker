class UserProfile:
    def __init__(self, name):
        self.name = name
        self.entries = {}  # {date: {'text': "...", 'mood': "..."}}

    def add_entry(self, date, text, mood):
        self.entries[date] = {'text': text, 'mood': mood}

    def show_history(self):
        if not self.entries:
            print("No entries yet.")
        else:
            for date, entry in self.entries.items():
                print(f"{date} - Mood: {entry['mood']} | Note: {entry['text']}")
