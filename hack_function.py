
def counter(n):
    for numeros in range(int(n+1)):

        if numeros == 0:
            continue
        numeros = str(numeros)
        print(numeros, end="")








if __name__ == "__main__":

    n = int(input("Ingresa un numero: "))

    counter(n)



