#asegura que un dato sea flotante
def numero_flotante(a):
    try: 
        numero=float(a)
        return numero
    except:
        print('Error, tipo de dato no valido')
        a=input('ingrese nuevamente el valor: ')
        return numero_flotante(a)
    
def fun_suma( a, b):
    a=numero_flotante(a)
    b=numero_flotante(b)
    return a + b

def fun_resta( a, b):
    a=numero_flotante(a)
    b=numero_flotante(b)
    return a - b

def fun_producto( a, b):
    a=numero_flotante(a)
    b=numero_flotante(b)
    return a * b

def fun_division( a, b):
    a=numero_flotante(a)
    b=numero_flotante(b)
    try: 
        return a/b
    except: 
        print('Error, no es posible dividir entre 0')
        a=input('ingrese nuevamente el dividendo: ')
        b=input('ingrese nuevamente el divisor: ')
        return fun_division( a, b)