#Cree un bucle For de Python.

for number in range(1, 11):
    print(number)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(x, y, z):
    return x + y + z 
    

print(suma(1, 2, 3))

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

lambda_suma = lambda x, y, z: x + y + z
print(lambda_suma(1, 2, 3))

'''Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 
*Sugerencia, si es necesario, utilice un bucle for in y el operador in.'''

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

for nombre_de_la_lista in lista_nombre:
    if nombre == nombre_de_la_lista:
        print(f'El nombre {nombre} coincide con el valor de la lista.')
        continue
    else:
        print(f'El nombre {nombre} no coincide con el valor de la lista.')







