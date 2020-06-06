# pip install pygame
import pygame
import random
pygame.init()

width = 900
height = 500

screen = pygame.display.set_mode((width, height))

# rgb
white = 255, 255, 255
black = 0, 0, 0
blue = 50, 50, 255
green = 50, 255, 57
red = 242, 29, 29

screen.fill(green)
x = 100
y = 100
x2 = 100
y2 = 100
moveX = 5
moveY = 5
moveXBall2 = 5
moveYBall2 = 5
color = random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255)
colorBall2 = random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255)
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    # surface, color, (x,y), radius
    for i in range(1):
        random_x = random.randint(0, 850)
        random_y = random.randint(0, 450)
        print(random_x, random_y)
        pygame.draw.circle(screen, color, (random_x, random_y), 50)
        # for i in range(20):
        #     #     print(x, y)
        #     pygame.draw.circle(screen, color, (x, y), 50)
        # pygame.draw.circle(screen, colorBall2, (x2, y2), 50)
    x += moveX
    y += moveY

    x2 += moveXBall2
    y2 += moveYBall2

    if y > 450:
        moveY = random.randint(-10, -5)
    if y < 50:
        moveY = random.randint(5, 10)
    if x > 850:
        moveX = random.randint(-10, -5)
    if x < 50:
        moveX = random.randint(5, 10)

    if y2 > 450:
        moveYBall2 = random.randint(-10, -5)
    if y2 < 50:
        moveYBall2 = random.randint(5, 10)
    if x2 > 850:
        moveXBall2 = random.randint(-10, -5)
    if x2 < 50:
        moveXBall2 = random.randint(5, 10)

    pygame.display.update()
