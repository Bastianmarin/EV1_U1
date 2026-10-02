import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt 

CSVEjemplo = pandas.read_csv("C:\\Users\\ALUMNO\\Desktop\\bastian\\EJEMPLO.csv", header=0, sep=",")

Datoslista = {
    "columna 1" : [10,20,30,40],
    "columna 2" : [1,3,5,7],
    "columna 3" : [13,26,39,52]
}
Listapanda = pandas.DataFrame(Datoslista)

print("Maximo de columna 1")
print (max(Datoslista["columna 1"]))
print ("Minimo de columna 1") 
print (min(Listapanda["columna 1"]))

print("Promedio de Columna 2")
print (np.mean(Datoslista["columna 2"]))
print("Desviacion de Columna 2")
print(np.std(Listapanda["columna 2"]))

print("Varianza de Columna 3")
print(np.var(Listapanda["columna 3"]))

print("------------------------------------------------------")

x = Listapanda["columna 1"]
y = Listapanda["columna 2"]

slope, intercept = np.polyfit(x,y,1)

print("Pendiente:",slope)
print("Intercepto:",intercept)

xpoints = np.array(Datoslista["columna 1"])
ypoints = np.array(Datoslista["columna 2"])

plt.plot(xpoints,ypoints)
plt.show()
print("------------------------------------------------------")

df = pandas.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df.head())
print(df.groupby("Sex")["Survived"].mean())
df.groupby("Sex")["Survived"].mean().plot(kind="box")
plt.show()