import random
import time
import webbrowser

ChalkColors = ["Red", "Green", "Blue", "Yellow", "White", "Black"]

def getChalkColor():
    input("What color would you like to use? Red, Green, Blue, Yellow, White, Black? Press Enter to continue...")
    user_color = input()
    if user_color.lower() == "red":
        print("Red? Why would you pick Red? It's the worst color! Press Enter to continue...")
        input()
        print("But beware, choosing red has consequences... Press Enter to continue...")
        input()
        print("In 15 minutes, a red light will appear in your house. Press Enter to continue...")
        input()
        print("And you have 2 hours before the entity comes for you... Press Enter to continue...")
        input()
        return "Red"
    else:
        return random.choice(ChalkColors)

selected_color = getChalkColor()

if selected_color:
    print("You chose the color:", selected_color)
else:
    print("You chose the color: None")

# If user chose red, initiate the countdown
if selected_color == "Red":
    time.sleep(0)  # 15 minutes countdown
    print("A red light appears in your house... You feel a sense of dread creeping in. Press Enter to continue...")
    input()
    time.sleep(0)  # 2 hours countdown
    print("You hear strange noises, and suddenly, a dark entity emerges from the shadows... Press Enter to continue...")
    input()
    print("It's too late. You're completely fucked. Press Enter to continue...")
    input()
    print("The best thing you can do now is to share your experience on the paranormal page of 4chan. Press Enter to continue...")
    input()
    print("Quickly, go to the x paranormal page on 4chan and make a post before it's too late. Press Enter to continue...")
    input()
    print("Time's running out. Open the link to the x paranormal page on 4chan now! Press Enter to continue...")
    input()
    webbrowser.open("https://boards.4chan.org/x/")
