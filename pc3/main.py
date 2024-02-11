import random
#asegura que el número ingresado sea entero
def numero_entero(a):
    try: 
        numero=int(a)
        return numero
    except:
        print('Error, Tipo de dato no válido')
        a=input('por favor ingrese otra vez el dato: ')
        return numero_entero(a)


#ordena una lista ingresada de menor a mayor y devuelve una lista ordenada
def ordena_lista(a):
    lista=list(a)
    lista.sort()
    return lista
   
#genera una cantidad x de números random y devuelve la lista
def generar_lista_random(cantidad_numeros):
    lista_numeros_random=[]
    for _ in range(cantidad_numeros):
        numero_random = random.randint(0,100)
        lista_numeros_random.append(numero_random)
    return lista_numeros_random