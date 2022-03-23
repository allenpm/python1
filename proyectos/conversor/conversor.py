def conversor(tipo_moneda, valor_moneda, cantidad_pesos):
    cantidad_dinero = cantidad_pesos/valor_moneda
    cantidad_dinero = str(cantidad_dinero)
    print("Usted tiene: "+ tipo_moneda + cantidad_dinero)

def run():
    menu = '''
    ¡Hola! Bienvenid@ si estas aca es porque queres convertir tu plata en otra moneda. 
    Te pido que por favor me digas a que moneda queres convertirlo. Las opciones son:

    1-Dolares
    2-Euros
    3-Reales.

    '''
    option = input('Ingrese su eleccion por favor: ')
    cantidad_pesos = input('Ingrese cuanta plata tiene: ')
    cantidad_pesos = float(cantidad_pesos)
    if option == '1':
        conversor('U$S', 109.54, cantidad_pesos)
    elif option == '2':
        conversor('€', 121.27, cantidad_pesos)
    elif option == '3':
        conversor('R$', 21.86, cantidad_pesos)
    else:
        input('Por favor ingrese una opcion valida: ')       

if __name__ == '__main__':
    run()