def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuántos pesos ' + tipo_pesos + ' tenes?: ')
    pesos = float(pesos) 
    # float transforma valor o contenido de una variable a un decimal
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    #round(variable, cantidad de numeros despues de la coma que quiero). Esto permite achicar el numero de dolares.
    dolares = str(dolares)
    print('Tienes U$S' + dolares + '.')
menu = '''
¡Bienvenido al conversor de monedas! :)

1 - Pesos argentinos
2 - Pesos colombianos
3 - Pesos mexicanos
Elige una opcion '''

opcion = int(int(input(menu)))

if opcion == 1:
    conversor("argentinos", 109.54)
elif opcion == 2:
    conversor("colombianos", 3819.84)
elif opcion == 3:
    conversor("mexicanos", 20.36)
else:
    print('Ingrese un numero valido por favor.')


