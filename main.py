# coding: utf-8
import pygame,sys
pygame.init()
pygame.display.set_caption("五子棋")
screen=pygame.display.set_mode((601,901))
font=pygame.font.Font("font.ttf",60)

start_caption=font.render("五子棋",True,(0,0,0)).convert_alpha()
start_start=font.render("开始",True,(0,0,0)).convert_alpha()
start_start_rect=start_start.get_rect()
start_start_rect.x=240
start_start_rect.y=500
print(start_start_rect.x)

play_map=[]
i,j=0,0
while i<=30:
    line=[]
    while j<=30:
        line.append(' ')
        j+=1
    i+=1
del i,j,line
player='b'

def start():
    global screen,start_caption,start_start,start_start,start_start_rect
    screen.blit(start_caption,(210,150))
    screen.blit(start_start,start_start_rect)

def play():
    pass

def over():
    pass

now=0
up=(start,play,over)
clock=pygame.time.Clock()
while True:
    clock.tick(20)
    screen.fill((236,236,236))
    up[now]()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
