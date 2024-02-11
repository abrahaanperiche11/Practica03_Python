fraccion=input('por favor ingrese una fracción en formato (X/Y): ')
contiene=fraccion.find("/")
#asegura que se cumpla el formato:
while True:
    if contiene>=0:
        numerador, denominador=fraccion.split('/')
        #asegura que el numerador sea entero:
        try: 
            numero=int(numerador)
        except:
            print('Value Error')
            fraccion=input('Por favor ingrese otra vez una fracción en formato (X/Y): ')
            contiene=fraccion.find("/")
            continue
        numerador=int(numerador)
        #asegura que el denominador sea entero:
        try: 
            numero=int(denominador)
        except:
            print('Value Error')
            fraccion=input('Por favor ingrese otra vez una fracción en formato (X/Y): ')
            contiene=fraccion.find("/")
            continue
        denominador=int(denominador)
        #asegura que la división sea diferente de x/0:
        try:
            numero=numerador/denominador
        except:
            print('ZeroDivisionError')
            fraccion=input('Por favor ingrese otra vez una fracción en formato (X/Y): ')
            contiene=fraccion.find("/") 
            continue   
        #asegura que el dividendo sea menor al divisor:
        if denominador>=numerador:
            porcentaje=numerador*10000//denominador/100
            if porcentaje<1:
                print('E')
            elif porcentaje>99:
                print('F')
            else:
                print(f'{porcentaje}%')
        else: 
            print('el Numerador es mayor al denominador')
            fraccion=input('Por favor ingrese otra vez una fracción en formato (X/Y): ')
            contiene=fraccion.find("/") 
            continue
        break
    else:
        fraccion=input('Error de formato, por favor ingrese otra vez una fracción en formato (X/Y): ')
        contiene=fraccion.find("/")
        