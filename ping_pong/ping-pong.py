
from pygame import *
import random
font.init()

window_height = 700
window_width = 500
fps = 60
clock = time.Clock()
window = display.set_mode((window_height, window_width))
display.set_caption('Пинг-понг')
background = (200,255,255)
speed_x = 3
speed_y = 3  
font1 = font.SysFont('Arial', 35)
font2 = font.SysFont('Arial', 35)
lose_rocketka_1 = font1.render('Player 1 lose' , 100 ,(180,0,0))
lose_rocketka_2 = font2.render('Player 2 lose' , 100 ,(180,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,player_weight,player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_weight,player_height))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):

    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y:
            self.rect.x += self.speed 
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 375:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 375:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        global speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y > window_width-50 or self.rect.y < 0:
            speed_y *= -1
        
            
        

rocketka_1 = Player ('roketka.jpg', 0, 200,10,30,130)
rocketka_2 = Player ('roketka.jpg', 670, 200,10,30,130)
ball = Enemy ('ball3.png', 335, 187,5,50,50)

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        
        window.fill(background)
        rocketka_1.reset()
        rocketka_1.update_1()
        rocketka_2.reset()
        rocketka_2.update_2()
        ball.reset()
        ball.update()
        if sprite.collide_rect(rocketka_1, ball) or sprite.collide_rect(rocketka_2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_rocketka_1,(250,190))
        if ball.rect.x > 650:
            finish = True
            window.blit(lose_rocketka_2,(250,190))
    display.update()
    clock.tick(fps)