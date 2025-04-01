import pygame
import os

pygame.init()
pygame.mixer.init()


music_folder = "lab7"
music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

if not music_files:
    print("not finded music ,check lab7！")
    exit()

current_song = 0  
paused = False 

def play_music(index):
    pygame.mixer.music.load(os.path.join(music_folder, music_files[index]))
    pygame.mixer.music.play()
    print(f": {music_files[index]}")

play_music(current_song)  

screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("music player")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                    print("stop")
                else:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("countinue")
            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
                print("stop")
            elif event.key == pygame.K_RIGHT: 
                current_song = (current_song + 1) % len(music_files)
                play_music(current_song)
            elif event.key == pygame.K_LEFT:  
                current_song = (current_song - 1) % len(music_files)
                play_music(current_song)

pygame.quit()
