from fuzzy_control import Controller
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud de la pertiga

# Simula el modelo del carro-pendulo.
# Parametros:
#   t_max: tiempo maximo (inicia en 0)
#   delta_t: incremento de tiempo en cada iteracion
#   theta_0: Angulo inicial (grados)
#   v_0: Velocidad angular inicial (radianes/s)
#   a_0: Aceleracion angular inicial (radianes/s2)

controlador = Controller()

def simular(t_max, delta_t, theta_0, v_0, a_0):
	theta = (theta_0 * np.pi) / 180
	v = v_0
	a = a_0

	# Simular
	y = []
	y_v = []
	f_v = []
	x = np.arange(0, t_max, delta_t)
	for t in x:

		fuzzy_ang = controlador.fuzzifier_ang(theta)
		fuzzy_vel = controlador.fuzzifier_vel(v)
		inference = controlador.fuzzy_inference(fuzzy_ang, fuzzy_vel)

		f = controlador.desfuzzifier(inference, 10, 80)
		f_v.append(f)
		a = calcula_aceleracion(theta, v, f)
		v = v + a * delta_t
		theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2
		
		if abs(theta*(180/np.pi)) >= 90:
			print('Fuerza insuficiente - Se cayo')
			break

		y.append(theta*(180/np.pi))
		y_v.append(v)
	


	fig, ax = plt.subplots(1, 2)
	figf, axf = plt.subplots()
	try:
		ax[0].plot(x[0:len(y)], y)

		ax[0].set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(delta_t) + " s")
		ax[0].grid()

	except:
		pass

	try:

		ax[1].plot(x[0:len(y_v)], y_v)
		ax[1].set(xlabel='time (s)', ylabel='Vel', title='Delta t = ' + str(delta_t) + " s")
		ax[1].grid()
	except:
		pass

	try:
		axf.plot(x[0:len(f_v)], f_v)
		axf.set(xlabel = 'time (s)', ylabel = 'Fuerza (N)', title='Delta t = ' + str(delta_t) + " s")
	except:
		pass
	
	plt.show()


# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, f):

    numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - CONSTANTE_m * CONSTANTE_l * np.power(v, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m))
    denominador = CONSTANTE_l * (4/3 - (CONSTANTE_m * np.power(np.cos(theta), 2) / (CONSTANTE_M + CONSTANTE_m)))
    return numerador / denominador




"""simular(10, 0.1, 45, 0, 0)

simular(10, 0.01, 45, 0, 0)

simular(10, 0.001, 45, 0, 0)"""

simular(30, 0.0001, 45, 5, 0)