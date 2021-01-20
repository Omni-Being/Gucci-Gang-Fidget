from turtle import *
import pygame


state = {'turn': 0}
title("Gucci Gang: Spinner")

def spinner():

    
    "Draw fidget spinner."
    clear()
    bgpic('BGIMG3.png')
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(150,'Red')
    back(100)
    right(120)
    forward(100)
    dot(150, 'blue')
    back(100)
    right(120)
    forward(100)
    dot(150, 'green')
    back(100)
    right(120)
    goto(0,0)
    dot(10,'white')
    update()

    
    


def animate():
    "Animate fidget spinner."
    
    if state['turn'] > 0:
        state['turn'] -= 1
    spinner()    
    ontimer(animate, 20)



def flick():
    "Flick fidget spinner."    
    state['turn'] += 20



    

setup(1152, 864, 50, 0)
hideturtle()
tracer(False)
onkey(flick, 'space')

pygame.mixer.init()
pygame.mixer.music.load("Gucci Gang.wav")
pygame.mixer.music.play()          
    
width(30)
listen()
animate()
done()
