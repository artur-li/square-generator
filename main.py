import pygame, sys, random
pygame.init()

screen = pygame.display.set_mode((600,600))
clock  = pygame.time.Clock()

class Rect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(self.random_color())
        self.rect = self.image.get_rect(center=(random.randint(10,590), random.randint(10,590)))
        self.direction_x = random.choice(["left", "right"])
        self.direction_y = random.choice(["up", "down"] )
    def random_color(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    def direction_to_move(self):
        if self.rect.centerx > 590:
            self.direction_x = 'left'
        elif self.rect.centerx < 10:
            self.direction_x = "right"
        elif self.rect.centery < 10:
            self.direction_y = "down"
        elif self.rect.centery > 590:
            self.direction_y = "up"
    def movement(self):
        if self.direction_x == "left":
            self.rect.centerx -= 3 
        elif self.direction_x == "right":
            self.rect.centerx += 3
        if self.direction_y == "down":
            self.rect.centery += 3
        elif self.direction_y == "up":
            self.rect.centery -= 3
    def update(self):
        self.direction_to_move()
        self.movement()
rect_group = pygame.sprite.Group()

def draw_rect():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            rect = Rect()
            rect_group.add(rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    draw_rect()
    rect_group.draw(screen)
    rect_group.update()
    pygame.display.update()
    clock.tick(60)
