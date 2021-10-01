from pygame import mixer
  
# Starting the mixer
mixer.init()
  
# Loading the song
mixer.music.load("cave5.mp3")
mixer.music.load("cave6.mp3")  
# Setting the volume
mixer.music.set_volume(0.7)
  
# Start playing the song
  
# infinite loop
while True:
    print("press '1' to play the caveone")
    print("press '2' to play the cavetw0")
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    print("Press 's' to shuffle music")
    query = input("  ")
      
    if query == 'p':
  
        # Pausing the music
        mixer.music.pause()     
    elif query == 's':
        import random
        s = random.randrange(1,2)
        print(s)
  
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break
    elif query == '1':
    
        # Stop the mixer
        mixer.music.load("cave5.mp3")
        mixer.music.play()
        break
    elif query == '2':
        mixer.music.load("cave6.mp3")
        mixer.music.play()
