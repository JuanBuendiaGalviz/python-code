def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("Cuantos pesos " + tipo_pesos + " tienes: "))

    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)


    print("Tienes $" + dolares + " en tus bolsillos")

menu = """
Bienvenido al conversor de monedas 💰

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos

Elige una opción:
"""
opcion = input(menu)

if opcion == str(1):
    conversor("Colombianos", 4089.30)
elif opcion == str(2):
    conversor("Argentinos", 116.76)
elif opcion == str(3):
    conversor("Mexicanos", 20.30)
else:
    print("Ingresa un número válido")

