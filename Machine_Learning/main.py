from MLP import MLP
import matplotlib.pyplot as plt
import numpy as np
modificar = 5
#funcion = 1 #reLU
#funcion = 2 #sigmoide
if modificar == 0: #no modifica el programa
    mlp = MLP(neuronas_ocultas = 100)
    funcion = 1 #reLU
    pesos = mlp.iniciar(numero_clases=3,
                        numero_ejemplos=300, 
                        graficar_datos=True,
                        learning_rate=1,
                        graficar = True,
                        f=funcion)

elif modificar == 1: #nuevo generador de datos
    mlp = MLP(neuronas_ocultas = 100)
    funcion = 1 #reLU
    pesos = mlp.iniciar2(numero_clases=3, 
                        numero_ejemplos=300, 
                        graficar_datos=True,
                        learning_rate=1,
                        graficar = True,
                        f=funcion)

elif modificar == 2: #barrido cantidad de neuronas capa oculta
    #neuronas=np.linspace(50,200,31)
    neuronas=np.linspace(50,200,4)
    funcion = 1 #reLU
    precision = []
    mlp = MLP(neuronas_ocultas = 100)
    numero_ejemplos = 300
    numero_clases = 3

    x1, t1 = mlp.generar_datos_clasificacion(numero_ejemplos, numero_clases)
    x_validacion1, t_validacion1 = mlp.generar_datos_clasificacion(cantidad_ejemplos=300, cantidad_clases=3)
    for i in neuronas:
        #print(i)
        mlp = MLP(neuronas_ocultas = int(i))
        
        precision.append(mlp.iniciar3(numero_clases=3, 
                            numero_ejemplos=300, 
                            graficar_datos=False,
                            learning_rate=1,
                            graficar = False,
                            f=funcion,
                            x=x1,
                            t=t1,
                            x_validacion=x_validacion1,
                            t_validacion=t_validacion1))

    plt.plot(neuronas, precision)
    plt.xlabel('Cantidad de neuronas en la capa oculta')
    plt.ylabel('Precision')
    plt.show()
        
elif modificar == 3: #barrido del learning_rate
    mlp = MLP(neuronas_ocultas = 100)
    funcion = 1 #reLU
    #learning = np.linspace(0.5,2,31)
    learning = np.linspace(0.5,2,4)
    precision = []
    numero_ejemplos = 300
    numero_clases = 3
    x1, t1 = mlp.generar_datos_clasificacion(numero_ejemplos, numero_clases)
    x_validacion1, t_validacion1 = mlp.generar_datos_clasificacion(cantidad_ejemplos=300, cantidad_clases=3)
    for i in learning:
        precision.append(mlp.iniciar3(numero_clases=3, 
                            numero_ejemplos=300, 
                            graficar_datos=False,
                            learning_rate=i,
                            graficar = False,
                            f=funcion,
                            x=x1,
                            t=t1,
                            x_validacion=x_validacion1,
                            t_validacion=t_validacion1))
    
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
    

elif modificar == 5: #barrido del learning_rate y neuronas de la capa oculta
    
    funcion = 1 #reLU
    learning = np.linspace(0.1,1,5)
    neuronas=np.linspace(100,200,5)
    precision = []
    for i in learning:
        print(i)
        p = []
        for j in neuronas:
            mlp = MLP(neuronas_ocultas = int(i))
            p.append(mlp.iniciar(numero_clases=3,
                            numero_ejemplos=300, 
                            graficar_datos=False,
                            learning_rate=i,
                            graficar = False,
                            f=funcion))
        precision.append(p)
    
    #graficar en 3d precision vs learning_rate vs neuronas
    x, y = np.meshgrid(learning, neuronas)
    z = np.array(precision)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('Precision vs learning_rate vs neuronas')	
    ax.set_xlabel('learning_rate')
    ax.set_ylabel('neuronas')
    ax.set_zlabel('precision')
    plt.show()

