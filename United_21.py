from pygame import *
init()
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, img, w, h, speed=0):
        super().__init__()
        self.w = w
        self.h = h
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def remove(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_e]:
            ball.rect.x = 100
            ball.rect.y = 100
 
 
class Ball(GameSprite):
    def __init__(self, x, y, img, w, h, speed_x, speed_y):
        self.w = w
        self.h = h
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.directH = 'r'
        self.directV = 'up'     
    def move(self):
        if self.rect.y >= 440:
            self.directV = 'up'
        if self.rect.y <= 10:
            self.directV = 'down'
        if self.directV == 'up':  
            self.rect.y -= self.speed_y
        if self.directV == 'down':
            self.rect.y += self.speed_y
        self.rect.x += self.speed_x
 
class Played(GameSprite):
    def moving(self):
        if keys[K_w]:
            if self.rect.y >= 10:
                self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y <= 400:
                self.rect.y += self.speed
    def moving_2(self):
        if keys[K_UP]:
            if self.rect.y >= 10:
                self.rect.y -= self.speed
        if keys[K_DOWN]:
            if self.rect.y <= 400:
                self.rect.y += self.speed
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
clock = time.Clock()
 
ball = Ball(100, 100, 'ball_png.png', 70, 70, 2, 2)
platform = Played(-35, 100, 'platform.png', 75, 100, 5)
platform1 = Played(660, 100, 'platform1.png', 75, 100, 5)
continue_game = GameSprite(280, 300, 'pr.png', 171, 60)

x_exit = 280
y_exit = 100

exit_game = GameSprite(x_exit, y_exit, 'exit.png', 171, 54)
restart = GameSprite(280, 200, 'restart.png', 171, 54)
bg = transform.scale(image.load('pole.png'), (700, 500))
menu = transform.scale(image.load('menu.png'), (700, 500))

font = font.SysFont('Arial', 30)




game = True
score = 0
check = 0
start = 1
x_click = 0
y_click = 0
while game:
    #события
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        start = 0

    if sprite.collide_rect(platform, ball):
        ball.speed_x *= -1
        score += 1
    if sprite.collide_rect(platform1, ball):
        ball.speed_x *= -1
        score += 1
    if score == check:
        check += 3
        ball.speed_x += 2
        ball.speed_y += 2
        platform.speed += 2
        platform1.speed += 2

    for ev in event.get():
        if ev.type == QUIT:
            game = False
        if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
            x_click, y_click = ev.pos



    #Отрисовка
    if start == 0:
        window.blit(menu, (0, 0))
        continue_game.render()
        exit_game.render()
        restart.render()
        if continue_game.rect.collidepoint(x_click, y_click):
            start = 1
        if exit_game.rect.collidepoint(x_click, y_click):
            game = False 
        if restart.rect.collidepoint(x_click, y_click):
            start = 1
            score = 0
            check = 0
            ball.rect.x = 100
            ball.rect.y = 100
            ball.speed_x = 2
            ball.speed_y = 2
    if start == 1:
        window.blit(bg, (0, 0))
        ball.render()
        platform.render()
        platform1.render()
        ball.move()
        platform.moving()
        platform1.moving_2()
        am = font.render('Общии счет:' + str(score), True, (0, 0, 0))
        window.blit(am, (20, 20))
    #Вызов методов
    display.update()
    clock.tick(60)