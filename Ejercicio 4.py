min_empleados = 10
min_facturacion = 2*10^6 # esto hace referencia a los dos millones

"""
codigo que no se va a ejecutar
"""
min_balance = 2*10^6 # millones, otra vez

empleados = 20
facturacion = 18
balance = 5 

es_microempresa = empleados < min_empleados and facturacion <= min_facturacion
es_pequenia = not es_microempresa and (balance <=10 or empleados <50 and facturacion <=10)
print(es_microempresa) # con esto se comprobará lo siguiente, si da falso entonces lo otro es verdadero
print(es_pequenia)
print(type(es_pequenia)) #comprobamos que lo hemos hecho bien si es que sale de tipo booleano