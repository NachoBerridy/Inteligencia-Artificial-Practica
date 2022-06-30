import numpy as np
import matplotlib.pyplot as plt

class Regresion:

    def __init__(self, neuronas_entrada, neuronas_ocultas, neuronas_salida, m, funcion):
        
        self.neuronas_entrada = neuronas_entrada
        self.neuronas_oculta = neuronas_ocultas
        self.neuronas_salida = neuronas_salida
        self.pesos = self.inicializar_pesos()
        self.train = self.generar_datos(m, funcion, 5000)
        self.test = self.generar_datos(m, funcion, 5000)
        self.validation = self.generar_datos(m, funcion, 5000)
        self.m  = m
        self.fun = funcion

    def generar_datos(self, m, func, amplitud):
 
        x = []
        y = []

        for i in range(m):
            rd = np.random.rand()
            
            if rd >= 0.5:
                y.append(func(i) + amplitud*rd)
            else:
                y.append(func(i) - amplitud*rd)

            
            x.append(i)

        return (np.array([x]).T, np.array([y]).T)
        
    def ejecutar_adelante(self, x):

        #(neuronas de entrada x neuronas ocultas) z
        #(neuronas ocultas x neuronas de salida) h
        #(neuronas de salida) y
        z = x.dotpesos['w1'] + self.pesos['b1']
        h = np.maximum(0, z)
        y = h.dot(self.pesos['w2']) + self.pesos['b2']

        return (z, h, y)
     
    def inicializar_pesos(self):

        randomgen = np.random.default_rng()
        w1 = 0.1 * randomgen.standard_normal((self.neuronas_entrada, self.neuronas_oculta))
        b1 = 0.1 * randomgen.standard_normal((1, self.neuronas_oculta))
        w2 = 0.1 * randomgen.standard_normal((self.neuronas_oculta, self.neuronas_salida))
        b2 = 0.1 * randomgen.standard_normal((1, self.neuronas_salida))
    
        return {"w1": w1, "b1": b1, "w2": w2, "b2": b2} 

    def regresion_loss(self, t , y):

        m = len(y)
        score = 0
        d = []

        for i in range(m):

            score = score +  (t[i] - y[i])**2
            d.append(-2*(t[i] - y[i]))

        return ((1/m)*score, np.array(d))

    def hacer_regresion(self, x):

        y = self.ejecutar_adelante(x)[2]

        return(y) 

    def train(self, learning_rate, epochs):
        print('Entrenando')
        #Para graficar
        loss_list = []
        it_list = []
        precision_list = []

        x = self.train[0]
        t = self.train[1]

        for i in range(epochs):

            z, h, y = self.ejecutar_adelante(x)
            z_val, h_val, y_val = self.ejecutar_adelante(self.validation[0])

            loss, d = self.regresion_loss(self.fun, t, y)

            # Extraemos los pesos a variables locales
            w1 = self.pesos["w1"]
            b1 = self.pesos["b1"]
            w2 = self.pesos["w2"]
            b2 = self.pesos["b2"]
        
            # Ajustamos los pesos: Backpropagation
            dL_dy = d                # Para todas las salidas, L' = p (la probabilidad)...
            #dL_dy[range(m), t] -= 0  # ... excepto para la clase correcta
            dL_dy /= self.m
            dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
            dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2
            dL_dh = dL_dy.dot(w2.T)
        
            dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
            dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)
            dL_dw1 = x.dot(dL_dz.T)                        # Ajuste para w1
            dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1
            # Aplicamos el ajuste a los pesos
            w1 += -learning_rate * dL_dw1
            b1 += -learning_rate * dL_db1
            w2 += -learning_rate * dL_dw2
            b2 += -learning_rate * dL_db2
            # Actualizamos la estructura de pesos
            # Extraemos los pesos a variables locales
            self.pesos["w1"] = w1
            self.pesos["b1"] = b1
            self.pesos["w2"] = w2
            self.pesos["b2"] = b2

            if i%100 == 0:

                precision_list.append(self.regresion_loss(self.validation[1], y_val)[0])

                loss_list.append(loss)

                it_list.append(i)


        fig, ax = plt.subplots(2, 2)

        ax[0][0].scatter(x, t)
        ax[0][0].plot(x, y)

        ax[0][1].scatter(self.validation[0], self.validation[1])
        ax[0][1].scatter(self.validation[0], y_val)

        ax[1][0].plot(it_list, loss_list)

        ax[1][1].plot(it_list, precision_list)

        plt.show()
        return(0)












     
        
