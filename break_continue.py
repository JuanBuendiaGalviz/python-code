
def run():
#    for contador in range(1001):
#        if contador%2 != 0:
#            continue
#       print(contador)

#    for i in range(0, 10000):
#        if i == 5798:
#            break
#       print(i)
    texto = input("Escribe un texto: ")

    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == "__main__":
    run()