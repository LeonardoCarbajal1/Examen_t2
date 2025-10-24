import random

def generar_palabra():
    palabra = ''
    for i in range(4):
        numero = random.randint(97, 122)
        letra = chr(numero)
        palabra += letra
    return palabra

def generar_matriz(tamano):
    matriz = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            fila.append(generar_palabra())
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))
    print()

def tiene_vocal(palabra):
    for letra in palabra:
        if letra in 'aeiou':
            return True
    return False

def contar_vocales(matriz):
    if len(matriz) == 1:
        fila = matriz[0]
        if len(fila) == 1:
            return 1 if tiene_vocal(fila[0]) else 0
        mitad = len(fila) // 2
        return contar_vocales([fila[:mitad]]) + contar_vocales([fila[mitad:]])
    mitad = len(matriz) // 2
    return contar_vocales(matriz[:mitad]) + contar_vocales(matriz[mitad:])

tamano = int(input("Ingrese el tamaño de la matriz: "))
matriz = generar_matriz(tamano)
mostrar_matriz(matriz)
print("Cantidad de palabras que tienen al menos una vocal:", contar_vocales(matriz))
