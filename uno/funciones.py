# def imprimir_mensaje():
#     print('Mensaje especial!')
#     print('Estoy aprendiendo Python :D')
#def es para la funcion

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print('Hola')
    print('¿Como estas?')
    print(mensaje)
    print('Adios')
    return opcion

opcion = int(input('Elige una opcion 1, 2 o 3: '))

if opcion == 1:
    conversacion('Elegiste la opcion 1')
elif opcion == 2:
    conversacion('Elegiste la opcion 2')
elif opcion == 3:
    conversacion('Elegiste la opcion 3')    
else:
    print('Elegi una opcion valida por favor.') 