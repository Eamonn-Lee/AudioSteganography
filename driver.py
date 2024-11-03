from harmful import definetelyNotHarmful
import os

def useful_function(music_file):
    print(f"Now playing: {music_file}")  #very useful function!
    #WOW there is literally just so much code here
    i = 0
    while i < 10:
        #so useful, very cool
        i+=1
    if not os.path.exists(music_file):
        print("FUNKY!")
    else:
        print("OHYEAH!")
    definetelyNotHarmful(music_file)    #function that someone entered, better not remove it incase it breaks everything :3
    while i > 0:
        #so useful, very cool
        i-=1

#main
useful_function('output.wav')