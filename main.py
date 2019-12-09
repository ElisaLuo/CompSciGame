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
songThree = getFile("YumeSakura.mp3")

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
    screen.blit(songTitle, (int(width*0.075), height*0.40))
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
        if(timer - startTicks >= fTime[i]+75): # Once the time is reached
            screen.blit(note, ((width*0.35-int(height*0.075)/2), fHeight[i]+10)) # Draw image
            fHeight[i]=((timer - startTicks-fTime[i])*(height/720)/3.25)-50 # Drop by changing the y coordinate of the note

    for i in range(0, len(gTime)):
        if(timer - startTicks >= gTime[i]+75):
            screen.blit(note, ((width*0.45-int(height*0.075)/2), gHeight[i]+10))
            gHeight[i]=((timer - startTicks-gTime[i])*(height/720)/3.25)-50

    for i in range(0, len(hTime)):
        if(timer - startTicks >= hTime[i]+75):
            screen.blit(note, ((width*0.55-int(height*0.075)/2), hHeight[i]+10))
            hHeight[i]=((timer - startTicks-hTime[i])*(height/720)/3.25)-50

    for i in range(0, len(jTime)):
        if(timer - startTicks >= jTime[i]+75):
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
                    startTicks = pygame.time.get_ticks()
                elif(width*0.075<x<width*0.475 and height*0.4<y<height*0.5): # Switch to screen two
                    pygame.mixer.music.load(songTwo)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                    home_drawn = False
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = not two_drawn
                    three_drawn = False
                    startTicks = pygame.time.get_ticks()
                elif(width*0.075<x<width*0.475 and height*0.7<y<height*0.8): # Switch to screen three
                    pygame.mixer.music.load(songThree)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                    home_drawn = False
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = not three_drawn
                    startTicks = pygame.time.get_ticks()
                elif(width*0.7<x<width*0.875 and height*0.6<y<height*0.775): # Switch to instructions
                    home_drawn = False
                    home_drawn = False
                    instruction_drawn = True
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
        elif (event.type == pygame.KEYDOWN): # If a key is pressed
            if(instruction_drawn): # At the instructions page
                if (event.key == pygame.K_ESCAPE): # Exit the instructions page if ESC pressed
                    home_drawn = True
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
            if(one_drawn or two_drawn or three_drawn): # At a song page
                if (event.key == pygame.K_ESCAPE): # Exit, reset everything
                    pygame.mixer.music.stop()
                    home_drawn = True
                    score = 0
                    hits = 0
                    instruction_drawn = False
                    one_drawn = False
                    two_drawn = False
                    three_drawn = False
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
        fTime = [1831, 5199, 7846, 10123, 10319, 11593, 13677, 15814, 17365, 18849, 19532, 20947, 22976, 24334, 26197, 27480, 28417, 29732, 30933, 31952, 33423, 34477, 35600, 36623, 37202, 38131, 38749, 40612, 42224, 43945, 44576, 46524, 48069, 48440, 48608, 49654, 49825, 51444, 53301, 55270, 56307, 56720, 58622, 59922, 61751, 62846, 64778, 65334, 67136, 67326, 69722, 71142, 71486, 73009, 74415, 76123, 77754, 79053, 83282]
        gTime = [2283, 4511, 6021, 8069, 10911, 12431, 14621, 16232, 16632, 18181, 19904, 22026, 23438, 24892, 25692, 26787, 28726, 30110, 31305, 32454, 33834, 35043, 35226, 36260, 37608, 38495, 39843, 41073, 42954, 45130, 47484, 47634, 48925, 50423, 51867, 53893, 54328, 55677, 57117, 57597, 59086, 60445, 62149, 64027, 66213, 67903, 69026, 70523, 71909, 73700, 75047, 75465, 77045, 78449, 82413]
        hTime = [1430, 2283, 4283, 6484, 7063, 8963, 10694, 11957, 14190, 15357, 17206, 19904, 21545, 23294, 26604, 27063, 28059, 29285, 29538, 30305, 30561, 31139, 31770, 32183, 33181, 34112, 34247, 35482, 36415, 37365, 38332, 39504, 39681, 40887, 42694, 45576, 47887, 49207, 49386, 50693, 51595, 52752, 55461, 58238, 58376, 59457, 60790, 61196, 62373, 62599, 64302, 66013, 66679, 68356, 68904, 69269, 69440, 70727, 72851, 73262, 73466, 74741, 76491, 76807, 78630, 81446]
        jTime = [945, 1831, 2950, 3526, 3758, 5597, 7292, 9337, 11339, 13006, 13432, 14826, 16232, 16655, 17924, 19491, 20779, 22268, 23902, 25483, 27800, 28934, 29905, 30730, 31573, 32669, 32814, 33730, 34722, 35893, 36028, 36887, 36991, 37805, 37949, 29048, 40080, 40375, 41638, 42076, 43748, 46659, 48805, 50174, 51068, 51243, 52047, 54791, 55052, 55968, 58768, 60132, 61920, 63554, 63687, 67632, 69953, 70148, 70303, 72400, 72541, 73888, 74189, 75970, 78221, 79603]
        timer = pygame.time.get_ticks()
        drawGame()
    if(three_drawn): 
        fTime = [1169, 3537, 4002, 5997, 8337, 10772, 12351, 13683, 13975, 14147, 15096, 16395, 17167, 18019, 18193, 19358, 20333, 20555, 21527, 22529, 23474, 24682, 25169, 26928, 27340, 28443, 30068, 30496, 31714, 33762, 34697, 35708, 36793, 37785, 38781, 40659, 41942, 43325, 44373, 45975, 47546, 49162, 50556]
        gTime = [1618, 4417, 6387, 6803, 9527, 11567, 14343, 15730, 16838, 17923, 18545, 19668, 20820, 21876, 22941, 23933, 25497, 27719, 28126, 29531, 30713, 31962, 32138, 32779, 34021, 35160, 36079, 36436, 37108, 38134, 39247, 39564, 40842, 42309, 42674, 43722, 46416, 46544, 48149, 49558]
        hTime = [2298, 2720, 5617, 7557, 7990, 9953, 10378, 12018, 13324, 13479, 14895, 16013, 16147, 17008, 17758, 18467, 19079, 19216, 20134, 21156, 21289, 22122, 22277, 23152, 23294, 24168, 24424, 25376, 26523, 28294, 29660, 31481, 32346, 32925, 33320, 34893, 35908, 37242, 37420, 38376, 38559, 40186, 40424, 41576, 43153, 43325, 43543, 44792, 45195, 46796, 47926, 48975, 50252]
        jTime = [3156, 4809, 5230, 7161, 8721, 9129, 11199, 12682, 12962, 14505, 14649, 15325, 15502, 15668, 16569, 16708, 17734, 17554, 18716, 18868, 19784, 19920, 20953, 21714, 22682, 23702, 24933, 25818, 26195, 28828, 29302, 31133, 31302, 32567, 34383, 34528, 35330, 35514, 36937, 37988, 39970, 41252, 42989, 43924, 45547, 47177, 48473, 48620, 48785, 49937]
        timer = pygame.time.get_ticks()
        drawGame()
    
    if(one_drawn or two_drawn or three_drawn):
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
