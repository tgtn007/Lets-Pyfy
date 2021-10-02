import pygame
import random
import math

player1=input("Enter your name : ")
pygame.init()       #initialize the pygame
screen=pygame.display.set_mode((800,600))       #create the screen

pygame.display.set_caption("Star Wars")     #For changing the caption of the game
icons=pygame.image.load("Ufo_py.png")       #For loading the image and change the icon
pygame.display.set_icon(icons)
enemy_list=[]
font=pygame.font.Font("freesansbold.ttf",32)
background=pygame.image.load("889.jpg")

player=pygame.image.load("shooter.png")           #loading the player image
playerx=370     #X - player's X coordinate
playery=480      #Y - player's Y Coordinate
playerx_change=0    

enemy_list.append(pygame.image.load("sp_1.png"))
enemy_list.append(pygame.image.load("sp_2.png"))
enemy_list.append(pygame.image.load("sp_3.png"))
enemy_list.append(pygame.image.load("sp_5.png"))
enemy=random.choice(enemy_list)
enemyX=random.randint(0,800)
enemyY=random.randint(50,350)
enemyX_change=3
enemyY_change=8

bullet=pygame.image.load("bullet.png")
bulletX=385
bulletY=487
bulletY_change=-6
bullet_state="yes"

 
value=0
def players(x,y):
    screen.blit(player,(x,y))       #for drawing the player at(x,y) coordinate

def enemy_e(x,y):
    screen.blit(enemy,(x,y))

def bullet_fire(x,y):
    global bullet_state
    bullet_state="no"
    screen.blit(bullet,(x,y))

def iscollision(a,b,c,d,x):
    distance=math.sqrt(math.pow(a-b,2)+math.pow(c-d,2))
    if distance<=x:
        return True
    else:
        return False

def score_value(c):
    value_1=font.render(f"{c}'s Score : {str(value)}",True,(255,0,0))
    screen.blit(value_1,(10,10))
Running=True

#Game loop
while Running:
    screen.fill((0,0,128))     #For changing the screen color
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                playerx_change=-4
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                playerx_change =4
            if event.key==pygame.K_SPACE:
                if bullet_state is "yes":
                    bulletX=playerx
                    bullet_fire(bulletX+15,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a or event.key== pygame.K_LEFT or event.key==pygame.K_d or event.key== pygame.K_RIGHT:
                playerx_change=0
    playerx+=playerx_change
    if playerx<=-1:
        playerx=-1
    elif playerx>=740:
        playerx=740

    enemyX+=enemyX_change
    if enemyX<=-1:
        enemyX_change=3
        enemyY+=enemyY_change
    elif enemyX>=740:
        enemyX_change=-3
        enemyY+=enemyY_change

    if bulletY<=0:
        bullet_state="yes"
        bulletY=playery+7
    if bullet_state is "no":
        bullet_fire(bulletX+15,bulletY)
        bulletY+=bulletY_change
    players(playerx,playery)
    collision=iscollision(enemyX,bulletX,enemyY,bulletY,30)
    if collision:
        value+=1
        bullet_state="yes"
        bulletY=playery+7
        enemyX=random.randint(0,800)
        enemyY=random.randint(50,350)
        enemy=random.choice(enemy_list)
    collision_game_over=iscollision (enemyX,playerx,enemyY,playery,55)
    if collision_game_over:
        Running=False
    enemy_e(enemyX,enemyY)
    score_value(player1)
    pygame.display.update()     #After Updating the screen work we have to run this command