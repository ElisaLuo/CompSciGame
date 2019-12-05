import pygame
from random import randint
from os import path

# Code taken from https://www.reddit.com/r/learnprogramming/comments/1xrcow/pythonpygame_why_cant_i_open_an_image_that_is_in/
# Returns the absolute path of a file, used when loading images
def getFile(fileName):
    return path.join(path.dirname(__file__), fileName)

# Load songs
songOne = getFile("CatchYouCatchMe.mp3")
songTwo = getFile("Unravel.mp3")

# Initialize pygame
pygame.init()
pygame.mixer.init()

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
songTitle = pygame.transform.scale(songTitle, (int(width*0.4), int(height*0.12))) 

instructionButton = pygame.image.load(getFile("HowToPlay.png"))
instructionButton = pygame.transform.scale(instructionButton, (int(height*0.175), int(height*0.175)))

note = pygame.image.load(getFile("Note.png"))
note = pygame.transform.scale(note, (int(height*0.075), int(height*0.075)))

shine = pygame.image.load(getFile("Shine.png"))
shine = pygame.transform.scale(shine, (int(width*0.1), int(height*0.9)))

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
score = 0
hits = 0
timer = pygame.time.get_ticks()
startTicks = pygame.time.get_ticks()

fShine = False
gShine = False
hShine = False
jShine = False

fCounter = 0
gCounter = 0
hCounter = 0
jCounter = 0

fTime = []
gTime = []
hTime = []
jTime = []
fHeight = []
gHeight = []
hHeight = []
jHeight = []
for i in range(0, 100):
    fHeight.append(0)
    gHeight.append(0)
    hHeight.append(0)
    jHeight.append(0)

# Functions for drawing what is on home screen
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
    text2 = textFont.render('2. Hits will give you extra points', True, (255, 255, 255))
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

def notesBoard(): # Display score and hits
    textFont = pygame.font.Font(None, 32)
    text1 = textFont.render('Score: ', True, (255, 255, 255))
    text2 = textFont.render(str(score), True, (255, 255, 255))
    text3 = textFont.render('Hits: ', True, (255, 255, 255))
    text4 = textFont.render(str(hits), True, (255, 255, 255))

    textrect1 = text1.get_rect()
    textrect1.centerx = width*0.35
    textrect1.centery = height*0.05

    textrect2 = text2.get_rect()
    textrect2.centerx = width*0.4
    textrect2.centery = height*0.05

    textrect3 = text3.get_rect()
    textrect3.centerx = width*0.6
    textrect3.centery = height*0.05

    textrect4 = text4.get_rect()
    textrect4.centerx = width*0.65
    textrect4.centery = height*0.05

    screen.blit(text1, textrect1)
    screen.blit(text2, textrect2)
    screen.blit(text3, textrect3)
    screen.blit(text4, textrect4)

    # Draw game board
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.3),int(height*0.1)),(int(width*0.3),int(height)),5)
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.35),int(height*0.1)),(int(width*0.35),int(height)))
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.4),int(height*0.1)),(int(width*0.4),int(height)),5)
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.45),int(height*0.1)),(int(width*0.45),int(height)))
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.5),int(height*0.1)),(int(width*0.5),int(height)),5)
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.55),int(height*0.1)),(int(width*0.55),int(height)))
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.6),int(height*0.1)),(int(width*0.6),int(height)),5)
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.65),int(height*0.1)),(int(width*0.65),int(height)))
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.7),int(height*0.1)),(int(width*0.7),int(height)),5)
    pygame.draw.line(screen,(255, 255, 255),(int(width*0.3), int(height*0.8)), (int(width*0.7), int(height*0.8)),5)

def dropNotes(): # Drops notes according to initially loaded array
    for i in range(0, len(fTime)): # For all times where a F note is suppose to drop
        if(timer - startTicks >= fTime[i]+50): # Once the time is reached
            screen.blit(note, ((width*0.35-int(height*0.075)/2), fHeight[i]+10)) # Draw image
            fHeight[i]=((timer - startTicks-fTime[i])*(height/720)/3.25)-50 # Drop by changing the y coordinate of the note

    for i in range(0, len(gTime)):
        if(timer - startTicks >= gTime[i]+50):
            screen.blit(note, ((width*0.45-int(height*0.075)/2), gHeight[i]+10))
            gHeight[i]=((timer - startTicks-gTime[i])*(height/720)/3.25)-50

    for i in range(0, len(hTime)):
        if(timer - startTicks >= hTime[i]+50):
            screen.blit(note, ((width*0.55-int(height*0.075)/2), hHeight[i]+10))
            hHeight[i]=((timer - startTicks-hTime[i])*(height/720)/3.25)-50

    for i in range(0, len(jTime)):
        if(timer - startTicks >= jTime[i]+50):
            screen.blit(note, ((width*0.65-int(height*0.075)/2), jHeight[i]+10))
            jHeight[i]=((timer - startTicks-jTime[i])*(height/720)/3.25)-50
def drawGame():
    notesBoard()
    dropNotes()

while not done:
    for event in pygame.event.get(): # Get user input events
        if (event.type == pygame.QUIT): # If user wants to exit
            done = True # Exit
        elif (event.type == pygame.MOUSEBUTTONDOWN): # If user clicks something
            if(home_drawn): # At the home screen
                x,y = pygame.mouse.get_pos() # Get mouse position
                # Switch to appropriate screen based on where the user clicked
                if(width*0.075<x<width*0.475 and height*0.1<y<height*0.2): # Switch to screen one
                    pygame.mixer.music.load(songOne)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                    home_drawn = False
                    instruction_drawn = False
                    one_drawn = True
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False
                    startTicks = pygame.time.get_ticks()
                elif(width*0.075<x<width*0.475 and height*0.25<y<height*0.35): # Switch to screen two
                    pygame.mixer.music.load(songTwo)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                    home_drawn = False
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = not two_drawn
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False
                    startTicks = pygame.time.get_ticks()
                elif(width*0.075<x<width*0.475 and height*0.4<y<height*0.5): # Switch to screen three
                    home_drawn = False
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = not three_drawn
                    four_drawn = False
                    five_drawn = False
                    startTicks = pygame.time.get_ticks()
                elif(width*0.075<x<width*0.475 and height*0.55<y<height*0.65): # Switch to screen four
                    home_drawn = False
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = not four_drawn
                    five_drawn = False
                    startTicks = pygame.time.get_ticks()
                elif(width*0.075<x<width*0.475 and height*0.7<y<height*0.8): # Switch to screen five
                    home_drawn = False
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = not five_drawn
                    startTicks = pygame.time.get_ticks()
                elif(width*0.7<x<width*0.875 and height*0.6<y<height*0.775): # Switch to instructions
                    home_drawn = False
                    home_drawn = False
                    instruction_drawn = True
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False
        elif (event.type == pygame.KEYDOWN): # If a key is pressed
            if(instruction_drawn): # At the instructions page
                if (event.key == pygame.K_ESCAPE): # Exit the instructions page if ESC pressed
                    home_drawn = True
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False
            if(one_drawn or two_drawn or three_drawn or four_drawn or five_drawn): # At a song page
                if (event.key == pygame.K_ESCAPE): # Exit, reset everything
                    pygame.mixer.music.stop()
                    home_drawn = True
                    score = 0
                    hits = 0
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
                    four_drawn = False
                    five_drawn = False
                    for i in range(0, len(fHeight)):
                        fHeight[i] = 0
                    for i in range(0, len(gHeight)):
                        gHeight[i] = 0
                    for i in range(0, len(hHeight)):
                        hHeight[i] = 0
                    for i in range(0, len(jHeight)):
                        jHeight[i] = 0
                if(event.key == pygame.K_f): # If the F key is pressed
                    #print("f", timer - startTicks-2000)
                    for i in range(0, len(fTime)):
                        if(height*0.85 >= fHeight[i] >= height*0.75): # If the note is hit in the desired range
                            hits = hits + 1 # Add 1 to the number of hits
                            score = score + 100 + hits*5 # Calculate score
                if(event.key == pygame.K_g): # If the G key is pressed
                    #print("g",timer - startTicks-2000)
                    for i in range(0, len(gTime)):
                        if(height*0.85 >= gHeight[i] >= height*0.75):
                            hits = hits + 1
                            score = score + 100 + hits*5
                if(event.key == pygame.K_h): # If the H key is pressed
                    #print("h", timer - startTicks-2000)
                    for i in range(0, len(hTime)):
                        if(height*0.85 >= hHeight[i] >= height*0.75):
                            hits = hits + 1
                            score = score + 100 + hits*5
                if(event.key == pygame.K_j): # If the J key is pressed
                    #print("j", timer - startTicks-2000)
                    for i in range(0, len(jTime)):
                        if(height*0.85 >= jHeight[i] >= height*0.75):
                            hits = hits + 1
                            score = score + 100 + hits*5

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_f]: 
        fShine = True
    if pressed[pygame.K_g]: 
        gShine = True
    if pressed[pygame.K_h]: 
        hShine = True
    if pressed[pygame.K_j]: 
        jShine = True
    
    screen.fill((0,0,0)) # Screen color
    screen.blit(background, (0, 0))
    
    # Draw the screen
    if(home_drawn): home()
    if(instruction_drawn): instructions()
    if(one_drawn): 
        fTime = [1281, 1932, 3696, 5531, 8492, 11290, 13516, 14500, 18590, 20498, 24236, 26145, 28637, 31457, 33316, 34792, 36208, 38668, 42463, 42906, 46168, 48018, 48470, 50812, 51263, 53637, 54105, 55056, 57221, 57666, 59135, 61106, 61550, 64463, 65066, 68806, 69384, 71565]
        gTime = [1932, 2856, 4197, 6004, 9790, 11570, 12781, 14851, 16770, 22128, 22688, 27946, 29110, 31899, 33823, 34299, 36580, 38042, 39099, 41497, 41898, 43408, 43855, 47088, 49930, 52670, 56016, 56939, 58087, 60069, 62024, 62431, 65640, 66139, 70597]
        hTime = [4701, 5497, 6993, 7500, 9415, 11879, 13955, 15934, 17891, 19973, 21594, 23565, 25418, 27206, 29595, 31017, 32845, 35313, 35783, 37568, 40560, 40989, 44298, 44693, 47513, 50337, 53144, 55595, 56497, 59618, 63581, 64019, 67717, 68238, 71114]
        jTime = [6546, 6993, 7500, 8994, 10242, 10750, 12173, 13241, 15372, 17400, 19291, 21098, 23147, 24902, 26733, 30117, 30517, 32426, 37087, 39587, 40035, 45158, 45691, 46625, 49051, 49530, 51767, 52172, 54613, 58599, 60627, 62759, 63171, 66678, 67189, 70037, 72175]
        timer = pygame.time.get_ticks()
        drawGame() 
    if(two_drawn): 
        fTime = [1000, 2000, 3000]
        gTime = [2000, 4000, 4500]
        hTime = [3500, 6000, 8000]
        jTime = [5000, 7000, 8000]
        timer = pygame.time.get_ticks()
        drawGame()
    if(three_drawn): 
        fTime = [1000, 2000, 3000]
        gTime = [2000, 4000, 4500]
        hTime = [3500, 6000, 8000]
        jTime = [5000, 7000, 8000]
        timer = pygame.time.get_ticks()
        drawGame()
    if(four_drawn): 
        fTime = [1000, 2000, 3000]
        gTime = [2000, 4000, 4500]
        hTime = [3500, 6000, 8000]
        jTime = [5000, 7000, 8000]
        timer = pygame.time.get_ticks()
        drawGame()
    if(five_drawn): 
        fTime = [1281, 1932, 3696, 5531]
        gTime = [1932, 2856, 4197, 6004]
        hTime = [5497, 6993, 7500]
        jTime = [6546, 6993, 7500]
        timer = pygame.time.get_ticks()
        drawGame()
    
    if(one_drawn or two_drawn or three_drawn or four_drawn or five_drawn):
        if(fShine):
            fCounter = fCounter + 1
            screen.blit(shine, (int(width*0.3), int(height*0.1)))
            if(fCounter >= 4):
                fShine = False
                fCounter = 0
        if(gShine):
            gCounter = gCounter + 1
            screen.blit(shine, (int(width*0.4), int(height*0.1)))
            if(gCounter >= 4):
                gShine = False
                gCounter = 0
        if(hShine):
            hCounter = hCounter + 1
            screen.blit(shine, (int(width*0.5), int(height*0.1)))
            if(hCounter >= 4):
                hShine = False
                hCounter = 0
        if(jShine):
            jCounter = jCounter + 1
            screen.blit(shine, (int(width*0.6), int(height*0.1)))
            if(jCounter >= 4):
                jShine = False
                jCounter = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
