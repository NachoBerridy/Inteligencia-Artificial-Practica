from importlib.resources import path
from unittest.mock import patch
import pygame
from pygame.draw import *
from path import*




cuadro = Layout(6,5,1,6,6)
cuadro.fill_mat()
path1=Path(cuadro)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()
size = (720,720)
if cuadro.racks_order == 0:
    tamaño_cuadro = int((720-cuadro.rows)/cuadro.rows) 
else:
    tamaño_cuadro = int((720-cuadro.columns)/cuadro.columns)
filas=1
columnas=6
#size = (tamaño_cuadro*cuadro.columns+100, tamaño_cuadro*cuadro.rows)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("A* ")
clock = pygame.time.Clock()
contador = 0

def mouse_pressed(contador):
    mouseX = int(pygame.mouse.get_pos()[0])
    mouseY = int(pygame.mouse.get_pos()[1])
    if contador ==0 and cuadro.mat[int(mouseY/(tamaño_cuadro+1)), int(mouseX/(tamaño_cuadro+1))].is_rack != False:
        cuadro.mat[int(mouseY/(tamaño_cuadro+1)), int(mouseX/(tamaño_cuadro+1))].is_starting_point = True
        contador = 1
    elif contador == 1 and cuadro.mat[int(mouseY/(tamaño_cuadro+1)), int(mouseX/(tamaño_cuadro+1))].is_rack != False: 
        cuadro.mat[int(mouseY/(tamaño_cuadro+1)), int(mouseX/(tamaño_cuadro+1))].is_target = True
        contador = 0
    return (contador,(int(mouseX/(tamaño_cuadro+1)), int(mouseY/(tamaño_cuadro+1))))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            contador=mouse_pressed(contador)[0]
            print (contador)
            if contador==1:
                path1.starting_point=mouse_pressed(contador)[1]
            elif contador==0:
                path1.target=mouse_pressed(contador)[1]
                sequence=path1.a_star()
                print(sequence)
                
                
    screen.fill(GREY)
    (x,y) = (0,1)
    for i in range(cuadro.rows):
        for j in range(cuadro.columns):
            if cuadro.mat[i,j].is_rack == True:
                rect(screen, WHITE, [x, y,tamaño_cuadro, tamaño_cuadro])
            elif cuadro.mat[i,j].is_rack == False:
                rect(screen, BLACK, [x, y, tamaño_cuadro, tamaño_cuadro])
            if cuadro.mat[i,j].is_target == True:
                rect(screen, RED, [x, y, tamaño_cuadro, tamaño_cuadro])
            if cuadro.mat[i,j].is_starting_point == True:
                rect(screen, BLUE, [x, y, tamaño_cuadro, tamaño_cuadro])
            x = x+tamaño_cuadro+1
        y = y+tamaño_cuadro+1
        x = 0    
    pygame.display.flip()
    clock.tick(1)