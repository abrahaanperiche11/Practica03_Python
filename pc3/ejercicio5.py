def numero_entero(n):
    try:
        numero=int(n)
        return numero
    except:
        print(f'Error dado que {n} no es un entero')
        n=input(f'ingrese correctamente el dato {n}: ')
        return numero_entero(n)

class Alumno:
    
    lista_notas=[]
    
    #inicialización:
    def __init__(self, nombre:str, numero_registro:int):
        self.nombre = nombre
        self.numero_registro=numero_registro
    #método de display: muestra toda la info del estudiante
    def Display(self):
        print(f'nombre del alumno: {self.nombre}, número de registro: {self.numero_registro}')
        
    #método de setAge: asigna la edad del estudiante
    def setAge(self, edad):
        edad=numero_entero(edad)
        self.edad=edad
        # return self.edad
        return print(f'la edad del alumno es: {self.edad}')
    
    #método de setNota: asigna las notas del estudiante
    def setNota(self):
        while True:
            estado_nota=input('Desea ingresar una nota? (si/no): ')
            if estado_nota.lower()=='si':
                nota=input('Por favor ingrese la nota: ')
                nota=numero_entero(nota)
                self.lista_notas.append(nota)
            elif estado_nota.lower()=='no':
                break
            else:
                print('Esta opción no es valida')
                continue
        return print(f'la lista de notas de {self.nombre} es: {self.lista_notas}')

#Ejemplo
alumno_1=Alumno('Abrahaan','AAPM11')
alumno_1.Display()
alumno_1.setAge(21)
alumno_1.setNota()