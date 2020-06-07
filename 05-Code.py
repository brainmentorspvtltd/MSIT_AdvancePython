import pygame
import random
import math
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


class Ball:

    def __init__(self):
        self.radius = 50
        self.x = random.randint(0, width - self.radius)
        self.y = random.randint(0, height - self.radius)
        self.moveX = random.randint(5, 10)
        self.moveY = random.randint(5, 10)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > (width - self.radius):
            self.moveX = -random.randint(5, 10)
        elif self.x < self.radius:
            self.moveX = random.randint(5, 10)
        elif self.y > height - self.radius:
            self.moveY = -random.randint(5, 10)
        elif self.y < self.radius:
            self.moveY = random.randint(5, 10)

        # x = 1 + 2 - 3 * (4 / 5) ** 6
        # print(x)


ball1 = Ball()
ball2 = Ball()
# ball3 = Ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    ball1Circle = pygame.draw.circle(
        screen, black, (ball1.x, ball1.y), ball1.radius)
    ball1.update()
    ball2Circle = pygame.draw.circle(
        screen, black, (ball2.x, ball2.y), ball2.radius)
    ball2.update()
    # pygame.draw.circle(screen, black, (ball3.x, ball3.y), ball3.radius)
    # ball3.update()

    # if ball1Circle.colliderect(ball2Circle):
    distanceBtwBalls = math.sqrt(
        ((ball2.x - ball1.x) ** 2) + ((ball2.y - ball1.y) ** 2))
    if distanceBtwBalls <= ball1.radius + ball2.radius:
        ball1.moveX, ball2.moveX = ball2.moveX, ball1.moveX
        ball1.moveY, ball2.moveY = ball2.moveY, ball1.moveY
        # ball1.moveX = ball2.moveX
        # ball1.moveY = ball2.moveY
        # ball2.moveX = ball1.moveX
        # ball2.moveY = ball1.moveY

        # a = 10
        # b = 20
        # a,b = b,a   #swapping
        # temp = a
        # a = b
        # b = temp

    pygame.display.update()
