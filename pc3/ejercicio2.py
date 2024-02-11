def numero_entero(n):
    try:
        numero=int(n)
        return numero
    #no ponemos un rango de notas porque el ejercicio no nos indica uno, pero en caso hubiera, utilizariamos
    #assert.
    except:
        print(f'Error dado que {n} no es un entero')
        n=input(f'ingrese correctamente el dato {n}: ')
        return numero_entero(n)
        
        
cadena_notas=input('por favor ingrese la lista de notas separada por comas: ')
lista_notas=[]
for nota in cadena_notas.split(','):
    nota=numero_entero(nota)
    nota=int(nota)
    lista_notas.append(nota)
    
print(f'la lista de notas es: {lista_notas}')