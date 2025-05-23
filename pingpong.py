from pygame import *
from random import randint
mixer.init()
window = display.set_mode((700, 500))
display.set_caption("PING-PONG")
background = transform.scale(image.load('table.jpg'), (700, 500))
finish = False
clock = time.Clock()
FPS = 60
mixer.init()
font.init()
font = font.SysFont('Arial', 40)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
    

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 620:
            self.rect.x += self.speed

class Ball(GameSprite):
    vector = Vector2(0, 1)
    def update(self):
        vector = self.vector * self.speed
        self.rect.x += vector.x
        self.rect.y += vector.y
        

rak = Player1('rak.png', 8, 300, 400, 60, 65)
rak1 = Player2('rak.png', 8, 300, 30, 60, 65)
ball = Ball('ball.png', 5, 150, 150, 30, 30)




game = True
while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    


    rak.reset()
    rak.update()
    rak1.reset()
    rak1.update()
    ball.reset()
    ball.update()

    if rak.rect.colliderect(ball.rect):
        ball.vector = -ball.vector.rotate(randint(-30, 30))
        ball.rect.bottom = rak.rect.top
    if rak1.rect.colliderect(ball.rect):
        ball.vector = -ball.vector.rotate(randint(-30, 30))
        ball.rect.top = rak1.rect.bottom

    if ball.rect.left <= 0 or ball.rect.right >= 700:
        ball.vector.x = -ball.vector.x
    
    if ball.rect.top <= 0:
        print("Нижний победил")
        ball.rect.center = (350, 250)
    if ball.rect.top >= 500:
        print("Верхний победил")
        ball.rect.center = (350, 250)

    display.update()    
    clock.tick(FPS)
