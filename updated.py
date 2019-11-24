#fts Faisal Abdelmonem

import pygame
import random

################################ CLASSES ######################################

class spaceship():
    def __init__(self,ship,x,y,width,height):
        self.x = x
        self.y = y
        self.vel = 15
        self.width = width
        self.height = height
        self.ship = pygame.transform.scale(ship,(self.width,self.height))
        self.lives = 3
        self.alive = True
        self.shottimer = 0
        
    #here the spaceship is drawn
    def draw(self,win):
        if self.alive:
            win.blit(self.ship,(self.x,self.y))

    #when damage is received
    def damaged(self):
        self.lives -= 1
        if self.lives == 0:
            self.alive = False


class bullet():
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 15
        self.evel = 20

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class enemySpaceships():
    def __init__(self,s,x,y,width,height,bots):
        self.bots = bots
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.s = pygame.transform.scale(s,(self.width,self.height))
        self.right = True
        self.left = False
        self.bullets = []
        self.bulvel = 20
        self.bulCount = 0
        self.timer = 0

    def drawUFO(self,win):
        if self.timer > 0:
            self.timer += 1
        if self.timer > 10:
            self.timer = 0
        if self.x >= self.width//2 and self.right:
            self.x += self.vel
            if self.x > w - 2*self.width:
                for j in self.bots:
                    j.right = False
                    j.left = True
        elif self.x <= w - self.width//2 and self.left:
            self.x -= self.vel
            if self.x < self.width:
                for j in self.bots:
                    j.left = False
                    j.right = True
        for shooter in self.bots:
            if abs(shooter.x - rocky.x) < 25 and self.bulCount < 1 and self.timer == 0:
                self.bulCount += 1
                self.bullets.append(bullet(round(shooter.x + shooter.width//2),round(shooter.y + shooter.height//2),9,(200,200,0)))
                self.timer = 1
        for ebul in self.bullets:
            if ebul.y < h - rocky.height:
                ebul.y += ebul.evel
            elif ebul.y >= h - rocky.height:
                if ebul in self.bullets:
                    self.bullets.remove(ebul)
                    self.bulCount -= 1
            if rocky.x < ebul.x < rocky.x + rocky.width and rocky.y < ebul.y < rocky.y + rocky.height:
                rocky.damaged()
                if ebul in self.bullets:
                    self.bullets.remove(ebul)
                    self.bulCount -= 1

        win.blit(self.s,(self.x,self.y))

class button():
    def __init__(self,color,x,y,width,height,text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win):
        if self.text != "":
            font = pygame.font.SysFont("arial",60)
            Text = font.render(self.text, 1, self.color)
            window.blit(Text,(self.x + (self.width/2 - Text.get_width()/2),self.y + (self.height/2 - Text.get_height()/2)))

    def isHovering(self,pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False

############################# ALL MY INITIALIZATIONS WILL BE HERE ########################

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("initial screen")
bg = pygame.image.load("SpaceBackground.jpg")
font = pygame.font.SysFont("arial",80)
playButton = button((0,0,100),150,400,150,100,"play game :)")
leaveButton = button((0,0,100),450,400,250,100,"leave game :(")
win = pygame.display.set_mode((800,600))
h = win.get_height()
w = win.get_width()
pygame.display.set_caption("Game")
bullets = []
rocky = spaceship(pygame.image.load("spaceship.png"),180,450,50,50)



################################### HELPER FUNCTIONS ##########################
def generateBots(num):
    bots = []
    while len(bots) < num:
        x = random.randint(50,400)
        y = random.randint(50,200)
        for b in bots:
            while abs(x - b.x) < 50:
                x = random.randint(50,400)
        bots.append(enemySpaceships(pygame.image.load("sprite.png"),x,y,70,40,bots))
    return bots            

def moveSpaceship(keys):
    if rocky.shottimer > 0:
        rocky.shottimer += 1
    if rocky.shottimer > 10:
        rocky.shottimer = 0
    if keys[pygame.K_SPACE] and rocky.shottimer == 0:
        if len(bullets) < 5:
            bullets.append(bullet(round(rocky.x+rocky.width//2),rocky.y,5,(0,0,255)))
            shottimer = 1
    if keys[pygame.K_LEFT]:
        if rocky.x > rocky.width:
            rocky.x -= rocky.vel
    if keys[pygame.K_RIGHT]:
        if rocky.x < w-2*rocky.width:
            rocky.x += rocky.vel
    if keys[pygame.K_UP]:
        if rocky.y > rocky.height:
            rocky.y -= rocky.vel
    if keys[pygame.K_DOWN]:
        if rocky.y < h-2*rocky.height:
           rocky.y += rocky.vel

def drawWind(bots):
    win.blit(bg,(0,0))
    rocky.draw(win)
    for j in bots:
        j.drawUFO(win)
        for ebul in j.bullets:
            ebul.draw(win)
    for bul in bullets:
        bul.draw(win)
    pygame.display.update()

def intro():
    intro = True
    while intro:
        pygame.time.delay(50)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.isHovering(pos):
                    intro = False
                    gameloop()
                if leaveButton.isHovering(pos):
                    intro = False
            if event.type == pygame.MOUSEMOTION:
                if playButton.isHovering(pos):
                    playButton.color = (175,200,0)
                else:
                    playButton.color = (0,0,100)
                if leaveButton.isHovering(pos):
                    leaveButton.color = (255,0,0)
                else:
                    leaveButton.color = (0,0,100)
                
        messageOnScreen(window,"Welcome to my game", (0,125,125),100,100)
        playButton.draw(window)
        leaveButton.draw(window)
        pygame.display.update()

def messageOnScreen(win,msg,color,x,y):
    Text = font.render(msg, 1, color)
    window.blit(Text,(x,y))
    win.blit(Text,(x,y))

def checkForBullets(bots):
    for bul in bullets:
        if bul.y > 50:
            bul.y -= bul.vel
        else:
            if bul in bullets:
                bullets.remove(bul)
        for bot in bots:
            if bot.x < bul.x < bot.x + bot.width and bot.y < bul.y < bot.y + bot.height:
                if bot in bots:
                    bots.remove(bot)
                if bul in bullets:
                    bullets.remove(bul)
                
    for bot in bots:
        if bot.y <= rocky.y <= bot.y + bot.height and bot.x <= rocky.x <= bot.x + bot.width:
            if bot in bots:
                bots.remove(bot)

def gameloop():
    bots = generateBots(5)
    run = True
    while run:
        pygame.time.delay(50)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        checkForBullets(bots)
        moveSpaceship(keys)
        messageOnScreen(win,"lives: " + str(rocky.lives),(255,255,255),25,25)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
        drawWind(bots)
        pygame.display.update()

#################################### MAINLOOP #################################

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(bg,(0,0))
    intro()
    run = False
    pygame.display.update()
    
pygame.quit()





        

