from itertools import count
import numpy as np
import matplotlib.pyplot as plt
from Regresion import Regresion


def f(x):

    return np.sin(10*x)
    
    #return np.log10(abs(3*x))
   

r = Regresion(1, 100, 1, 50, f)


a = r.train_method(learning_rate=0.1, epochs=10000)

r.test_method()




















