

def run():
    LIMITE = 1000000
    contador = 0
    potencia_de_dos = 2**contador

    while potencia_de_dos < LIMITE:
        contador += 1
        print(potencia_de_dos)
        potencia_de_dos = 2**contador




if __name__ == "__main__":
    run()