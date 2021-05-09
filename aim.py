import pygame, random
pygame.init()
win=pygame.display.set_mode((1440,900))
pygame.display.set_caption("Aim Trainer")
black=(0,0,0)
rand1=random.randint(50,450)
rand2=random.randint(50,450)

width=20
height=20
score=0

def enemy():
    e=pygame.draw.ellipse(win, (255,0,0),(rand1,rand2,width,height)) #target
    return e
def player():
    play=pygame.draw.ellipse(win, (255,255,255),(x,y,width/3,height/3)) #crosshair
    return play

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) #making the mouse invisible

run=True

while run:
    x, y = pygame.mouse.get_pos()
    pygame.time.delay(10)
    if player().colliderect(enemy()):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                rand1=random.randint(50,450)
                rand2 = random.randint(50, 450)
                score += 1
                print("Your Score Is:",str(score)) #displaying the score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    win.fill((black))
    player()
    enemy()
    pygame.display.update()
