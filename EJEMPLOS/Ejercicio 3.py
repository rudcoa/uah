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
print(es_microempresa)