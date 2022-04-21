from msilib import sequence
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
        size = ((tamaño_cuadro+1)*path1.storage.columns,(tamaño_cuadro+1)*path1.storage.rows)
    else:
        tamaño_cuadro = int((720-(path1.storage.columns))/(path1.storage.columns+1))
        size = ((tamaño_cuadro+1)*path1.storage.columns,(tamaño_cuadro+1)*path1.storage.rows)
    
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
                    try:
                        """Esto borra el camino anterior"""
                        for i in sequence:
                            if path1.storage.mat[i[0],i[1]].is_target == True:
                                path1.storage.mat[i[0],i[1]].is_target = False
                            if path1.storage.mat[i[0],i[1]].is_starting_point == True:
                                path1.storage.mat[i[0],i[1]].is_starting_point = False
                            path1.storage.mat[i[0],i[1]].set_color((255,255,255))
                    except:
                        pass
                    path1.starting_point=p
                elif contador==0:
                    path1.target=p
                    sequence=path1.a_star()
                    
                    
        screen.fill((148, 148, 148))
        (x,y) = (0,1)
        fuente = pygame.font.Font(None, 20)
        for i in range(path1.storage.rows):
            for j in range(path1.storage.columns):
                if path1.storage.mat[i,j].is_rack == True:
                    rect(screen, path1.storage.mat[i,j].color, [x, y,tamaño_cuadro, tamaño_cuadro])
                    
                elif path1.storage.mat[i,j].is_rack == False:
                    rect(screen, path1.storage.mat[i,j].color, [x, y, tamaño_cuadro, tamaño_cuadro])
                    #text = "1"
                    #mensaje = fuente.render(text, 1, (255, 255, 255))
                    #screen.blit(mensaje, (x, y))
                if path1.storage.mat[i,j].is_target == True:
                    rect(screen, path1.storage.mat[i,j].color, [x, y, tamaño_cuadro, tamaño_cuadro])
                if path1.storage.mat[i,j].is_starting_point == True:
                    rect(screen, path1.storage.mat[i,j].color, [x, y, tamaño_cuadro, tamaño_cuadro])
                if path1.storage.mat[i,j].is_cargo_bay == True:
                    rect(screen, path1.storage.mat[i,j].color, [x, y, tamaño_cuadro, tamaño_cuadro])
                x = x+tamaño_cuadro+1
            y = y+tamaño_cuadro+1
            x = 0    
        pygame.display.flip()
        #clock.tick(1)
