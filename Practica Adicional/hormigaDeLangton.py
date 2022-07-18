#Trabajo Practico 1 - Inteligencia Artificial I - UNCuyo
#Ejercicio 8 - Grupo 2

import turtle 
  
def cambiarColor(grafico, hormiga, color): 
    grafico[coordenadas(hormiga)] = color # mapa(10,0) = 'black'
  
def coordenadas(hormiga): 
    return (round(hormiga.xcor()), round(hormiga.ycor())) 
    # xcor e ycor son metodos de la libreria turtle que devuelven las coordenadas de la tortuga

def HormigaDeLangton():   
    
    ventana = turtle.Screen() #Guardamos la pantalla en la variable ventana
    ventana.screensize(1020,1020) #Tamaño de la pantalla
    ventana.bgcolor('white') #Color de fondo de la pantalla (Interface gráfica) 
    ventana.title('Hormiga de Langton - Grupo 2')
  
    hormiga = turtle.Turtle() #Guardamos el "lapiz" en la variable hormiga 
    hormiga.shape('square') #Le damos la forma al "Lapiz"    
    hormiga.shapesize(0.5) #Le damos tamaño al "Lapiz"  
    hormiga.speed(1000000) #Establecemos la velocidad con la que pinta cada cuadro                                
      
    posicion = coordenadas(hormiga) #Devuelve la coordenada de la variable hormiga                            

    mapa = {} 
    contador = 0

    while True: 
          
        if contador%100==0:
            print (contador)

        paso = 10 #distancia que se mueve  
        #Cuando encuentra blanco o sin pintar haciendo uso de la clave:valor (x,y):color                                    
        if posicion not in mapa or mapa[posicion] == "white": 
              
            hormiga.fillcolor("black") #Elige el color negro    
            hormiga.stamp() #Pinta la pantalla con la forma de la tortuga/lapiz                                 
            cambiarColor(mapa, hormiga, "black") 
            hormiga.right(90) #dobla hacia la derecha 90°
            hormiga.forward(paso) #mueve hacia adelante la distancia "paso"                         
            posicion = coordenadas(hormiga) #devuelve las coordenadas de la posicion actual
            contador=contador+1
              
        else:
            hormiga.fillcolor("white") 
            hormiga.stamp() 
            cambiarColor(mapa, hormiga, "white")       
            hormiga.left(90) 
            hormiga.forward(paso) 
            posicion = coordenadas(hormiga) 
            contador=contador+1
            
    

HormigaDeLangton()
