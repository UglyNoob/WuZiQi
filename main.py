# coding: utf-8
import pygame,sys
pygame.init()
screen=pygame.display.set_mode((601,901))

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

