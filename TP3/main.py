from MLP import MLP
import matplotlib.pyplot as plt
import numpy as np
modificar = 2
#funcion = 1 #reLU
#funcion = 2 #sigmoide
if modificar == 0: #no modifica el programa
    mlp = MLP(neuronas_ocultas = 100)
    funcion = 1 #reLU
    pesos = mlp.iniciar(numero_clases=3,
                        numero_ejemplos=300, 
                        graficar_datos=False,
                        learning_rate=1,
                        graficar = False,
                        f=funcion)

elif modificar == 1: #nuevo generador de datos
    mlp = MLP(neuronas_ocultas = 100)
    funcion = 1 #reLU
    pesos = mlp.iniciar2(numero_clases=3, 
                        numero_ejemplos=300, 
                        graficar_datos=False,
                        learning_rate=1,
                        graficar = False,
                        f=funcion)

elif modificar == 2: #barrido cantidad de neuronas capa oculta
    #neuronas=np.linspace(50,200,31)
    neuronas=np.linspace(50,200,4)
    funcion = 1 #reLU
    precision = []
    for i in neuronas:
        #print(i)
        mlp = MLP(neuronas_ocultas = int(i))
        precision.append(mlp.iniciar(numero_clases=3, 
                            numero_ejemplos=300, 
                            graficar_datos=False,
                            learning_rate=1,
                            graficar = False,
                            f=funcion))
    plt.plot(neuronas, precision)
    plt.xlabel('Cantidad de neuronas en la capa oculta')
    plt.ylabel('Precision')
    plt.show()
        

elif modificar == 3: #barrido del learning_rate
    mlp = MLP(neuronas_ocultas = 100)
    funcion = 1 #reLU
    learning = np.linspace(0.5,2,31)
    precision = []
    for i in learning:
        precision.append(mlp.iniciar(numero_clases=3,
                            numero_ejemplos=300, 
                            graficar_datos=False,
                            learning_rate=i,
                            graficar = False,
                            f=funcion))
    
    plt.plot(learning,precision)
    plt.xlabel('learning_rate')
    plt.ylabel('precision')
    plt.show()

elif modificar == 4: #funcion sigmoide
    funcion = 2 #sigmoide
    mlp = MLP(neuronas_ocultas = 100)
    pesos = mlp.iniciar(numero_clases=3, 
                        numero_ejemplos=300, 
                        graficar_datos=False,
                        learning_rate=1,
                        graficar = True,
                        f=funcion)
    
