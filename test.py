import pygame as pg
import random

questions = [ 
            [["pics/bg.png", 4],["pics/farm.png", 240]],
            [["pics/bg.png", 4],["pics/farm.png", 240]],
            [["pics/farm.png", 240],["bg.png", 4]],
            [["pics/bg.png", 4],["pics/farm.png", 240]],
            [["pics/farm.png", 240],["pics/bg.png", 4]]
            ]


pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


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



def main():
    bg = pg.image.load("pics/lemonade.png").convert()
    done = False
    lemonadestand = True
    output = None
    x = random.sample([1,2,3,4,0], 5)
    i = 0
    j = 0
    appear = True
    lemons = 0
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
                output =input_box.handle_event(event)

            	
            if output != None:
                if int(output) == questions[x[i]][j][1]:
                    lemons += 5
                    print "lemons: " + str(lemons)
                if j == 0:
                    j = 1
                    bg = pg.image.load(questions[x[i]][j][0]).convert()
                else:
                    j = 0
                    i+=1
                    lemonadestand = True
                    bg = pg.image.load("pics/lemonade.png").convert()
            	print output
                output = None
            input_box.update()

            # screen.fill((30, 30, 30))
            input_box.draw(screen)
            pg.display.flip()
            pg.display.update()

        else:
            if appear:
                cont = pg.image.load('pics/cont.png').convert()
                cont = pg.transform.scale(cont, (125,75))
                appear = False
            c = screen.blit(cont, (0, 400))   
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pg.mouse.get_pos()
                    if c.collidepoint(pos):
                        lemonadestand = False
                        appear = True
                        if i < 5:
                            bg = pg.image.load(questions[x[i]][0][0]).convert()
                        else:
                            print lemons
                            done = True

            pg.display.flip()
            pg.display.update()
if __name__ == '__main__':
    main()
    pg.quit()