objetivo = int(input("Ingresa un número: "))

respuesta  = 0 

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f"la raiz cuadradra de {objetivo} es {respuesta}")
else:
    print(f"{objetivo} no tiene una raiz cuadrada exacta")