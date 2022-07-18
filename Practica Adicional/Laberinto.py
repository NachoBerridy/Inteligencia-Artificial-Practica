
from turtle import *
from math import *
import time


"""def funcionDeCosto(a,b):
    return round(sqrt((15-a)**2+(15-b)**2)+(abs(3-a)+abs(3-b)),2)"""
    
def funcionDeCosto(a,b):
    return round(sqrt((15-a)**2+(15-b)**2))#+sqrt((3-a)**2+(3-b)**2),2)

ventana =Screen() #Guardamos la pantalla en la variable ventana
ventana.screensize(2000,2000) #Tamaño de la pantalla
ventana.bgcolor('white') #Color de fondo de la pantalla (Interface gráfica) 
ventana.title('Laberinto - Grupo 2')
cursor = Turtle()
cursor.color('black') 

paso = 2 
cursor.shape("square") 
cursor.shapesize(paso)
cursor.speed(1000)
cursor.penup()#El lapiz deja de rayar para moverte
cursor.backward(150*paso)
cursor.left(90)
cursor.forward(150*paso)
cursor.pendown()#El lapiz vuelve a rayar para moverte
cursor.right(90)

mapa_costo = {}
mapa_casillas = {}
mapa_raiz = {}
barrera = ((3,11),(4,10),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),(11,9),(12,9),(13,9),(14,9),(14,10),(14,11),(14,12))
p_inicial= (3,3)
p_final = (15,15)
funcionG={}

for fila in range(16):
    for columna in range(17):
        if (fila+1,columna+1) in barrera:
            cursor.fillcolor("red")
            cursor.stamp()
            mapa_casillas[(fila+1,columna+1)] = (cursor.xcor(),cursor.ycor())
            mapa_costo[(fila+1,columna+1)] = 10000
            mapa_raiz[(fila+1,columna+1)] = (0,0)
            funcionG[(fila+1,columna+1)] = 0
            cursor.forward(20*paso)
            cursor.penup()
        elif (fila+1,columna+1) == p_final:
            cursor.fillcolor("green")
            cursor.stamp()
            mapa_casillas[(fila+1,columna+1)] = (cursor.xcor(),cursor.ycor())
            mapa_costo[(fila+1,columna+1)] = funcionDeCosto(fila+1,columna+1)
            mapa_raiz[(fila+1,columna+1)] = (0,0)
            funcionG[(fila+1,columna+1)] = 0
            cursor.forward(20*paso)
            cursor.penup()   
        else:
            cursor.fillcolor("white")
            cursor.stamp()
            mapa_casillas[(fila+1,columna+1)] = (cursor.xcor(),cursor.ycor())
            mapa_costo[(fila+1,columna+1)] = funcionDeCosto(fila+1,columna+1)
            mapa_raiz[(fila+1,columna+1)] = (0,0)
            funcionG[(fila+1,columna+1)] = 0
            cursor.forward(20*paso)
            cursor.penup()
    cursor.backward(20*paso*17)
    cursor.right(90)
    cursor.forward(20*paso)
    cursor.left(90)

#Esto vuelve el cursor al punto inicial 
cursor.penup()
cursor.goto(mapa_casillas[p_inicial])
cursor.fillcolor("yellow") 
cursor.stamp()
cursor.pendown()

cursor.shape("turtle")
cursor.shapesize(1)
cursor.fillcolor("black")
cursor.stamp()

(x,y) = (3,3)
mapa_costo[x,y]=0
mapa_costo[3,3] = 1000
mapa_raiz[3,3] = (3,3)
camino = [p_final]
puntos = []
nodos_cerrados = [(3,3)]
nodos_abiertos = []
g = 0

while (x,y)!=p_final:

    nodo_raiz = (x,y)
    puntos.clear()

    if   x==1: 
        if 1<y & y<17 : 
            puntos = [(x+1,y),(x,y+1),(x,y-1)]
        elif y==1:
            puntos = [(x+1,y),(x,y+1)]
        elif y==17:
            puntos = [(x+1,y),(x,y-1)]            

    elif y==1:  
        if x<16 & x>1 :
            puntos = [(x+1,y),(x-1,y),(x,y+1)]
        elif x==16:
            puntos = [(x-1,y),(x,y+1)]

    elif x ==16:
        if 1<y & y<17:
            puntos = [(x-1,y),(x,y+1),(x,y-1)]
        elif y==17:
            puntos = [(x-1,y),(x,y-1)]

    elif y==17:  
        if 1<x & x<16 :
            puntos = [(x+1,y),(x-1,y),(x,y-1)]
    else: 
        puntos = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

    for i in puntos:
        funcionG[i]=funcionG[nodo_raiz]+1
        costo = mapa_costo[i]+funcionG[i]
        if mapa_raiz[i]==(0,0):
            nodos_abiertos.append(i)
        if costo<mapa_costo[i] or mapa_raiz[i]==(0,0):
            mapa_raiz[i]=nodo_raiz
            mapa_costo[i] = costo

    for i in nodos_abiertos:
        if (mapa_costo[x,y]>mapa_costo[i]  & mapa_costo[i]!=1000):
            (x,y) = i

    mapa_costo[x,y] = 1000
    nodos_cerrados.append((x,y))
    nodos_abiertos.remove((x,y))
    g = g + 1

while p_final!=p_inicial:
    camino.append(mapa_raiz[p_final])
    p_final = mapa_raiz[p_final]
camino_ordenado = reversed(camino)    
print ("El camino hallado es:")
for j in camino_ordenado:
    print (j)
    cursor.penup()
    cursor.goto(mapa_casillas[j[0],j[1]])
    cursor.stamp()
    cursor.pendown()
    #time.sleep(0.5)

print ("El costo de la busqueda fue de: ",len(camino))
cursor.showturtle()
input()
