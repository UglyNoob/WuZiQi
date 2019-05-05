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
start_exit=font.render("退出",True,(0,0,0)).convert_alpha()
start_exit_rect=start_exit.get_rect()
start_exit_rect.x=240
start_exit_rect.y=600

play_map=[]
i,j=0,0
while i<=30:
    line=[]
    while j<=30:
        line.append(' ')
        j+=1
    play_map.append(line)
    i+=1;j=0
del i,j,line
player='b'

black=font.render("黑方",True,(0,0,0)).convert_alpha()
white=font.render("白方",True,(0,0,0)).convert_alpha()
over_won=font.render("胜利",True,(0,0,0)).convert_alpha()
over_pos=black.get_rect().width

def check_color(what):
    if what=='b':return (0,0,0)
    elif what=='w':return (255,255,255)

def check_eat(x,y):
    global play_map,winner,winners,now
    #横向找
    i=0;time=1;who=None
    while i<=30:
        if play_map[i][y]==who and who!=' ':
            time+=1
            if time==5:
                winner=who
                winners.append((i*20,y*20))
                now=2
                return
        else:
            time=1;who=play_map[i][y];winners=[(i*20,y*20)]
        i+=1
    #纵向找
    j=0;time=1;who=None
    while j<=30:
        if play_map[x][j]==who and who!=' ':
            time+=1
            if time==5:
                winner=who
                winners.append((x*20,j*20))
                now=2
                return
        else:
            time=1;who=play_map[x][j];winners=[(x*20,j*20)]
        j+=1

def start():
    global screen,pos,now,start_caption,start_start,start_start_rect,start_exit,start_exit_rect
    screen.blit(start_caption,(210,150))
    if start_start_rect.collidepoint(pos):
        screen.fill((200,200,200),start_start_rect)
    elif start_exit_rect.collidepoint(pos):
        screen.fill((200,200,200),start_exit_rect)
    screen.blit(start_start,start_start_rect)
    screen.blit(start_exit,start_exit_rect)

def play():
    global screen,play_map,player
    x,y=0,0
    while x<=30:
        pygame.draw.line(screen,(0,0,0),(x*20,0),(x*20,600))
        pygame.draw.line(screen,(0,0,0),(0,x*20),(600,x*20))
        x+=1
    if pos[0]<=600 and pos[1]<=600:
        pygame.draw.circle(screen,check_color(player),(round(pos[0]/20)*20,round(pos[1]/20)*20),10)
    x=0
    while x<=30:
        while y<=30:
            color=check_color(play_map[x][y])
            if color:
                pygame.draw.circle(screen,color,(x*20,y*20),10)
            y+=1
        x+=1;y=0

def over():
    global screen,black,white,winner,winners,over_won,over_pos
    x,y=0,0
    while x<=30:
        pygame.draw.line(screen,(0,0,0),(x*20,0),(x*20,600))
        pygame.draw.line(screen,(0,0,0),(0,x*20),(600,x*20))
        x+=1
    x=0
    while x<=30:
        while y<=30:
            color=check_color(play_map[x][y])
            if color:
                pygame.draw.circle(screen,color,(x*20,y*20),10)
            y+=1
        x+=1;y=0
    pygame.draw.line(screen,(255,0,0),winners[0],winners[1])

    if winner=='b':
        screen.blit(black,(0,600))
    else:
        screen.blit(white,(0,600))
    screen.blit(over_won,(over_pos,600))

now=0
up=(start,play,over)
clock=pygame.time.Clock()
while True:
    clock.tick(20)
    screen.fill((236,236,236))
    pos=pygame.mouse.get_pos()
    up[now]()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if now==1 and pos[0]<=600 and pos[1]<=600:
                x=round(pos[0]/20);y=round(pos[1]/20)
                if not check_color(play_map[x][y]):
                    play_map[x][y]=player
                    check_eat(x,y)
                    if player=='w':player='b'
                    else:player='w'
            elif now==0:
                if start_start_rect.collidepoint(event.pos):
                    now=1
                elif start_exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        elif event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
