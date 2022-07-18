import matplotlib.pyplot as plt
lista1=[[5,7,9],[2,5,3],[1,5,2],[2,4,6]]
lista2=[0,1,2,3]

fig,ax =plt.subplots()
ax.boxplot(lista1)
ax.set_xticklabels(lista2)
ax.set_ylabel("Dispersion de cada individuo")
ax.set_xlabel("Iteraciones")
plt.show()