# def impimir_funcion():
#     print("mensaje especial")
#     print("learning using functions")


# impimir_funcion()
# impimir_funcion()
# impimir_funcion()
# def conversation(mensaje):
#     print("hola")
#     print("cómo estás?")
#     print(mensaje)


# opction = int(input("Elige un opcion (1,2,3): "))
# if opction == 1:
#     conversation("elegiste la opcion 1")
# elif opction == 2:
#     conversation("elgiste la opcion 2")
# elif opction == 3:
#     conversation("elgiste la opcion 3")
# else:
#     print("adios")


# def suma(a, b):
#     print("se suman 2 num")
#     result = a + b
#     return result


# sumatoria = suma(3, 4)
# print(sumatoria)

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuánto dinero" + tipo_pesos + "tienes?: ")
    pesos = float(pesos)
    result_dolar = pesos/valor_dolar
    # con el metodo round, recibe dos parametros; la variable y la cantidad de decimales a mostrar
    result_dolar = round(result_dolar, 3)
    result_dolar = str(result_dolar)
    print("Tienes $: " + result_dolar + " dólares")


menu = """
Welcome convert money 
1: Pesos colombianos
2: Pesos argentinos
3: pesos Mexicanos

Elige un opcion: 
"""
option = input(menu)
if option == "1":
    conversor("colombianos", 3769)
elif option == "2":
    conversor("argentinos", 65)
elif option == "3":
    conversor("mexicanos", 24)
else:
    print("Opcion no válida")
