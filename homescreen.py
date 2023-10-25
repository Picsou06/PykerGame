<<<<<<< HEAD
from tkinter import * #Importer tkinter
def homescreen(): #Fonction Homescreen
    screen = Tk() #Definition de la variable screen
    screen.resizable(width=False, height=False)
    screen.iconbitmap("Images/UnNomDeJeuDePoker.ico")
    img = PhotoImage(file="Images//background.gif")
    w, h = screen.winfo_screenwidth(), screen.winfo_screenheight()
    can = Canvas(screen, width=w, height=h)
    can.create_image(140,200, anchor=NW, image=img)
    can.pack(fill="both", expand=True)
    can.place(x=0,y=0)
    screen.geometry("400x400")
    screen.mainloop()
    
=======
import pygame
from pygame import *
import game

def homescreen(screen):
    screen_width, screen_height = screen.get_size()
    background_image = pygame.transform.scale(pygame.image.load("images/background.gif"), (screen_width,screen_height))
    gif_image = pygame.image.load("images/play.gif")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                print("space")
                game.game(screen)

        gif_x = (screen_width - gif_image.get_width()) / 2
        gif_y = screen_height - gif_image.get_height()
        screen.blit(background_image, (0, 0))
        screen.blit(gif_image, (gif_x, gif_y))

        pygame.display.flip()

    pygame.quit()
>>>>>>> 89d54f8 (Evan: Début d'idée, base screen et placement carte)
