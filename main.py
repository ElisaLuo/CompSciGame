import pygame
from random import randint
from os import path

# Code taken from https://www.reddit.com/r/learnprogramming/comments/1xrcow/pythonpygame_why_cant_i_open_an_image_that_is_in/
# Returns the absolute path of a file, used when loading images
def getFile(fileName):
    return path.join(path.dirname(__file__), fileName)

# Initialize pygame
pygame.init()

# Get display width and height and set screen to it
width = int(pygame.display.Info().current_w/1.5) # Screen zoom scale (1.5)
height = int(pygame.display.Info().current_h/1.5)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Pygame Project") # Set display name
clock = pygame.time.Clock()

# Loads all images and changes images to appropriate size
background = pygame.image.load(getFile("Background.jpg"))
background = pygame.transform.scale(background, (width, height))

songTitle = pygame.image.load(getFile("Song.png"))
songTitle = pygame.transform.scale(songTitle, (int(width*0.4), int(height*0.1))) 

instructionButton = pygame.image.load(getFile("HowToPlay.png"))
instructionButton = pygame.transform.scale(instructionButton, (int(height*0.175), int(height*0.175)))

# If the different screens are drawn
home_drawn = True
instruction_drawn = False
one_drawn = False
two_drawn = False
three_drawn = False
four_drawn = False
five_drawn = False

done = False

# Item setup


# Functions for drawing what is on screen
def home():
    screen.blit(songTitle, (int(width*0.075), height*0.10))
    screen.blit(songTitle, (int(width*0.075), height*0.25))
    screen.blit(songTitle, (int(width*0.075), height*0.40))
    screen.blit(songTitle, (int(width*0.075), height*0.55))
    screen.blit(songTitle, (int(width*0.075), height*0.70))
    screen.blit(instructionButton, (int(width*0.7), height*0.6))

def instructions(): # Prints out instructions
    titleFont = pygame.font.Font(None, 64) 
    textFont = pygame.font.Font(None, 32)

    titleText = titleFont.render('Instructions', True, (255, 255,255)) 
    text1 = textFont.render('1. Press F, G, H, J to the corresponding falling note', True, (255, 255, 255))
    text2 = textFont.render('2. Combos will give you extra points', True, (255, 255, 255))
    text3 = textFont.render('(Press ESC to return to home page)', True, (255, 255, 255))

    textrect = titleText.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = height*0.2

    textrect1 = text1.get_rect()
    textrect1.centerx = screen.get_rect().centerx
    textrect1.centery = height*0.3

    textrect2 = text2.get_rect()
    textrect2.centerx = screen.get_rect().centerx
    textrect2.centery = height*0.4

    textrect3 = text3.get_rect()
    textrect3.centerx = screen.get_rect().centerx
    textrect3.centery = height*0.5

    screen.blit(titleText, textrect)
    screen.blit(text1, textrect1)
    screen.blit(text2, textrect2)
    screen.blit(text3, textrect3)

def one():
    pygame.draw.circle(screen, (255,255,255), (int(width*0.5),int(height*0.5)), 100)

def two():
    pygame.draw.circle(screen, (255,255,0), (int(width*0.6),int(height*0.5)), 100)

def three():
    pygame.draw.circle(screen, (255,0,255), (int(width*0.7),int(height*0.5)), 100)

def four():
    pygame.draw.circle(screen, (0,255,255), (int(width*0.8),int(height*0.5)), 100)

def five():
    pygame.draw.circle(screen, (255,0,0), (int(width*0.9),int(height*0.5)), 100)

while not done:
    for event in pygame.event.get(): # Key press events
        if (event.type == pygame.QUIT):
            done = True
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            # If the mouse button is clicked when at home screen
            if(home_drawn):
                x,y = pygame.mouse.get_pos() # Get mouse position
                # Switch to appropriate screen based on where the user clicked
                if(width*0.075<x<width*0.475 and height*0.1<y<height*0.2): # Switch to screen one
                    instruction_drawn = False
                    one_drawn = not one_drawn
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False
                elif(width*0.075<x<width*0.475 and height*0.25<y<height*0.35): # Switch to screen two
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = not two_drawn
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False
                elif(width*0.075<x<width*0.475 and height*0.4<y<height*0.5): # Switch to screen three
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = not three_drawn
                    four_drawn = False
                    five_drawn = False
                elif(width*0.075<x<width*0.475 and height*0.55<y<height*0.65): # Switch to screen four
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = not four_drawn
                    five_drawn = False
                elif(width*0.075<x<width*0.475 and height*0.7<y<height*0.8): # Switch to screen five
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = not five_drawn
                elif(width*0.7<x<width*0.875 and height*0.6<y<height*0.775):
                    home_drawn = False
                    instruction_drawn = True
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False
        elif (event.type == pygame.KEYDOWN):
            if(instruction_drawn):
                if (event.key == pygame.K_ESCAPE):
                    home_drawn = True
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False

                    

    screen.fill((0,0,0)) # Screen color
    screen.blit(background, (0, 0))

    # Draw the screen
    if(home_drawn): home()
    if(instruction_drawn): instructions()
    if(one_drawn): one()
    if(two_drawn): two()
    if(three_drawn): three()
    if(four_drawn): four()
    if(five_drawn): five()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
