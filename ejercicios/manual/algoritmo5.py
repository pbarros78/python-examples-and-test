def servir_agua_hervida (agua_hervida, contenedor):
    if (agua_hervida == False):
	    print('Tomar el hervidor y ponerle agua')
	    print('Encender el hervidor para hervir el agua')
	    print('Una vez hervida el agua servirla en la/el ', contenedor)
	    agua_hervida = True
    else:
        print('Tomar hervidor y servir el agua en la/el ', contenedor)
    return agua_hervida


#Servir_bebidas_calientes
agua_hervida = False
print('================================')
print('Hacer y servir café')
print('================================')
print('Tomar una taza')
print('Tomar una cuchara')
print('Buscar el café')
print('Buscar el endulzante')
print('Poner café en la taza')
print('Poner endulzante en la taza')
agua_hervida = servir_agua_hervida(agua_hervida, 'taza')
print('Revolver contenido')
print('Disfrutar del café')
print('================================')
print('Hacer y servir mate')
print('================================')
print('Tomar una matero')
print('Tomar una cuchara')
print('Buscar el mate')
print('Buscar el endulzante')
print('Poner mate en el matero')
print('Poner endulzante en el matero')
agua_hervida = servir_agua_hervida(agua_hervida, 'matero')
print('Revolver contenido o reposar')
print('Disfrutar del mate')
#FinAlgoritmo
