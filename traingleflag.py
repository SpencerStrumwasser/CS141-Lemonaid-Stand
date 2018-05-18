import pygame
import time 

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

pygame.init()
# display_width = 500
# display_height = 400
display_width = 640
display_height = 480

def display(sprite, x,y):
    gameDisplay.blit(sprite, (x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color, loc=(display_width*0.6, 40)):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = loc
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    # time.sleep(2)
    return

def clear(): 
    pygame.draw.rect(gameDisplay, green, [100, 0, display_width, 100])

def paint_get(): 
    clear()
    message_display('You Added Paint!', black)

def paint_put(): 
    clear()
    message_display('You Got Paint', black)

def print_score(score):
    pygame.draw.rect(gameDisplay, green, [0, display_height-60, 160, 600])
    message_display('Score: '+str(score), black, (80, display_height-20))

def paint_box(x, y, x_width, y_width): 
    rb_img = pygame.image.load('pics/redbrush.png').convert_alpha()
    rb_size = rb_img.get_size() 
    redbrush = pygame.transform.scale(rb_img, (int(rb_size[0]*0.5), int(rb_size[1]*0.5)))
    pygame.draw.rect(gameDisplay, red, [x, y, x_width, y_width])
    display(redbrush, x+4, y+4)

def flag(x, y, x_width, y_width): 
    sc_img = pygame.image.load('pics/flag.jpg').convert_alpha() 
    sc_size = sc_img.get_size()
    shopcart = pygame.transform.scale(sc_img, (int(sc_size[0]*0.1), int(sc_size[1]*0.1))) 
    pygame.draw.rect(gameDisplay, black, [x, y, x_width, y_width])
    display(shopcart, x+4, y+4)

def door(x, y): 
    door_img = pygame.image.load('pics/door.png').convert_alpha()
    door_size = door_img.get_size()
    door = pygame.transform.scale(door_img, (int(door_size[0]*0.5), int(door_size[1]*0.5)))
    display(door, x, y)

def game_loop():
    # x =  (display_width * 0.45)
    # y = (display_height * 0.8)
    x =  100
    y = 200
    score = 0
    gameDisplay.fill(white)
    x_change = 0
    y_change = 0
    clock = pygame.time.Clock()
    gameExit = False
    door_loc = (425, 135)
    f_loc = (display_width-200, display_height-200) # (386, 316)
    f_dim = (150, 120)
    buff = 10
    # flag(f_loc[0], f_loc[1], f_dim[0], f_dim[1])
    door(door_loc[0], door_loc[1])


    prize = pygame.image.load('pics/prize.png').convert_alpha()
    bg = pygame.image.load("pics/back1.jpg").convert()
    gameDisplay.blit(bg, (0, 0))
    gameDisplay.blit(prize, (240, 180))
    message_display('Rewards:            x5', white, (200, 400))
    lemon_img = pygame.image.load('pics/lemon1.png').convert_alpha() 
    lemon_sz = lemon_img.get_size()
    lemons = pygame.transform.scale(lemon_img, (int(lemon_sz[0]*0.08), int(lemon_sz[1]*0.08)))
    gameDisplay.blit(lemons, (220, 340))
    pygame.display.flip()
    pygame.display.update()



    # pygame.time.delay(2000)
    # display(prize, 100, 100)
    gotpaint = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP: 
                    y_change = -5
                elif event.key == pygame.K_DOWN: 
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                    y_change = 0

        # # (100, 5), (10, 95)
        # if y <= paint_loc[1]+paint_dim[1]+buff and x <= paint_loc[0]+paint_dim[0]+buff and gotpaint == False:
        #     paint_get()
        #     gotpaint = True
        # # (300, 265), (405, 200) 
        # # y>= 306 and x>= 376
        # if y >= display_height-200 and x >= display_width-200:
        #     if gotpaint == True:
        #         score += 1 
        #         gotpaint = False
        #         paint_put()
        #         print_score(score)
        if x >= 340 and (y >= 135 or y<= 215):
            pygame.quit()
            quit()
        if x < 5:
            # gameExit = True
            x_change = 10
            message_display('Avoid the fence!', black)
        elif  x > display_width - s1_size[0]*0.2 :
            # gameExit = True
            x_change = -10
            message_display('Avoid the fence!', black)
        x += x_change
        y += y_change
        display(sprite1,x,y)

        pygame.display.update()
        flag(f_loc[0], f_loc[1], f_dim[0], f_dim[1])
        clock.tick(30)
        # print(clock)
        # print(x, y)
if __name__ == '__main__':
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Painting a House')

    s1_img = pygame.image.load('pics/sprite1.png').convert_alpha()
    # s1_img = pygame.image.load('pics/sprite2.gif').convert_alpha()
    s1_size = s1_img.get_size() 
    sprite1 = pygame.transform.scale(s1_img, (int(s1_size[0]*0.2), int(s1_size[1]*0.2)))

    game_loop()
    pygame.quit()
    quit()