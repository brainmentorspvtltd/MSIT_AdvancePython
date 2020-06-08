import pygame
import random
import math
pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))

# rgb
white = 255, 255, 255
black = 0, 0, 0
blue = 50, 50, 255
green = 50, 255, 57
red = 242, 29, 29


class Ball:

    def __init__(self):
        self.radius = random.randint(10, 50)
        self.x = random.randint(0, width - self.radius)
        self.y = random.randint(0, height - self.radius)
        self.moveX = random.randint(5, 10)
        self.moveY = random.randint(5, 10)
        self.color = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)

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

    def checkCollision(self):
        for ball in ballsList:
            if ball is self:
                continue
            distanceBtwBalls = math.sqrt(
                ((ball.x - self.x) ** 2) + ((ball.y - self.y) ** 2))
            if distanceBtwBalls <= self.radius + ball.radius:
                self.moveX, ball.moveX = ball.moveX, self.moveX
                self.moveY, ball.moveY = ball.moveY, self.moveY

    # destructor
    def __del__(self):
        print("Ball deleted")


ballsList = []

for i in range(10):
    ball = Ball()
    ballsList.append(ball)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)

    for ball in ballsList:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
        ball.update()
        ball.checkCollision()

    pygame.display.update()
