import pygame
from pygame.draw import *

def mouse_pressed(contador, path1, tamaño_cuadro):

    mouseX = int((pygame.mouse.get_pos()[0])/(tamaño_cuadro+1))
    mouseY = int((pygame.mouse.get_pos()[1])/(tamaño_cuadro+1))
    
    if contador ==0 and path1.storage.mat[int(mouseY), int(mouseX)].is_rack != False:
        path1.storage.mat[mouseY, mouseX].is_starting_point = True
        path1.storage.mat[mouseY,mouseX].set_color()
        contador = 1
    elif contador == 1 and path1.storage.mat[int(mouseY), int(mouseX)].is_rack != False: 
        path1.storage.mat[mouseY,mouseX].is_target = True
        path1.storage.mat[mouseY,mouseX].set_color()
        contador = 0
    return (contador,(int(mouseY), int(mouseX)))



def main_loop(path1):

    pygame.init()

    size = (720,720)

    if path1.storage.racks_order == 0:
        tamaño_cuadro = int((720-(path1.storage.rows))/(path1.storage.rows+1)) 
    else:
        tamaño_cuadro = int((720-(path1.storage.columns))/(path1.storage.columns+1))
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Grupo 6 - A* (Ejercicio 1)")
    clock = pygame.time.Clock()
    contador = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                contador,p=mouse_pressed(contador,path1,tamaño_cuadro)
                if contador==1:
                    path1.starting_point=p
                elif contador==0:
                    path1.target=p
                    sequence=path1.a_star()
                    #print(sequence)
                    
                    
        screen.fill((148, 148, 148))
        (x,y) = (0,1)

<<<<<<< HEAD
        for i in range(path1.storage.rows-1):
            for j in range(path1.storage.columns-1):
=======
        for i in range(path1.storage.rows):
            for j in range(path1.storage.columns):
>>>>>>> 72e7d2c3f89ba68ab926cbc5e3519f188ae0d3da
                if path1.storage.mat[i,j].is_rack == True:
                    rect(screen, path1.storage.mat[i,j].color, [x, y,tamaño_cuadro, tamaño_cuadro])
                elif path1.storage.mat[i,j].is_rack == False:
                    rect(screen, path1.storage.mat[i,j].color, [x, y, tamaño_cuadro, tamaño_cuadro])
                if path1.storage.mat[i,j].is_target == True:
                    rect(screen, path1.storage.mat[i,j].color, [x, y, tamaño_cuadro, tamaño_cuadro])
                if path1.storage.mat[i,j].is_starting_point == True:
                    rect(screen, path1.storage.mat[i,j].color, [x, y, tamaño_cuadro, tamaño_cuadro])
                x = x+tamaño_cuadro+1
            y = y+tamaño_cuadro+1
            x = 0    
        pygame.display.flip()
        #clock.tick(1)