
import pandas as pd
import math


def generar_aleatorios(datos, a, c, m, x0, n):
    for i in range(n):
        xprox = (a*x0 + c)%m
        x0 = xprox
        ri = xprox/m
        datos.append(ri)



def d_mas(dmas, datos):
    i = 1
    cant = len(datos)
    for numero in datos:
        n = (i/cant) - numero
        i += 1
        dmas.append(n)



def d_menos(dmenos, datos):
    i = 1
    cant = len(datos)
    for numero in datos:
        n = numero - ((i-1)/cant)
        i += 1
        dmenos.append(n)



def verificacion(resultado, n, alfa):
    tabla = 'tabla.csv'
    datos = pd.read_csv(tabla)
    if n <= 50:
        #Columnas de la tabla
        if alfa == 0.20:
            columna = 0
        if alfa == 0.10:
            columna = 1
        if alfa == 0.05:
            columna = 2
        if alfa == 0.02:
            columna = 3
        if alfa == 0.01:
            columna = 4
        if alfa == 0.005:
            columna = 5
        if alfa == 0.002:
            columna = 6
        if alfa == 0.001:
            columna = 7
        valor_tabla = datos.iloc[n-1, columna]
    else:
        if alfa == 0.20:
            valor_tabla = 1.07/math.sqrt(n)
        if alfa == 0.10:
            valor_tabla = 1.22/math.sqrt(n)
        if alfa == 0.05:
            valor_tabla = 1.36/math.sqrt(n)
        if alfa == 0.02:
            valor_tabla = 1.52/math.sqrt(n)
        if alfa == 0.01:
            valor_tabla = 1.63/math.sqrt(n)
        if alfa == 0.005:
            valor_tabla = 1.73/math.sqrt(n)
        if alfa == 0.002:
            valor_tabla = 1.85/math.sqrt(n)
        if alfa == 0.001:
            valor_tabla = 1.95/math.sqrt(n)
   
    if resultado <= valor_tabla:
        print("El valor D = {} es menor o igual que el tabulado {} para n = {} y alfa = {}".format(resultado,valor_tabla,n, alfa))
        print("La prueba es aceptada.")
    else:
        print("El valor D = {} es mayor o igual que el tabulado {} para n = {} y alfa = {}".format(resultado,valor_tabla,n, alfa))
        print("La prueba es rechazada.")
    


def mayor(Dmas, Dmenos):
    if Dmas <= Dmenos:
        resultado = Dmenos
    else:
        resultado = Dmas
    return resultado



datos = []
dmenos = []
dmas = []



a = int(input("Ingrese el parametro a: "))
c = int(input("Ingrese el parametro c: "))
m = int(input("Ingrese el parametro m: "))
x0 = int(input("Ingrese el parametro x0: "))
n = int(input("Ingrese la cantidad de muestra: "))
alfa = input("Ingrese el parametro alfa: ")
alfa = float(alfa)



generar_aleatorios(datos, a, c, m, x0, n)
datos.sort()   #ordena menor a mayor las variables aleatorias
d_mas(dmas, datos)     #cargar el vector D+
d_menos(dmenos, datos) #cargar el vector D-
dmas_max = max(dmas)   #obtener maximo de D+
dmenos_max = max(dmenos)  #obtener maximo de D-
resultado = mayor(dmas_max, dmenos_max)  #obtener el mas grande de ambos



print("Usando los parametros a = {}, c = {}, m = {}, x0 = {} se han generado los datos.".format(a,c,m,x0))
print("\nVariables aleatorias generadas: {}".format(datos))
print("\nVector con D+: {}".format(dmas))
print("\nVector con D-: {}".format(dmenos))
print("\nValor maximo de D+: {}".format(dmas_max))
print("\nValor maximo de D-: {}".format(dmenos_max))
print("\nResultado D: ({},{}) el mayor entre ambos es {}".format(dmas_max, dmenos_max, resultado))
verificacion(resultado, n, alfa)  #validar con la tabla