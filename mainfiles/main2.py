import pygame
import time
import random

pygame.init()

#############
crash_sound = pygame.mixer.Sound("cough.wav")
#############
 
display_width = 1500
display_height = 750
adjF = 30
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
car_width = 73
car_height = 73
 
#gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay = pygame.display.set_mode((display_width,display_height))


background = pygame.transform.scale(pygame.image.load('bg.jpeg'), (display_width, display_height))
background_size = background.get_size()
background_rect = background.get_rect()



pygame.display.set_caption('Mic, The Panda')
clock = pygame.time.Clock()
 
carImg = pygame.image.load('car.png')
gameIcon = pygame.image.load('car.png')

objectImgs = []

covidImg = pygame.image.load('covid.png')
vaccineImg = pygame.image.load('covaxin.png')
oxygenImg = pygame.image.load('oxy.png')




objectImgs.append(covidImg)
objectImgs.append(vaccineImg)
objectImgs.append(oxygenImg)

objectImgs[0] = pygame.transform.scale(covidImg, (100, 100))
objectImgs[1] = pygame.transform.scale(vaccineImg, (100, 100))
objectImgs[2] = pygame.transform.scale(oxygenImg, (100, 100))


pygame.display.set_icon(gameIcon)

pause = False
#crash = True
 
def things_dodged(count,vac,oxy):
    
    if(oxy<50):
    	font = pygame.font.SysFont("comicsansms", 45)
    	text = font.render("Fought: "+str(count)+" | Power: "+str(int(vac))+" | Oxygen: "+str(int(oxy)), True, red)
    else:
    	font = pygame.font.SysFont("comicsansms", 35)
    	text = font.render("Fought: "+str(count)+" | Power: "+str(int(vac))+" | Oxygen: "+str(int(oxy)), True, white)
    gameDisplay.blit(text,(0,0))
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

'''
def covid(x,y):
    gameDisplay.blit(covidImg,(x,y))

def vaccine(x,y):
    gameDisplay.blit(vaccineImg,(x,y))
'''


def buildImg(objectImg,x,y):
    gameDisplay.blit(objectImg,(x,y))



 
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
 
 
def crash(count):
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Khatam Tata Baye Baye", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    mediumText = pygame.font.SysFont("comicsansms",75)
    TextSurf, TextRect = text_objects("Score: "+str(count), mediumText)
    TextRect.center = ((display_width/2),(display_height/2)+100)
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        #button("Play Again",450,450,100,50,green,bright_green,game_loop)
        button("Quit",(display_width/2)-50,(display_height/2)+150,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",450,450,100,50,green,bright_green,unpause)
        button("Quit",900,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Mic, The Panda", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",450,450,100,50,green,bright_green,game_loop)
        button("Quit",900,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global pause
    ############
    pygame.mixer.music.load('breath.wav')
    pygame.mixer.music.play(-1)
    ############
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    
    wi,hi = background_size
    xi = 0
    yi = 0

    x1i = 0
    y1i = -hi

 
    x_change = 0
    
    thing_startx = random.randrange(0, display_width-100)
    thing_starty = -600
    thing_speed = 4
    thing_width_default = 100
    thing_widthC = 100
    thing_height_default = 100
    thing_heightC = 100
    
    cheezein = []
    typ = random.randrange(0, 3)
    chze = {'thing_starty': thing_starty, 'thing_startx': thing_startx, 'typ': typ}
    cheezein.append(chze)
 
    chrashed = False;
    thingCount = 1
 
    rr=255
    gg=255
    bb=255
    
    doVacZero = 0
    doOxyZero = 0;
    dodged = 0
    vac = 0
    vacReducer = 0.5
    oxy = 100
    oxyReducer = 0.005
    multiplier = 1
 
    gameExit = False
 
    while not gameExit:
 
        #moving background
        y1i += 5
        yi += 5
        gameDisplay.blit(background,(xi,yi))
        gameDisplay.blit(background,(x1i,y1i))
        if yi > hi:
            yi = -hi
        if y1i > hi:
            y1i = -hi
        #moving background ends
        
        
        
        
        
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -(5*1.5)
                if event.key == pygame.K_RIGHT:
                    x_change = (5*1.5)
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        
        
        car(x,y)
        vac = vac - vacReducer
        oxy = oxy - oxyReducer
        if(vac<0):
        	vac=0;
        if(oxy<=0):
        	crash(dodged);
        	
        things_dodged(dodged,vac,oxy)
 
        
        if x > display_width - car_width or x < 0:
            crash(dodged)
 
        
        #things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        '''
        if(typeOfVastu==0):
        	covid(thing_startx,thing_starty);
        elif(typeOfVastu==1):
        	vaccine(thing_startx,thing_starty);
        '''
        
        #covid(thing_startx,thing_starty);
 
        
        thing_starty += thing_speed
        
        for obj in cheezein:
            thing_starty = obj['thing_starty']
            thing_startx = obj['thing_startx']
            typ = obj['typ']
            
            if(typ==0):
                thing_width = thing_widthC
                thing_height = thing_heightC
            else:
                thing_width = thing_width_default
                thing_height = thing_height_default

            
            buildImg(objectImgs[typ],thing_startx,thing_starty)
            obj['thing_starty'] += (thing_speed * random.randrange(1,3))
            
            
            if thing_starty > display_height:
                cheezein.remove(obj)
                chrashed = False;
                thing_speed += 0.1
                if(typ == 0):
                	thing_widthC += (dodged * 1.005)
                	thing_heightC += (dodged * 1.005)
                	multiplier = multiplier+0.02
                	objectImgs[typ] = pygame.transform.scale(covidImg, (int(thing_widthC), int(thing_heightC)))
                	
                
                
                if(doVacZero == 1):
                	vac = 0
                	doVacZero = 0
                if(doOxyZero == 1):
                	oxyReducer = oxyReducer*multiplier
                	doOxyZero = 0
                #if(typ == 0):
                #	dodged += 1
                
                newVastu = random.randrange(1, 3)
                for i in range(newVastu):
                    if(len(cheezein)>3):
                        break
                    typ = random.randrange(0, 3)
                    if(typ == 0):
                    	thing_width = thing_widthC
                    	thing_height = thing_heightC
                    else:
                    	thing_width = thing_width_default
                    	thing_height = thing_height_default
                    	
                    thing_starty = 0 - thing_height
                    thing_startx = random.randrange(0,int(display_width-thing_width))
                    
                    chz = {'thing_starty': thing_starty, 'thing_startx': thing_startx, 'typ': typ}
                    cheezein.append(chz)
     
            if y < thing_starty+thing_height - adjF and y + car_height > thing_starty:
                print('y crossover')
     
                if(x>thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width):
                    #cheezein.remove(obj)
                    obj['thing_starty'] = display_height+1
                    #chrashed = True
                    #Virus#
                    pygame.mixer.music.load('cough.wav')
                    pygame.mixer.music.play()
                    if typ==0:
                        doVacZero = 1
                        dodged += 1
                        print('x crossover')
                        if(vac==0):
                        	if(oxy>0):
                        		doOxyZero = 1
                        	else:
                        		crash(dodged)
		            
                    #Vaccine#
                    elif typ==1:
                        vac = 100
                        oxy = 100
                        oxyReducer = 0.002
                        print('Vaccine')
                        pygame.mixer.music.load('yeah.wav')
                        pygame.mixer.music.play()
		            
                    #Oxygen#
                    elif typ==2:
                        oxy = 100
                        oxyReducer = 0.002
                        print('Oxygen')
                        pygame.mixer.music.load('yeah.wav')
                        pygame.mixer.music.play()
            
            
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
