from Regresion import Regresion


def f(x):

    return x**2-x*50+2

r = Regresion(1, 100, 1, 50, f)
print(type(r))

print(r.pesos['b2'])

a = r.train(learning_rate=1,epochs=10000)
x,y = r.generar_datos(10,f,1000)