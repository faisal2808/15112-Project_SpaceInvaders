#fts Faisal Abdelmonem

import pygame
import random
from functools import *

################################ CLASSES ######################################

#this is the spaceship class where the object is created and the parameters are
#initialized based on it's width height and the position where it starts
#the object is also initialized a predetermined velocity and a total of 3 lives
class spaceship():
    def __init__(self,ship,x,y,width,height):
        self.bullets = []
        self.x = x
        self.y = y
        self.vel = 15
        self.width = width
        self.height = height
        self.ship = pygame.transform.scale(ship,(self.width,self.height))
        self.lives = 3
        self.alive = True
        self.shottimer = 0
        self.level = 1
        self.score = 0
        
    #here the spaceship is drawn
    def draw(self,win):
        if self.alive:
            win.blit(self.ship,(self.x,self.y))

    #when damage is received
    def damaged(self):
        self.lives -= 1
        if self.lives == 0:
            self.alive = False

#this is the bullet class where when the object is made the input given is its position
#and its color and radius
class bullet():
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 15
        self.evel = 20

    #this draws the bullets as circles
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

#this is the class that is responsible of controlling the boss
#the functions in it are explained below
class Boss():
    def __init__(self,image,x,y,width,height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image,(self.width,self.height))
        self.alive = True
        self.vel = 20
        self.bulCount = 0
        self.bullets = []
        self.damaged = False
        self.dropped = False
        
    #this function will make the boss move and check if it is alive
    #if the boss dies it goes to the next level
    #while it is alive it will avoid the bullets and shoot at you
    def moveBoss(self,win):
        if rocky.x < self.x + 80:
            self.x -= self.vel
        if rocky.x > self.x + self.width//2:
            self.x += self.vel
        for b in rocky.bullets:
            if rocky.x < self.x + 50 and self.x + 50 < b.x < self.x + self.width//2 + 70:
                self.x += self.vel
            if self.x < self.width and self.x + 50 < b.x < self.x + self.width//2 + 70:
                self.x += self.vel
            if rocky.x > self.x + self.width//2 + 40 and self.x + 50 < b.x < self.x + self.width//2 + 70:
                self.x -= self.vel
            if self.x > w - self.width and self.x + 50 < b.x < self.x + self.width//2 + 70:
                self.x -= self.vel
            if self.x + 70 < b.x < self.x + self.width//2 + 50 and self.y + self.height - 40 > b.y > self.y:
                if b in rocky.bullets:
                    rocky.bullets.remove(b)
                    self.damaged = True                   
        self.attack(win)

    #this function is responsible for the boss's attacks once it detects
    #the object within it's range it will shoot at it
    def attack(self,win):
        if self.bulCount < 1:
            self.bulCount += 1
            self.bullets.append(bullet(round(self.x + self.width//2),round(self.y + self.height//2),15,(200,200,200)))
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

        win.blit(self.image,(self.x,self.y))

#this class is responsible for the enemy spaceships that attack the user their
#images are the same but the positions are randomly assigned and the way they
# attack is based on their position relative to the user and one bot touches
# the end of the screen they all change direction
class enemySpaceships():
    def __init__(self,s,x,y,width,height,bots):
        self.bots = bots
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5 + rocky.level
        self.s = pygame.transform.scale(s,(self.width,self.height))
        self.right = True
        self.left = False
        self.bullets = []
        self.bulvel = 15 + rocky.level
        self.bulCount = 0
        self.timer = 0

    #this function draws the bots and moves them and makes them shoot
    #if the user is in the range
    def drawUFO(self,win):
        if self.x >= self.width//2 and self.right:
            self.x += self.vel
            if self.x >= w - 2*self.width:
                for j in self.bots:
                    j.right = False
                    j.left = True
        elif self.x <= w - self.width//2 and self.left:
            self.x -= self.vel
            if self.x <= self.width:
                for j in self.bots:
                    j.left = False
                    j.right = True

        self.attack(win)

    #this controls the attacks of the bots
    def attack(self,win):
        if abs(self.x - rocky.x) < 25 and self.bulCount < 1:
            self.bulCount += 1
            self.bullets.append(bullet(round(self.x + self.width//2),round(self.y + self.height//2),9,(200,200,0)))
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

#this class is responsible for any buttons i might need within the game
class button():
    def __init__(self,color,x,y,width,height,text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    #draws the button
    def draw(self,win):
        if self.text != "":
            font = pygame.font.SysFont("arial",60)
            Text = font.render(self.text, 1, self.color)
            win.blit(Text,(self.x + (self.width/2 - Text.get_width()/2),self.y + (self.height/2 - Text.get_height()/2)))

    #if the mouse is above the button it returns true
    def isHovering(self,pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False

############################# ALL MY INITIALIZATIONS WILL BE HERE ########################

pygame.init()

#this game is created on an 800x600 window so please
#make sure it is like that before running it :)
bg = pygame.image.load("SpaceBackground.jpg")
playButton = button((0,0,100),150,400,150,100,"play game :)")
leaveButton = button((0,0,100),450,400,250,100,"leave game :(")
HowButton = button((0,255,0),300,300,200,100,"how to play")
backButton = button((0,255,0),300,450,200,100,"go back")
playAgain = button((0,0,100),150,400,150,100,"play again :)")
win = pygame.display.set_mode((800,600))
h = win.get_height()
w = win.get_width()
pygame.display.set_caption("Game")
#there are other sprites if you want to use them change the name here
rocky = spaceship(pygame.image.load("spaceship.png"),180,450,50,50)
boss = Boss(pygame.image.load("boss.png"),150,100,250,150)


################################### HELPER FUNCTIONS ##########################

#this generates the given number of bots
def generateBots(num):
    bots = []
    while len(bots) < num:
        x = random.randint(50,400)
        y = random.randint(50,200)
        for b in bots:
            while abs(x - b.x) < 25:
                x = random.randint(50,400)
        bots.append(enemySpaceships(pygame.image.load("sprite.png"),x,y,70,40,bots))
    return bots            

#this function moves the spaceship when the arrow keys are pressed and shoots
#if the spacebar is pressed
def moveSpaceship(keys):
    for bul in rocky.bullets:
        if bul.y > 50:
            bul.y -= bul.vel
        else:
            if bul in rocky.bullets:
                rocky.bullets.remove(bul)
    if keys[pygame.K_SPACE]:
        if len(rocky.bullets) < 5:
            rocky.bullets.append(bullet(round(rocky.x+rocky.width//2),rocky.y,5,(0,0,255)))
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

#this function draws the window where the game is played
def drawWin():
    win.blit(bg,(0,0))
    rocky.draw(win)
    boss.moveBoss(win)
    for ebul in boss.bullets:
        ebul.draw(win)
    for bul in rocky.bullets:
        bul.draw(win)
    pygame.display.update()

        
#this function draws the window where the game is drawn when the gameloop is run
def drawWind(bots):
    win.blit(bg,(0,0))
    rocky.draw(win)
    for j in bots:
        j.drawUFO(win)
        for ebul in j.bullets:
            ebul.draw(win)
    for bul in rocky.bullets:
        bul.draw(win)
    pygame.display.update()
        

#this is the intro loop that introduces the user to the game
def intro():
    win.blit(bg,(0,0))
    intro = True
    GameStart = False
    rules = False
    while intro:
        pygame.time.delay(50)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.isHovering(pos):
                    intro = False
                    GameStart = True
                if leaveButton.isHovering(pos):
                    intro = False
                if HowButton.isHovering(pos):
                    intro = False
                    rules = True
            if event.type == pygame.MOUSEMOTION:
                if playButton.isHovering(pos):
                    playButton.color = (175,200,0)
                else:
                    playButton.color = (0,0,100)
                if leaveButton.isHovering(pos):
                    leaveButton.color = (255,0,0)
                else:
                    leaveButton.color = (0,0,100)
                if HowButton.isHovering(pos):
                    HowButton.color = (0,0,255)
                else:
                    HowButton.color = (0,255,0)
                    
        messageOnScreen(win,"Tartvaders", (0,125,125),250,100,90)
        HowButton.draw(win)
        playButton.draw(win)
        leaveButton.draw(win)
        pygame.display.update()
    if GameStart:
        showLevel()
    elif rules:
        instructions()

#this loop takes you to the how to play menu where you can read the instructions
# and go back with the go bck button
def instructions():
    viewing = True
    back = False
    win.blit(bg,(0,0))
    while viewing:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                viewing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.isHovering(pos):
                    viewing = False
                    back = True
            if event.type == pygame.MOUSEMOTION:
                if backButton.isHovering(pos):
                    backButton.color = (0,0,255)
                else:
                    backButton.color = (0,255,0)
                
            
        messageOnScreen(win,"how to play", (255,0,0),200,100,100)
        messageOnScreen(win,"use the arrow keys to move", (0,0,255),150,225,50)
        messageOnScreen(win,"use the spacebar to shoot", (0,0,255),150,300,50)
        backButton.draw(win)
        pygame.display.update()
    if back:
        intro()

#this loop is run once the user leaves the game or loses
def outro():
    outro = True
    while outro:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                outro = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playAgain.isHovering(pos):
                    outro = False
                    rocky.lives = 3
                    rocky.alive = True
                    rocky.level = 1
                    rocky.score = 0
                    gameloop()
                if leaveButton.isHovering(pos):
                    outro = False
            if event.type == pygame.MOUSEMOTION:
                if playAgain.isHovering(pos):
                    playAgain.color = (175,200,0)
                else:
                    playAgain.color = (0,0,100)
                if leaveButton.isHovering(pos):
                    leaveButton.color = (255,0,0)
                else:
                    leaveButton.color = (0,0,100)
                
        messageOnScreen(win,"Gameover", (255,0,0),250,100,100)
        messageOnScreen(win,"score: " + str(rocky.score), (255,255,255),250,300,75)
        playAgain.draw(win)
        leaveButton.draw(win)
        pygame.display.update()

#this is called if a message is wanted to be displayed
def messageOnScreen(win,msg,color,x,y,size):
    font = pygame.font.SysFont("arial",size)
    Text = font.render(msg, 1, color)
    win.blit(Text,(x,y))

#here we check if the bullets hit the bots
def checkForBullets(bots):
    for bul in rocky.bullets:
        for bot in bots:
            if bot.x < bul.x < bot.x + bot.width and bot.y < bul.y < bot.y + bot.height:
                if bot in bots:
                    bots.remove(bot)
                    rocky.score += 10
                if bul in rocky.bullets:
                    rocky.bullets.remove(bul)
                    
    for bot in bots:
        if bot.y <= rocky.y <= bot.y + bot.height and bot.x <= rocky.x <= bot.x + bot.width:
            if bot in bots:
                bots.remove(bot)
                rocky.damaged

#this shows the level once all the UFO's are destroyed
def showLevel():
    win.blit(bg,(0,0))
    messageOnScreen(win,"level " + str(rocky.level),(255,255,255),300,250,100)
    pygame.display.update()
    pygame.time.delay(750)
    gameloop()

#here the gameloop is called
def gameloop():
    fightingBoss = False
    num = rocky.level%5
    if num == 0:
        fightingBoss = True
    if not fightingBoss:
        bots = generateBots(num + 4)
    newLevel = False
    run = True
    while run and rocky.lives > 0:
        pygame.time.delay(50)
        keys = pygame.key.get_pressed()
        moveSpaceship(keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
        if not fightingBoss:
            drawWind(bots)
            checkForBullets(bots)
            if len(bots) == 0:
                run = False
                newLevel = True
            else:
                allbots = map(lambda bot: bot.x <= 0 or bot.x >= w,bots)
                allLeft = reduce(lambda x,y: x and y,allbots)
                if allLeft:
                    run = False
        else:
            drawWin()
            if boss.damaged:
                run = False
                newLevel = True
        messageOnScreen(win,"lives: " + str(rocky.lives),(255,255,255),0,0,75)
        messageOnScreen(win,"score: " + str(rocky.score),(255,255,255),500,0,75)
        pygame.display.update()
    if newLevel:
        rocky.bullets = []
        rocky.level += 1
        showLevel()
    else:
        outro()

#here the mainloop function is defined i explain what it does below
def mainloop():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.blit(bg,(0,0))
        run = False
        pygame.display.update()
    intro()

#################################### MAINLOOP #################################

#here the mainloop is executed this loop runs the entire program
# and it also calls the intro loop that sends the player to the intro window
mainloop()        
pygame.quit()

