def suggest_activity(mood):
    if "Happy" in mood:
        return "Go out for a walk or call a friend!"
    elif "Sad" in mood:
        return "Try journaling more or listen to calm music."
    else:
        return "Take a deep breath and relax."
