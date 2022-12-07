import pygame
import math
import random
from pygame.locals import *
vec = pygame.math.Vector2

MAXSPEED = 4
curLoc = 200, 200
setThrot = 0
curThrot = 0
setAngle = 0
setAngle2 = 0
curAngle = 0
speed = 0



class Tank(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/OrangeTank.png")
        self.ogimg = self.image
        self.position = vec(xpos, ypos)
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        global curLoc, setThrot, curThrot, setAngle, curAngle, speed

        self.dir = curAngle
        self.vel = vec( math.cos(math.radians(self.dir))*speed,
                        math.sin(math.radians(self.dir))*speed)
        self.position += self.vel
        curLoc = self.position
        self.rect.center = self.position
        self.image = pygame.transform.rotate(self.ogimg, -curAngle-90)
        self.rect = self.image.get_rect(center=self.rect.center)      


        if speed != MAXSPEED * setThrot/100:
            if speed < MAXSPEED * setThrot/100:
                speed += MAXSPEED/60
            if speed > MAXSPEED * setThrot/100:
                speed -= MAXSPEED/10
        if speed > MAXSPEED:
            speed = MAXSPEED
        if speed < 0:
            speed = 0

        if curAngle > setAngle:
            curAngle -= 2
            #print(angle)
        if curAngle < setAngle:
            curAngle += 2
            #print("poop")
        # keep angle within 0-360
        if curAngle > 360:
            curAngle -= 360
        if curAngle < 0:
            curAngle += 360


    def run(self):

        def start():
            global setThrot
            setThrot = 100

        def whatdo():
            global curLoc, setAngle, curAngle, setThrot
            x, y = curLoc

            if x > 550:
                setThrot = 0
                setAngle = 180
                if curAngle == 180:
                    setThrot = 100
            if x < 50:
                setThrot = 0
                setAngle = 0
                if curAngle == 0:
                    setThrot = 100
            

        start()

        whatdo()

        Tank.update(self)
