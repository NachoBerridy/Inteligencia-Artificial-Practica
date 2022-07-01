import numpy as np
import matplotlib.pyplot as plt
import math 


class MLP:


    def __init__(self, neuronas_ocultas, neuronas_entrada = 2, numero_clases = 3):
        
        # Inicializa pesos de la red
        self.neuronas_capa_ocultas = neuronas_ocultas
        self.neuronas_entrada = neuronas_entrada
        self.numero_clases = numero_clases
        self.pesos = self.inicializar_pesos(n_entrada= self.neuronas_entrada, 
                                            n_capa_2 = self.neuronas_capa_ocultas,
                                            n_capa_3 = self.numero_clases)
        
        
# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)

    def generar_datos_clasificacion(self, cantidad_ejemplos, cantidad_clases, factor_angulo = 0.79, amplitud_aleatoriedad = 0.1):
        FACTOR_ANGULO = factor_angulo
        AMPLITUD_ALEATORIEDAD = amplitud_aleatoriedad

        # Calculamos la cantidad de puntos por cada clase, asumiendo la misma cantidad para cada 
        # una (clases balanceadas)
        n = int(cantidad_ejemplos / cantidad_clases)

        # Entradas: 2 columnas (x1 y x2)
        x = np.zeros((cantidad_ejemplos, 2))
        # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
        t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")

        randomgen = np.random.default_rng()

        # Por cada clase (que va de 0 a cantidad_clases)...
        for clase in range(cantidad_clases):
            # Tomando la ecuacion parametrica del circulo (x = r * cos(t), y = r * sin(t)), generamos 
            # radios distribuidos uniformemente entre 0 y 1 para la clase actual, y agregamos un poco de
            # aleatoriedad
            radios = np.linspace(0, 1, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)

            # ... y angulos distribuidos tambien uniformemente, con un desfasaje por cada clase
            angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n)

            # Generamos un rango con los subindices de cada punto de esta clase. Este rango se va
            # desplazando para cada clase: para la primera clase los indices estan en [0, n-1], para
            # la segunda clase estan en [n, (2 * n) - 1], etc.
            indices = range(clase * n, (clase + 1) * n)

            # Generamos las "entradas", los valores de las variables independientes. Las variables:
            # radios, angulos e indices tienen n elementos cada una, por lo que le estamos agregando
            # tambien n elementos a la variable x (que incorpora ambas entradas, x1 y x2)
            x1 = radios * np.sin(angulos)
            x2 = radios * np.cos(angulos)
            x[indices] = np.c_[x1, x2]

            # Guardamos el valor de la clase que le vamos a asociar a las entradas x1 y x2 que acabamos
            # de generar
            t[indices] = clase

        return x, t

    
    def generar_datos_clasificacion2(self, cantidad_ejemplos, cantidad_clases, factor_angulo = 0.79, amplitud_aleatoriedad = 0.1):
        FACTOR_ANGULO = factor_angulo
        AMPLITUD_ALEATORIEDAD = amplitud_aleatoriedad

        # Calculamos la cantidad de puntos por cada clase, asumiendo la misma cantidad para cada 
        # una (clases balanceadas)
        n = int(cantidad_ejemplos / cantidad_clases)

        # Entradas: 2 columnas (x1 y x2)
        x = np.zeros((cantidad_ejemplos, 2))
        # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
        t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")

        randomgen = np.random.default_rng()
        # Por cada clase (que va de 0 a cantidad_clases)...
        for clase in range(cantidad_clases):
            # Tomando la ecuacion parametrica del circulo (x = r * cos(t), y = r * sin(t)), generamos 
            # radios distribuidos uniformemente entre 0 y 1 para la clase actual, y agregamos un poco de
            # aleatoriedad
            #radios = np.linspace(0, 1, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)
            radios = np.linspace(0, 1, n) + (clase+1)*AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)
            # ... y angulos distribuidos tambien uniformemente, con un desfasaje por cada clase
            angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n)

            # Generamos un rango con los subindices de cada punto de esta clase. Este rango se va
            # desplazando para cada clase: para la primera clase los indices estan en [0, n-1], para
            # la segunda clase estan en [n, (2 * n) - 1], etc.
            indices = range(clase * n, (clase + 1) * n)

            # Generamos las "entradas", los valores de las variables independientes. Las variables:
            # radios, angulos e indices tienen n elementos cada una, por lo que le estamos agregando
            # tambien n elementos a la variable x (que incorpora ambas entradas, x1 y x2)
            x1 =  radios+3*AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)
            x2 = (2*clase-1)+7*AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)+radios* np.cos(angulos)
            x[indices] = np.c_[x1, x2]

            # Guardamos el valor de la clase que le vamos a asociar a las entradas x1 y x2 que acabamos
            # de generar
            t[indices] = clase

        return x, t



    def inicializar_pesos(self, n_entrada, n_capa_2, n_capa_3):
        randomgen = np.random.default_rng()

        w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
        b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))

        w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
        b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))

        return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}

    def ejecutar_adelante(self, x, pesos,funcion):
        # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
        z = x.dot(pesos["w1"]) + pesos["b1"]
        #print(type(z))

        if funcion==1:
            # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
            h = np.maximum(0, z)
        elif funcion==2:
            h=(1/(1+(np.exp(-z))))

        # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
        # las neuronas y para todos los ejemplos proporcionados
        y = h.dot(pesos["w2"]) + pesos["b2"]

        return {"z": z, "h": h, "y": y}

    def clasificar(self, x, pesos):
        # Corremos la red "hacia adelante"
        resultados_feed_forward = self.ejecutar_adelante(x, pesos,funcion=1)
        
        # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
        # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
        # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
        # (es decir, por filas)
        max_scores = np.argmax(resultados_feed_forward["y"], axis=1)

        # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
        # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
        # retornamos la primera columna
        try:
            m = max_scores[:, 0]
        except:
            m = max_scores[:]

        return m

    # x: n entradas para cada uno de los m ejemplos(nxm)
    # t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
    # pesos: pesos (W y b)

    def loss(self, y, m, t):
        
        
        # LOSS
        # a. Exponencial de todos los scores
        exp_scores = np.exp(y)

        # b. Suma de todos los exponenciales de los scores, fila por fila (ejemplo por ejemplo).
        #    Mantenemos las dimensiones (indicamos a NumPy que mantenga la segunda dimension del
        #    arreglo, aunque sea una sola columna, para permitir el broadcast correcto en operaciones
        #    subsiguientes)

        sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)

        # c. "Probabilidades": normalizacion de las exponenciales del score de cada clase (dividiendo por 
        #    la suma de exponenciales de todos los scores), fila por fila

        p = exp_scores / sum_exp_scores

        # d. Calculo de la funcion de perdida global. Solo se usa la probabilidad de la clase correcta, 
        #    que tomamos del array t ("target")

        loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))

        return (loss, p)
        
    def train(self, x, t, pesos, learning_rate, epochs, x_validacion, t_validacion,graficar,f):
        
        mejores_pesos = pesos
        # Cantidad de filas  (i.e. cantidad de ejemplos)
        m = np.size(x, 0) 
        
        #Listas para graficas
        precision = []
        recall = []
        f1 = []
        
        loss_train = []
        loss_validacion = []
        
        dloss_val_list = []
        for i in range(epochs):
            # Ejecucion de la red hacia adelante
            resultados_feed_forward = self.ejecutar_adelante(x, pesos,funcion=f)
            y_validacion = self.ejecutar_adelante(x_validacion, pesos,funcion=f)['y']
            y = resultados_feed_forward["y"]
            h = resultados_feed_forward["h"]
            z = resultados_feed_forward["z"]

            loss, p = self.loss(y,m,t)

            # Mostramos solo cada 1000 epochs
            if i %1000 == 0:
                print("Loss epoch", i, ":", loss)

            # Extraemos los pesos a variables locales
            w1 = pesos["w1"]
            b1 = pesos["b1"]
            w2 = pesos["w2"]
            b2 = pesos["b2"]
            
            # Ajustamos los pesos: Backpropagation
            dL_dy = p                # Para todas las salidas, L' = p (la probabilidad)...
            dL_dy[range(m), t] -= 1  # ... excepto para la clase correcta
            dL_dy /= m

            dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
            dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2

            dL_dh = dL_dy.dot(w2.T)


            if f==1:
                dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
                dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)
           
            elif f==2:
                dL_dz = dL_dh*(h*(1-h))  #derivada de la funcion sigmoide dh/dz = h*(1-h) 


            dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
            dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1

            # Aplicamos el ajuste a los pesos
            w1 += -learning_rate * dL_dw1
            b1 += -learning_rate * dL_db1
            w2 += -learning_rate * dL_dw2
            b2 += -learning_rate * dL_db2

            # Actualizamos la estructura de pesos
            # Extraemos los pesos a variables locales
            pesos["w1"] = w1
            pesos["b1"] = b1
            pesos["w2"] = w2
            pesos["b2"] = b2

            if i%200 == 0:
                
                scores = self.clasificar(x_validacion, pesos)
                val = self.accuracy(t_validacion, scores, 3)

                precision.append((sum(val[0]))/3)
                recall.append((sum(val[1]))/3)
                f1.append((sum(val[2]))/3)
                
                loss_train.append(loss)
                loss_validacion.append(self.loss(y_validacion, m, t_validacion)[0])
                

                #Cretetio de parada mediante derivadas

                if len(precision)>2:
                    
                    d_loss_validation = (3*loss_validacion[-1]-4*loss_validacion[-2]+loss_validacion[-3])/(2*200)
                    dloss_val_list.append(d_loss_validation)
                    d_loss_train = (3*loss_train[-1]-4*loss_train[-2]+loss_train[-3])/(2*200)
                    d_f1 = (3*f1[-1]-4*f1[-2]+f1[-3])/(2*200)
                    d_precision = (3*precision[-1]-4*precision[-2]+precision[-3])/(2*200)
                    d_recall = (3*recall[-1]-4*recall[-2]+recall[-3])/(2*200)
                    
                    if len(dloss_val_list)>5:
                        if (np.sign(dloss_val_list[-1]) == 1 and 
                            np.sign(dloss_val_list[-2]) == 1 and
                            np.sign(dloss_val_list[-3]) == 1 and
                            
                            np.sign(d_f1) == -1):

                            break
       
        if graficar == True:
            fig, ax = plt.subplots(1, 2)
            
            ax[0].plot(f1, marker = 'o')
            ax[0].set(title = 'F1 SCORE vs Epoch', ylabel = 'F1', xlabel = 'Epoch*200' )
            ax[0].grid()

            ax[1].plot(loss_train, label = 'Train')
            ax[1].plot(loss_validacion, label = 'Validacion')
            ax[1].set(title = 'LOSS vs Epoch', ylabel = 'loss', xlabel = 'Epoch*200' )
            ax[1].grid()
            
            plt.legend()
            plt.show()
        #print ("Precision = ",precision[-1])
        #print ()
        #print ()
        return (pesos, precision[-1])

    def accuracy(self, t, max_scores, cantidad_clases):
        t = list(t)
        max_scores = list(max_scores)
        precision = []
        recall = []
        f1 = [] 

        for i in range(cantidad_clases):

            a = 0 #Cantidad de ejemplos clasificados como i correctamente

            for j in range(len(t)):

                if t[j] == max_scores[j] and t[j] == i:
                    a = a+1
                    
            b = max_scores.count(i) #Cantidad total de ejemplos clasificados como i
            c = t.count(i) #Cantidad total de ejemplos en la clase i
            try:
                precision.append(round(a/b, 4))
            except:
                precision.append(0)

            recall.append(round(a/c, 4))

            try:
                f1.append(round((2*precision[i]*recall[i])/(precision[i]+recall[i]), 4))
            except:
                f1.append(0)

        return (precision, recall, f1)
            
    def iniciar(self, numero_clases, numero_ejemplos, graficar_datos,learning_rate,graficar,f):
        # Generamos datos
        x, t = self.generar_datos_clasificacion(numero_ejemplos, numero_clases)
        x_validacion, t_validacion = self.generar_datos_clasificacion(cantidad_ejemplos=300, cantidad_clases=3)

        # Graficamos los datos si es necesario
        if graficar_datos:
            # Parametro: "c": color (un color distinto para cada clase en t)
            fig, ax = plt.subplots(1, 2)
            ax[0].scatter(x[:, 0], x[:, 1], c=t)
            ax[1].scatter(x_validacion[:, 0], x_validacion[:, 1], c=t_validacion)
            plt.show()

        # Entrena
        LEARNING_RATE = learning_rate
        EPOCHS=30000
        """print(x)
        if f==2: #normalizar datos para la funcion sigmoide
            x = ((x - np.minimum(0,x))/(np.maximum(0,x)- np.minimum(0,x)))
            t = ((t - np.minimum(0,t))/(np.maximum(0,t)- np.minimum(0,t)))
        print(x)"""
        self.pesos, pres = self.train(x, t, self.pesos, LEARNING_RATE, EPOCHS, x_validacion, t_validacion,graficar, f)

        

        return pres


    def iniciar2(self, numero_clases, numero_ejemplos, graficar_datos,learning_rate,graficar,f):
        # Generamos datos
        x, t = self.generar_datos_clasificacion2(numero_ejemplos, numero_clases)
        x_validacion, t_validacion = self.generar_datos_clasificacion2(cantidad_ejemplos=300, cantidad_clases=3)

        # Graficamos los datos si es necesario
        if graficar_datos:
            # Parametro: "c": color (un color distinto para cada clase en t)
            fig, ax = plt.subplots(1, 2)
            ax[0].scatter(x[:, 0], x[:, 1], c=t)
            ax[1].scatter(x_validacion[:, 0], x_validacion[:, 1], c=t_validacion)
            plt.show()

        # Entrena
        LEARNING_RATE = learning_rate
        EPOCHS=30000

        if f==2: #normalizar datos para la funcion sigmoide
            x = ((x - np.minimum(0,x))/(np.maximum(0,x)- np.minimum(0,x)))
            t = ((t - np.minimum(0,t))/(np.maximum(0,t)- np.minimum(0,t)))
        self.pesos = self.train(x, t, self.pesos, LEARNING_RATE, EPOCHS, x_validacion, t_validacion,graficar,f)


    def iniciar3(self, numero_clases, numero_ejemplos, graficar_datos,learning_rate,graficar,f,x,t,x_validacion, t_validacion):

            # Graficamos los datos si es necesario
            if graficar_datos:
                # Parametro: "c": color (un color distinto para cada clase en t)
                fig, ax = plt.subplots(1, 2)
                ax[0].scatter(x[:, 0], x[:, 1], c=t)
                ax[1].scatter(x_validacion[:, 0], x_validacion[:, 1], c=t_validacion)
                plt.show()

            # Entrena
            LEARNING_RATE = learning_rate
            EPOCHS=30000

            self.pesos, pres = self.train(x, t, self.pesos, LEARNING_RATE, EPOCHS, x_validacion, t_validacion,graficar,f)
            return pres
     
    def test_method(self):
        
        x_test, t_test = self.generar_datos_clasificacion(cantidad_ejemplos=300, cantidad_clases=3)
        max_score = self.clasificar(x_test, self.pesos)
        precision, recall, f1 = self.accuracy(t_test, max_score, self.numero_clases)
        
     

        clases = np.linspace(0, self.numero_clases-1, self.numero_clases)
        fig2, ax2 = plt.subplots(1, 3)
        
        ax2[0].bar(clases, precision)
        ax2[0].set(title = 'Precision vs Clase', ylabel = 'Precision', xlabel = 'Clase')
        ax2[1].bar(clases ,recall)
        ax2[1].set(title = 'Recall vs Clase', ylabel = 'Recall', xlabel = 'Clase')
        ax2[2].bar(clases, f1)
        ax2[2].set(title = 'F1 vs Clase', ylabel = 'F1', xlabel = 'Clase')
        plt.show()
