import time
import random

arreglo = list(range(1, 1_000_001))

def busqueda_secuencial(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


def busqueda_binaria(arr, objetivo):
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio] == objetivo:
            return medio

        elif arr[medio] < objetivo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return -1

numero = int(input("Ingrese el número a buscar en el rango (1-1000000): "))

inicio = time.time()
posicion1 = busqueda_secuencial(arreglo, numero)
fin = time.time()
tiempo_secuencial = fin - inicio

inicio = time.time()
posicion2 = busqueda_binaria(arreglo, numero)
fin = time.time()
tiempo_binaria = fin - inicio


print("\nResultado")
print("....")

if posicion1 != -1:
    print(f"Número encontrado en la posición: {posicion1}")
else:
    print("Número no encontrado")

print(f"Tiempo de búsqueda secuencial: {tiempo_secuencial} segundos")

if posicion2 != -1:
    print(f"Número encontrado en la posición de manera binaria: {posicion2}")
else:
    print("Número no encontrado de manera binaria")

print(f"Tiempo de búsqueda binaria: {tiempo_binaria} segundos")