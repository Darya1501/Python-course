import pygame
import random
import time


class Ball:
    def __init__(self, display):
        self.display = display
        self.color = pygame.Color('red')
        self.center_x = 100
        self.center_y = 100
        self.radius = 30
        
        self.vx = 2
        self.vy = 2
        
        

    def show(self):
        pygame.draw.circle(self.display, self.color, (self.center_x, self.center_y), self.radius)
        
    def clear(self):
        pygame.draw.circle(self.display, pygame.Color('white'), (self.center_x, self.center_y), self.radius)    
        
    def go(self):
        self.center_x += self.vx
        self.center_y += self.vy
        
    def move(self):
        self.clear()
        self.go()
        self.show() 
        
    def stop(self):
        self.vx = 0
        self.vy = 0     
        
    def is_in_field(ball):
        width, height = display.get_size() 
        if (width - ball.radius) > ball.center_x > ball.radius and (height - ball.radius) > ball.center_y > ball.radius:
            return True 
        return False    
    
    def is_ball_catch(ball, x, y):
            if ball.center_x - ball.radius <= x <= ball.center_x + ball.radius and ball.center_y - ball.radius <= y <= ball.center_y + ball.radius:
                return True    
            return False


class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)

        self.color = pygame.Color((152, 251, 152))
        width, height = display.get_size()
        self.center_x = random.randint(self.radius, width - self.radius)
        self.center_y = random.randint(self.radius, height - self.radius)


class PointBall(Ball):
    def __init__(self, display, x, y):
        super().__init__(display)

        self.color = pygame.Color('yellow')
        self.center_x = x
        self.center_y = y


class RandomPointMovableBall(RandomPointBall):
    def __init__(self, display):
        super().__init__(display)
        
        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)
        
        while self.vx == 0 and self.vy == 0:
            self.vx = random.randint(-3, 3)
            self.vy = random.randint(-3, 3)            
        
def show_text(text):
    font = pygame.font.SysFont('arial', 25)
    text = font.render(text, True,
                      (0, 0, 139), (173, 216, 230))
    display.blit(text, (50, 50))
            

pygame.init()

width = 1400
height = 700
display = pygame.display.set_mode((width, height))

display.fill(pygame.Color('white'))

balls = []
for i in range(10):
    ball = RandomPointMovableBall(display)
    ball.show()
    balls.append(ball)

pygame.display.flip()


clock = pygame.time.Clock()

counter = 0
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:   
            pos = event.pos
            for ball in balls:
                if ball.is_ball_catch(pos[0], pos[1]):
                    ball.stop()
                    if ball.is_in_field():
                        counter += 1  

        for ball in balls:
            ball.move()
        
        text = f'Вы поймали {counter} шт.'
        show_text(text)
    
    pygame.display.flip()
    clock.tick(60)
