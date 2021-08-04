# CONVERTIDOS DE PESOS COLOMBIANOS A DÓLARES
menu = """
Welcome convert money 
1: Pesos colombianos
2: Pesos argentinos
3: pesos Mexicanos

Elige un opcion: 
"""
option = input(menu)
if option == "1":
    pesos = input("¿cuánto dinero colombiana tienes?: ")
    pesos = float(pesos)
    dolar = 3769
    result_dolar = pesos/dolar
    # con el metodo round, recibe dos parametros; la variable y la cantidad de decimales a mostrar
    result_dolar = round(result_dolar, 3)
    result_dolar = str(result_dolar)
    print("Tienes $: " + result_dolar + " dólares")
elif option == "2":
    pesos = input("¿cuánto dinero argentino tienes?: ")
    pesos = float(pesos)
    dolar = 65
    result_dolar = pesos/dolar
    # con el metodo round, recibe dos parametros; la variable y la cantidad de decimales a mostrar
    result_dolar = round(result_dolar, 3)
    result_dolar = str(result_dolar)
    print("Tienes $: " + result_dolar + " dólares")
elif option == "3":
    pesos = input("¿cuánto dinero mexicano tienes?: ")
    pesos = float(pesos)
    dolar = 24
    result_dolar = pesos/dolar
    # con el metodo round, recibe dos parametros; la variable y la cantidad de decimales a mostrar
    result_dolar = round(result_dolar, 3)
    result_dolar = str(result_dolar)
    print("Tienes $: " + result_dolar + " dólares")
else:
    print("Opcion no válida")


# CONVERTIDOR DE DÓLARES A PESOS COLOMBIANOS
# peso_dolar = input("Cuántos dólares tienes?: ")
# peso_dolar = float(peso_dolar)
# peso = 3769
# conver = peso_dolar * peso
# conver = round(conver, 2)
# conver = str(conver)
# print("De dólares a peso colombino es: " + conver)
