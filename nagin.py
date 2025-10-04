import pygame
import time
from pygame import mixer
import random
import sys



class game:
    #CONSTRUCTOR
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', 24)

        #SCREEN
        self.screensize = [700, 700]
        self.screen = pygame.display.set_mode(self.screensize)
        pygame.display.set_caption("game")

        #ALL VARIABLE FOR SHEAK
        self.body = 3
        self.blocksizex=25
        self.blocksizey=25
        self.sneak = []
        self.spositionx=[350,375,400]
        self.spositiony=[350,350,350]
        self.sbody = pygame.image.load("sneak.png")
        self.sbody=pygame.transform.scale(self.sbody,(self.blocksizex,self.blocksizey))
        self.sdx=-25
        self.sdy=0

        #ALL VARIABLE FOR APPLE
        self.apple=pygame.image.load("apple.png")
        self.apple=pygame.transform.scale(self.apple,(self.blocksizex,self.blocksizey))
        self.applex=random.randint(0,700)
        self.applex=(self.applex//25)*25
        self.appley = random.randint(0, 700)
        self.appley = (self.appley // 25) * 25

        self.score=0

        self.running = True


    #THE LOOP METHOD
    def run(self):
        while self.running:
            #APPENDING IMAGE FOR THE LENGTH OF BODY
            for i in range(self.body):
                self.sneak.append(self.sbody)

            self.screen.fill((0, 0, 0))

            #SCORE DISPLAY
            sc=self.font.render(f"score:{self.score}",True,(255,255,255))
            self.screen.blit(sc,(10,10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        self.sdy=0
                        self.sdx = 0
                        self.sdy=-self.blocksizey
                        mixer.Sound("move.wav").play()
                    if event.key==pygame.K_s:
                        self.sdy = 0
                        self.sdx = 0
                        self.sdy = self.blocksizey
                        mixer.Sound("move.wav").play()
                    if event.key==pygame.K_a:
                        self.sdx=0
                        self.sdy = 0
                        self.sdx=-self.blocksizex
                        mixer.Sound("move.wav").play()
                    if event.key==pygame.K_d:
                        self.sdx=0
                        self.sdy = 0
                        self.sdx = self.blocksizex
                        mixer.Sound("move.wav").play()

            #WHEN YOU EAT THE APPLE
            if self.spositionx[0] == self.applex and self.spositiony[0] == self.appley:
                mixer.Sound("eat.wav").play()
                self.score += 1
                self.body += 1
                self.spositionx.append(self.spositionx[-1])
                self.spositiony.append(self.spositiony[-1])
                self.applex = random.randint(0, 700)
                self.applex = (self.applex // 25) * 25
                self.appley = random.randint(0, 700)
                self.appley = (self.appley // 25) * 25




            #HOW THE SNEAK MOVES
            for i in reversed(range(1,self.body)):
                self.spositionx[i]=self.spositionx[i-1]
                self.spositiony[i]=self.spositiony[i-1]

            self.spositionx[0]+=self.sdx
            self.spositiony[0]+=self.sdy

            # IF COLLIDE
            if self.spositionx[0] > 700 or self.spositiony[0] > 700 or self.spositionx[0] < 0 or self.spositiony[0] < 0:
                for i in range(0, self.body):
                    self.spositiony[i] = 800
                self.applex = 800
                self.appley = 800
                self.font = pygame.font.Font('freesansbold.ttf', 100)
                sc = self.font.render(f"score:{self.score}", True, (255, 255, 255))
                self.screen.blit(sc, (200, 300))
                pygame.display.update()

                time.sleep(5)
                self.running = False

            for i in range(1, self.body):
                if self.spositionx[0] == self.spositionx[i] and self.spositiony[0] == self.spositiony[i]:
                    for i in range(0, self.body):
                        self.spositiony[i] = 800

                    self.applex = 800
                    self.appley = 800

                    self.font = pygame.font.Font('freesansbold.ttf', 100)
                    sc = self.font.render(f"score:{self.score}", True, (255, 255, 255))
                    self.screen.blit(sc, (200, 300))
                    pygame.display.update()

                    time.sleep(5)
                    self.running = False

            #APPLE BLIT
            self.screen.blit(self.apple,(self.applex,self.appley))



            #SHOING THE SNEAK
            for i in range(self.body):
                self.screen.blit(self.sbody, (self.spositionx[i],self.spositiony[i]))



            pygame.display.update()
            time.sleep(0.25)


# game
game().run()