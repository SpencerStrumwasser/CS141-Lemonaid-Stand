import pygame as pg
import random
import time

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

f= open("datacollection.txt","w+")

questions = [ 
            [["pics/bg.png", 4],["pics/farm2.png", 240]],
            [["pics/cityblock.png", 5],["pics/school.jpg", 8]],
            [["pics/farm2.png", 240],["pics/bg.png", 4]],
            [["pics/bg.png", 4],["pics/farm2.png", 240]],
            [["pics/farm2.png", 240],["pics/bg.png", 4]]
            ]


pg.init()
pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)
myfontquest = pg.font.SysFont('Comic Sans MS', 25)
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)

prize = pg.image.load('pics/prize.png').convert_alpha()
success = pg.image.load("pics/back3.jpg").convert()
lemonsold = pg.image.load("pics/lemonsold.png").convert()

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color, loc=(640*0.4, 40)):
    largeText = pg.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = loc
    screen.blit(TextSurf, TextRect)
    # pg.display.update()
    # time.sleep(2)
    return

def message_displaysmall(text, color, loc=(640*0.4, 40)):
    largeText = pg.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = loc
    screen.blit(TextSurf, TextRect)
    # pg.display.update()
    # time.sleep(2)
    return


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    temp = self.text
                    self.text = ''
                    self.txt_surface = FONT.render(self.text, True, self.color)
                    return temp
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)




class LemonadeStand:

    """ LemonadeStand class with three methods - make_lemonade, sell_lemonade, display_data.
    """

    def __init__(self):
        """ setup initial parameters. weather is randomized."""
        self.day = 0
        self.cash = 0
        self.lemonade = 10
        self.weather = random.randrange(50, 100)
        self.questions = 1
        self.first = 1

        
        

    def sell_lemonade(self, price):
        """ Sell lemonade that you have made previously. Bad weather and/or high price will discount net demand. """
        try:
            price = int(price)
        except ValueError:
            price = 10
        cups = random.randrange(1, 101)  # without heat or price factors, will sell 1-100 cups per day
        price_factor = float(100 - price) / 100  # 10% less demand for each ten cent price increase
        if price_factor < 0:
            price_factor = 0
        heat_factor = 1 - (((100 - self.weather) * 2) / float(100))  # 20% less demand for each 10 degrees below 100
        if price == 0:
            self.lemonade = 0  # If you set price to zero, all your lemonade sells, for nothing.
            print('All of your lemonade sold for nothing because you set the price to zero.')
            self.day += 1
            self.weather = random.randrange(50, 100)
        demand = int(round(cups * price_factor * heat_factor))
        if demand > self.lemonade:
            print(
                'You only have ' + str(self.lemonade) + ' cups of lemonade, but there was demand for ' + str(
                    demand) + '.')
            demand = self.lemonade
        revenue = demand * round((float(price) / 100), 2)
        self.lemonade -= demand
        self.cash += revenue
        self.day += 1
        self.weather = random.randrange(50, 100)
        print('You sold ' + str(demand) + ' cup(s) of lemonade and earned $' + str(revenue) + ' dollars!\n')
        return demand


def disp_success(num):
    screen.blit(success, (0, 0))
    screen.blit(prize, (240, 180))
    message_display('You got it right!', white)
    pg.display.flip()
    pg.display.update()
    pg.time.delay(1000)
    
    message_display('Rewards:            x5', white, (200, 400))
    message_displaysmall('Each Lemon Makes 3-5 cups of Lemonade!!', white, (250, 450))
    lemon_img = pg.image.load('pics/lemon1.png').convert_alpha() 
    lemon_sz = lemon_img.get_size()
    lemons = pg.transform.scale(lemon_img, (int(lemon_sz[0]*0.08), int(lemon_sz[1]*0.08)))
    screen.blit(lemons, (220, 340))
    pg.display.flip()
    pg.display.update()
    pg.time.delay(1500)



def disp_failure():
    screen.blit(success, (0, 0))
    message_display('You got it wrong', white)
    
    
    pg.display.flip()
    pg.display.update()
    pg.time.delay(1000)

    message_display('Better luck next time', white, (300, 300))
    
    pg.display.flip()
    pg.display.update()
    pg.time.delay(1500)

def disp_lemons(numsold, cash):
    screen.blit(lemonsold, (0, 0))
    if numsold > 1:
        message_display('Congrats you sold ' + str(numsold), blue, (300, 50))
        message_display('cups of lemonades', blue, (300, 100))
    elif numsold == 1:
        message_display('Congrats you sold ' + str(numsold), blue, (300, 50))
        message_display('cup of lemonade', blue, (300, 100))
    else:
        message_display("Oh no, you sold", blue, (300, 50)) 
        message_display("no lemonade today", blue, (300, 100))
    pg.display.flip()
    pg.display.update()
    pg.time.delay(1000)

    message_display('You earned ' + str(cash) + ' dollars', blue, (300, 300))
    
    pg.display.flip()
    pg.display.update()
    pg.time.delay(1500)


def main():
    bg = pg.image.load("pics/lemonade.png").convert()
    # testing 
    done = False
    lemonadestand = True
    output = None
    x = random.sample([1,2,3,4,0], 5)
    i = 0
    j = 0
    appear = True
    stand = LemonadeStand()
    while not done:

    	screen.blit(bg, (0, 0))
    	

        if not lemonadestand:
            if appear:
                button = pg.image.load('pics/hint.png').convert()
                button = pg.transform.scale(button, (25,25))
                input_box = InputBox(200, 400, 240, 32)
                appear = False
            b = screen.blit(button, (425, 400))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                	pos = pg.mouse.get_pos()
                	if b.collidepoint(pos):
                		print "hi"
                output = input_box.handle_event(event)

            	
            if output != None:
                try:
                    output = int(output)
                except ValueError:
                    pass
                if output == questions[x[i]][j][1]:
                    rewards = 5
                    for i in range(rewards):
                        stand.lemonade += random.randint(3,5)
                    print "lemons: " + str(stand.lemonade)
                    # testing
                    f.write(str(x[i]) + str(j) + " Correct \n")
                    disp_success(rewards)
                else:
                    disp_failure()
                    f.write(str(x[i]) + str(j) + "Wrong\n")
                if j == 0:
                    j = 1
                    bg = pg.image.load(questions[x[i]][j][0]).convert()
                else:
                    j = 0
                    i+=1
                    lemonadestand = True
                    appear = True
                    bg = pg.image.load("pics/lemonade.png").convert()
                output = None
            input_box.update()
            input_box.draw(screen)
            pg.display.flip()
            pg.display.update()

        else:
            if appear:
                textday = myfont.render('Day: ' + str(stand.day), False, (0, 0, 0))
                textcash = myfont.render('Cash: ' + str(stand.cash), False, (0, 0, 0))
                textweather = myfont.render('Degrees: ' + str(stand.weather), False, (0, 0, 0))
                textlemonade = myfont.render('Lemonade: ' + str(stand.lemonade), False, (0, 0, 0))
                textquestion1 = myfontquest.render('Enter the price you will sell', False, (0, 0, 0))
                textquestion2 = myfontquest.render('your lemonade for (in cents)', False, (0, 0, 0))
                input_box = InputBox(200, 440, 240, 32)
                appear = False 
            screen.blit(textday,(0,200))
            screen.blit(textweather,(0,240))
            screen.blit(textlemonade,(0,280)) 
            screen.blit(textcash,(0,320)) 
            screen.blit(textquestion1,(195,370))
            screen.blit(textquestion2,(195,400))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                output = input_box.handle_event(event)

            if output != None:
                current_cash = stand.cash
                lemons_sold = stand.sell_lemonade(output)
                cash_made = stand.cash - current_cash
                disp_lemons(lemons_sold, cash_made)
                lemonadestand = False
                appear = True
                if i < 5:
                    bg = pg.image.load(questions[x[i]][0][0]).convert()
                else:
                    print stand.lemonade
                    done = True
                output = None

            input_box.update()
            input_box.draw(screen)
            pg.display.flip()
            pg.display.update()
if __name__ == '__main__':
    main()
    pg.quit()