'''
def get_mood(color):
    mycolor = color.lower().strip()


if color == "red"
    return "angry"
elif color = "yellow"
    return = mellow
elif color == "blue"
    return "sad"
elif color = "green"
    return = happy
elif color == "black"
    return "scary"
elif color = "purple"
    return = roayal
elif color = "pink"
    retutn = fun
'''
def get_mood(color):
    color_moods = {
      "red":"angry",  
      "yellow":"mellow",
      "blue":"sad",
      "green":"happy",
      "black":"scary",
      "purple":"angry",
      "red":"roayal",
      "pink":"fun"
    }
if color in color_moods:
    return color_moods[color]
else:
    return False

print("Mood Ring!")
ring_color = input("Enter color on ring: ").strip().lower()
mood = get_mood(ring_color)

if (mood != False):
    print(f"You are felling very {mood}")
else:
    print("Sorry, Invalid color")