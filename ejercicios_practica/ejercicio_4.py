# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos condicionales y operador incremento

# Objetico
# Verificar cuanta veces (contar) el usuario
# ingresa por consola un número mayor a cero
cantidad_numeros_positivos = 0

# Alumno:
# Deberá solicitar tres números enteros por consola,
# cada nuḿero entero lo debe almacenar en variables llamadas:
# numero_1
# numero_2
# numero_3

numero_1 = int (input("ingrese numero 1: \n"))
numero_2 = int (input("ingrese numero 2: \n"))
numero_3 = int (input("ingrese numero 3: \n"))

print("numero 1:",numero_1)
print("numero 2:",numero_2)
print("numero 3:",numero_3)

if numero_1 > 0:
    cantidad_numeros_positivos +=1
else: 
    print('el numero es menor que cero')

if numero_2 > 0:
    cantidad_numeros_positivos +=1
else: 
    print('el numero es menor que cero')

if numero_3 > 0:
    cantidad_numeros_positivos +=1   
else: 
    print('el numero es menor que cero')
 
print("cantidad de nuemros positivos_:",cantidad_numeros_positivos)






# Deberá realizar un tres condicionales separados,
# en cada condicional deberá averiguar si cada número
# es mayor a cero.

# Por cada número mayor a cero (cada condicional que se cumpla)
# deberá incrementar en 1 (+= 1) la "variable cantidad_numeros_positivos"


# Al finalizar, imprimir en pantalla la variable cantidad_numeros_positivos



