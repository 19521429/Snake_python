import pygame,random,time,sys
import tkinter as tk
from tkinter import messagebox

black = 52, 73, 94
white = 236, 240, 241
red = 231, 76, 60
green = 22, 160, 133
blue = 0, 0, 255
wetalpha = 52, 73, 94


class Snake_game:
    def __init__(self):
        pygame.init()
        self.score  = 0
        self.left = 20
        self.top = 40
        self.width  = 800
        self.height = 600
        self.minwidth = 400
        self.minheight = 200
        self.speed = 1
        self.maxspeed = 7
        self.px = 20 # 20pixel
        self.snakepos = [100,60]
        self.snakebody = [[100,60],[80,60],[60,60]]
        self.fpos = [0,0]
        self.IMG_Food = pygame.transform.scale(pygame.image.load('apple.png'),(self.px,self.px))
        self.IMG_head = pygame.transform.scale(pygame.image.load('head.png'),(self.px,self.px))
        self.IMG_body = pygame.transform.scale(pygame.image.load('body.png'),(self.px,self.px))
        self.Eat_sound = pygame.mixer.Sound('Eat.mp3')
        self.Lose_sound = pygame.mixer.Sound('Lose.mp3')
        self.direction = 'RIGHT' #hướng di chuyển của rắn, mặc định theo game snake sẽ đi từ trái sang phải
        self.move = 'RIGHT'
        self.Have_Food = False
        self.start()

    def start(self):
        self.setTitle('Snake')
        self.setWindow(self.width,self.height)
        self.DrawFood()

    def drawline(self,left,top,width,height):# vẽ đường viền
        pygame.draw.rect(self.window,white,(left,top,width,height),2)
    
    def setScore(self, s):
        self.score = s

    def message_box(self,subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        msg = messagebox.askyesno(subject, content)
        if(msg):
            try:
                root.destroy()
                self.replay()
            except:
                pass
        else:
            pygame.quit()
            sys.exit()

    def replay(self):
        self.snakepos = [100,60]
        self.snakebody = [[100,60],[80,60],[60,60]]
        self.direction = 'RIGHT'
        self.move = 'RIGHT'
        self.score = 0
        self.speed = 1
        self.width = 800
        self.height = 600
        self.setWindow(self.width,self.height)
        self.start()

    def gameover(self):
        time.sleep(3)
        self.Lose_sound.play()
        self.window.fill(black)
        gfont = pygame.font.SysFont('Arial',60)
        msg = 'YOU LOSE'
        gsurf = gfont.render(msg,True,green)
        grect = gsurf.get_rect()
        grect.midtop = (self.width/2 - 30 , self.height /2 - 40)
        self.window.blit(gsurf,grect)

        gfont = pygame.font.SysFont('Arial',30)
        score = 'SCORE : ' + str(self.score)
        gsurf = gfont.render(score,True,white)
        grect = gsurf.get_rect()
        grect.midtop = (self.width/2 - 20 , self.height /2 + 30)
        self.window.blit(gsurf,grect)
        pygame.display.flip()

        self.message_box('OH No !!!', 'You lose. Do you want to play again ?')

        

    def displayscore(self):
        sfont = pygame.font.SysFont('Arial',20)
        ssurf = sfont.render('Score : ' + str(self.score) + ' Level : ' + str(self.speed) ,True, white)
        srect = ssurf.get_rect()
        self.window.blit(ssurf,srect)

    def setTitle(self,title):
        pygame.display.set_caption(title)

    def setWindow(self,width,height):
        self.window = pygame.display.set_mode((width,height))

    def DrawFood(self):
        if self.Have_Food == False :
            fx = random.randrange((self.left + 20) / 10, (self.width - self.left - 20)/10)
            fy = random.randrange((self.top  + 20) / 10, (self.height - self.top - 20)/10)
            if fx % 2 != 0: fx += 1
            if fy % 2 != 0: fy += 1
            self.fpos = [fx * 10, fy * 10]
        self.Have_Food = True

    def render(self):
        for pos in self.snakebody: # render ra thân rắn
            self.window.blit(self.IMG_body,pygame.Rect(pos[0],pos[1],20,20))
        self.window.blit(self.IMG_head,pygame.Rect(self.snakebody[0][0],self.snakebody[0][1],20,20))
        self.window.blit(self.IMG_Food,pygame.Rect(self.fpos[0],self.fpos[1],self.px,self.px))
        
        
    def refresh(self):
        self.window.fill(wetalpha)

    def resetpos(self):
        if self.speed < 7: # chiều dài thân rắn > chiều dài của window
            lenght = len(list(self.snakebody))
            self.snakepos[0] = self.left + lenght * 20
            self.snakepos[1] = self.top + 20
            self.snakebody[0][0] = self.snakepos[0]
            self.snakebody[0][1] = self.snakepos[1]
            temp = 1
            for i in self.snakebody[1:]:
                i[0] = self.snakepos[0] - temp * 20
                i[1] = self.snakepos[1] # nối đuôi vào đầu
                temp += 1
        else:
            lenght = len(list(self.snakebody))
            self.snakepos[0] = self.left + lenght * 20
            self.snakepos[1] = self.top + 20
            self.snakebody[0][0] = self.snakepos[0]
            self.snakebody[0][1] = self.snakepos[1]
            temp = 1
            for i in self.snakebody[1:]:
                i[0] = self.snakepos[0] - temp * 20
                i[1] = self.snakepos[1] # nối đuôi vào đầu
                temp += 1

        self.move = 'RIGHT'
        self.direction = self.move
        self.setWindow(self.width,self.height)



    