from pygame import *
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
        #if keys[K_LEFT] and self.rect.x > 5:
            #self.rect.x -= self.speed
        #if keys[K_RIGHT] and self.rect.x < 620:
            #self.rect.x += self.speed
    


'''class Enemy(GameSprite):
    def __init__(self, player_image, speed, x, y, width, height):
        super().__init__(player_image, speed, x, y, width, height)
    def update(self):
        self.rect.y += self.speed
        global lost 
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(30, 420)
            lost = lost + 1'''



rak = Player1('rak.png', 5, 300, 400, 60, 65)
rak1 = Player1('rak.png', 5, 300, 30, 60, 65)
ball = Player1('ball.png', 5, 150, 150, 30, 30)




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


    display.update()    
    clock.tick(FPS)
