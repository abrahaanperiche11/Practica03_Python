from main import numero_entero
from main import generar_lista_random
from main import ordena_lista

cantidad=20
cantidad=numero_entero(cantidad)
lista=generar_lista_random(cantidad)
print(f'la lista de numeros random es: {lista}')
lista_ordenada=ordena_lista(lista)
print(f'la lista ordenada de menor a mayor es: {lista_ordenada} ')