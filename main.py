from datetime import datetime
from user_profile import UserProfile
from mood_analyzer import analyze_mood
from data_handler import save_data, load_data
from utils import suggest_activity

def main():
    print("🌟 Welcome to Mood Journal & Sentiment Tracker 🌟")
    
    user = load_data()
    if not user:
        name = input("Enter your name: ").strip()
        user = UserProfile(name)
    else:
        print(f"Welcome back, {user.name}!")

    while True:
        print("\nChoose an option:")
        print("1. Add New Entry")
        print("2. View Mood History")
        print("3. Save and Exit")
        
        choice = input("Your choice: ")

        if choice == "1":
            text = input("How are you feeling today? ")
            if not text:
                print("Please enter something.")
                continue
            mood = analyze_mood(text)
            date = datetime.now().strftime("%Y-%m-%d")
            user.add_entry(date, text, mood)
            print(f"Your mood is: {mood}")
            print(f"Suggested Activity: {suggest_activity(mood)}")
        
        elif choice == "2":
            print("\n📘 Your Mood History:")
            user.show_history()
        
        elif choice == "3":
            save_data(user)
            print("Journal saved. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()
