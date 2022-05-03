import pygame
from pygame.draw import *

def mouse_pressed(contador, path1, tamaño_cuadro):

    mouseX = int((pygame.mouse.get_pos()[0])/(tamaño_cuadro+1))
    mouseY = int((pygame.mouse.get_pos()[1])/(tamaño_cuadro+1))
    
    if contador ==0:
        if path1.storage.mat[mouseY, mouseX].is_rack == True:
        
            path1.storage.mat[mouseY, mouseX].is_starting_point = True
            path1.storage.mat[mouseY,mouseX].set_color()
        
        elif path1.storage.mat[mouseY, mouseX].is_rack == False:
        
            x = path1.storage.mat[mouseY, mouseX].a_x 
            y = path1.storage.mat[mouseY, mouseX].a_y
            path1.storage.mat[mouseY, mouseX].set_color((244, 16, 202))
            path1.storage.mat[mouseY, mouseX].is_starting_point = True
            mouseX = x
            mouseY = y
        contador = 1
    elif contador == 1:

        if path1.storage.mat[mouseY, mouseX].is_rack == True:

            path1.storage.mat[mouseY,mouseX].is_target = True
            path1.storage.mat[mouseY,mouseX].set_color()
            
        elif path1.storage.mat[mouseY, mouseX].is_rack == False:

            x = path1.storage.mat[mouseY, mouseX].a_x 
            y = path1.storage.mat[mouseY, mouseX].a_y
            path1.storage.mat[mouseY, mouseX].set_color((152, 244, 16))
            path1.storage.mat[mouseY, mouseX].is_target = True
            mouseX = x
            mouseY = y
            
            
        contador =0
              
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
    fuente = pygame.font.Font(None, 20)
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
                            if path1.storage.mat[i[0],i[1]].is_rack == True:
                                path1.storage.mat[i[0],i[1]].set_color((255,255,255))
                            else:
                                path1.storage.mat[i[0],i[1]].set_color((0, 0, 0))
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
                rect(screen, path1.storage.mat[i,j].color, [x, y,tamaño_cuadro, tamaño_cuadro])
                if path1.storage.mat[i,j].is_rack == False:
                    text = str(path1.storage.mat[i,j].product)
                    mensaje = fuente.render(text, 1, (255, 255, 255))
                    screen.blit(mensaje, (x, y))
                x = x+tamaño_cuadro+1
            y = y+tamaño_cuadro+1
            x = 0    
        pygame.display.flip()
        #clock.tick(1)
