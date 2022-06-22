from MLP import MLP
import matplotlib.pyplot as plt

mlp = MLP()


pesos = mlp.iniciar(numero_clases=3, numero_ejemplos=300, graficar_datos=False)
