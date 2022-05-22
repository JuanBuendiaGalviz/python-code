import random 


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Ingres un numero del 1 al 100: "))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Es numero es mas grande")
        else:
            print("El numero es mas pequeño")
        numero_elegido = int(input("Ingresa de nuevo un número: "))
    print("Adivinaste el número!!")


if __name__ == "__main__":
    run()