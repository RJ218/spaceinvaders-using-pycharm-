import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
# title and icon
pygame.display.set_caption("Space_Invaders")
icon = pygame.image.load('C:\\Users\\RJ\\PycharmProjects\\spaceinvader\\ufo1.png')
pygame.display.set_icon(icon)

playerIMG = pygame.image.load('C:\\Users\RJ\\PycharmProjects\\spaceinvader\\spaceship1.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load('C:\\Users\\RJ\\PycharmProjects\\spaceinvader\\monster.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(.3)
    enemyY_change.append(30)

bulletIMG = pygame.image.load("C:\\Users\\RJ\\PycharmProjects\\spaceinvader\\bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bulletstate = "ready"  # ready means you can't see the bullet

backIMG = pygame.image.load('C:\\Users\\RJ\\PycharmProjects\\spaceinvader\\155.jpg')


def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))


def bulletfire(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletIMG, (x + 16, y + 10))


def show_score(x, y):
    scre = font.render("score :" + str(score), True, (255, 255, 255))
    screen.blit(scre , (x,y))

def collision(bx, by, ex, ey):
    distance = math.sqrt((math.pow(bx - ex, 2)) + (math.pow(by - ey, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    # screen.blit(backIMG, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.7
            if event.key == pygame.K_RIGHT:
                playerX_change = .7
            if event.key == pygame.K_SPACE:
                if bulletstate is "ready":
                    bulletfire(playerX, playerY)
                    xcord = playerX
        # if event.key == pygame.K_UP:
        #    playerY_change=-.3
        # if event.key == pygame.K_DOWN:
        #   playerY_change=.3
        if event.type == pygame.KEYUP:
            playerX_change = 0
            # playerY_change=0

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        # enemyY += enemyY_change
        if enemyX[i] <= 0:
            enemyX_change[i] = .3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -.3
            enemyY[i] += enemyY_change[i]
        col = collision(bulletX, bulletY, enemyX[i], enemyY[i])
        if col:
            bulletY = 480
            bulletstate = "ready"
            score += 1
            #print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736
    # playerY += playerY_change

    if bulletY < 0:
        bulletY = 480
        bulletstate = "ready"

    if bulletstate is "fire":
        bulletfire(xcord, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
