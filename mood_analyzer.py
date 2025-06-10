def analyze_mood(text):
    text = text.lower()
    happy = ["happy", "great", "good", "excited", "joy", "love"]
    sad = ["sad", "tired", "bad", "angry", "upset", "depressed"]

    if any(word in text for word in happy):
        return "Happy 😊"
    elif any(word in text for word in sad):
        return "Sad 😞"
    else:
        return "Neutral 😐"
