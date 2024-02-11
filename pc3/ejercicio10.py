#importe de datos 
from ejercicio3 import Circulo
from ejercicio4 import Rectangulo

#asegura que el dato ingresado sea un número entero:
def numero_entero(n):
    try:
        numero=int(n)
        return numero
    except:
        print(f'Error dado que {n} no es un entero')
        n=input(f'ingrese correctamente el dato {n}: ')
        return numero_entero(n)
#asegura que el dato ingresado sea un número flotante
def numero_flotante(n):
    try:
        numero=float(n)
        return numero
    except:
        print(f'Error dado que {n} no es un número')
        n=input(f'ingrese correctamente el dato {n}: ')
        return numero_flotante(n)

#asegura que el menú siga hasta que el usuario quiera salir
while True:
    opcion=input('''Menú de opciones:
             1) Calcular el área de un círculo.
             2) Calcular el área de un rectángulo.
             3) Calcular el área de un cuadrado.
             4) Salir
             Ingresa la opción: ''')
    opcion=numero_entero(opcion)
    if opcion==1:
        radio=input('Ingresa la medida del radio del círculo: ')
        radio=numero_flotante(radio)
        resultado=Circulo(radio)
        resultado=resultado.area_circulo()
    elif opcion==2:
        largo=input('Ingrese la medida del largo: ')
        largo=numero_flotante(largo)
        ancho=input('Ingrese la medida del ancho: ')
        ancho=numero_flotante(ancho)
        resultado=Rectangulo(largo,ancho)
        resultado=resultado.area_rectangulo()
    elif opcion==3:
        lado=input('Ingrese la medida del lado: ')
        lado=numero_flotante(lado)
        resultado=Rectangulo(lado,lado)
        resultado=resultado.area_rectangulo()
    elif opcion==4:
        print('Espero haya sido de utilidad')
        break
    else:
        print('la opción escogida no se encuentra dentro de las opciones')
        print('-------------------------------')
        continue
    print(f'''
el resultado es: {resultado}''')
    print('-------------------------------')