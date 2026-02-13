# region CODE 0 EJEMPLO ANTERIOR MEDIR TU VELOCIDAD DE TECLEO
# Cómo medir el tiempo que demoras en teclear una cadena
# import time
# inicio = time.time()  # instante justo antes del input
# nombre1 = input("Escribe tu nombre --> ")
# t1 = time.time() - inicio #tiempo transcurrido mientras teclea el nombre

# inicio = time.time()  # instante justo antes del input
# nombre2 = input("Vuelvelo a teclear --> ")
# t2 = time.time() - inicio

# if nombre1 == nombre2: #si lo tecleó dos veces seguidas igual lo damos como correcto
#     if t1<t2:
#         print(f'Hola {nombre1} te has demorado {t1:.3f} segs en teclear tu nombre')
#         print(f'a una velocidad de {t1/len(nombre1):.3f} caracteres x segundo')
#     else:
#         print(f'Hola {nombre2} te has demorado {t2:.3f} segs en teclear tu nombre')
#         print(f'a una velocidad de {t2/len(nombre2): .3f} caracteres x segundo')
# else: print('Lo siento parece que no has tecleado bien el nombre')
# Este código no da la oportunidad de rectificar si no tecleaste dos veces seguidas la misma cadena
# endregion

#region CODE 1 CICLO PARA REPETIR EL PROCESO MIENTRAS LA CONDICION DEL CICLO SEA TRUE
# import time
# entrada_incorrecta = True
# while entrada_incorrecta:
#     inicio = time.time()  # instante justo antes del input
#     nombre1 = input("Escribe tu nombre --> ")
#     t1 = time.time() - inicio #tiempo transcurrido mientras teclea el nombre
#
#     inicio = time.time()  # instante justo antes del input
#     nombre2 = input("Vuelvelo a teclear --> ")
#     t2 = time.time() - inicio
#     if nombre1 == nombre2: #si lo tecleó dos veces seguidas igual lo damos como correcto
#         if t1<t2:
#             print(f'Hola {nombre1} te has demorado {t1:.3f} segs en teclear tu nombre')
#             print(f'a una velocidad de {t1/len(nombre1):.3f} caracteres x segundo')
#         else:
#             print(f'Hola {nombre2} te has demorado {t2:.3f} segs en teclear tu nombre')
#             print(f'a una velocidad de {t2/len(nombre2): .3f} caracteres x segundo')
#             entrada_incorrecta = False #Para que el próximo while evalúe a false y no se vuelva a repetir
#     else:
#         print('LO SIENTO PARECE QUE NO HAS TECLEADO BIEN EL NOMBRE. Vuélvelos a teclear\n')
#endregion

#region CODE 2 ABORTAR LA EJECUCIÓN DE UN CICLO CON UN BREAK
# import time
# while True:
#     inicio = time.time()  # instante justo antes del input
#     nombre1 = input("Escribe tu nombre --> ")
#     t1 = time.time() - inicio #tiempo transcurrido mientras teclea el nombre
#     inicio = time.time()  # instante justo antes del input
#     nombre2 = input("Vuelvelo a teclear --> ")

#     t2 = time.time() - inicio
#     if nombre1 == nombre2: #si lo tecleó dos veces seguidas igual lo damos como correcto
#         if t1<t2:
#             print(f'Hola {nombre1} te has demorado {t1:.3f} segs en teclear tu nombre')
#             print(f'a una velocidad de {t1/len(nombre1):.3f} caracteres x segundo')
#         else:
#             print(f'Hola {nombre2} te has demorado {t2:.3f} segs en teclear tu nombre')
#             print(f'a una velocidad de {t2/len(nombre2): .3f} caracteres x segundo')
#         break #Abortar la ejecución del ciclo y seguir a continuación
#     else:
#         print('LO SIENTO PARECE QUE NO HAS TECLEADO BIEN EL NOMBRE. Vuélvelos a teclear\n')
#endregion

#region CODE 3 PROCESAR LOS DATOS DE UNA FUENTE QUE CUMPLEN CON UNA CIERTA CONDICIÓN.
#Condición: Contar todas las cadenas que empiezan con "a". Procesar: Escribirla en mayúscula
# print("Vamos a entrar una secuencia de cadenas y terminar con una línea en blanco")
# print("las que empiecen con 'a' las pasaré a mayúsculas y las contaré")
# cuantas = 0 #en un ciclo suelen haber variables que se deben inicializar con un valor antes de empezar el ciclo
# while True:
#     s = input("Entra una cadena (Teclee solo Enter para terminar): ")
#     if len(s) == 0:
#         break
#     elif s[0]=='a': #Procesar las que cumplen con una condición
#         cuantas = cuantas+1
#         print(s.upper())  # Upper pasa a mayúscula
#     else:
#         print(s)
#     # Note Si llega aquí el ciclo se repite
# print(f'El total de cadenas que empiezan con "a" es {cuantas}')
# #Vea cómo hacer esto en una Jupyter Notebook. Cada input abrirá una caja de entrada en Jupyter
#endregion

#region CODE 4 ENTRAR UNA SECUENCIA DE ENTEROS Y HALLAR EL MENOR Y EL MAYOR
# n=int(input("Entra un número --> "))
# min = max = n #asumimos que ese primer entero es el mayor y el menor
# while True:
#     s = input('Entra otro número (Teclea Enter para terminar): --> ')
#     if len(s) == 0: break
#     n = int(s)
#     if n < min: min = n
#     elif n > max: max = n
# print(f'El menor es {min} y el mayor es {max}')
##Retoque este código para completar el caso en que no se de ningún número y se empiece con una línea en blanco
#endregion

#region CODE 5 RANGE. HALLAR LOS ENTEROS DE UN INTERVALO QUE SON CUADRADOS PERFECTOS
# import math
# inicio = int(input("Entra la cota inferior del intervalo: "))
# final = int(input("Entra la cota superior del intervalo: "))
# if inicio > final:
#     print(f'ERROR {inicio} y {final} NO FORMAN UN INTERVALO CORRECTO')
# else:
#     print(f'Los cuadrados perfectos en el intervalo ({inicio},{final}) son:')
#     for k in range(inicio, final + 1): #el valor de k va de inicio hasta final con incremeto 1
#         raiz = int(math.sqrt(k))
#         if raiz*raiz == k:
#             print(f'{k} es cuadrado perfecto su raiz es {raiz}')
#endregion

#region CODE 6 RANGO CON PASO. HALLAR LOS CUADRADOS PERFECTOS DE UN INTERVALO Y QUE SEAN IMPARES
import math
inicio = int(input("Entra la cota inferior del intervalo: "))
final = int(input("Entra la cota superior del intervalo: "))
if inicio <0 or inicio > final:
    print(f'ERROR {inicio} y {final} NO FORMAN UN INTERVALO CORRECTO PARA LO QUE SE SOLICITA')
else:
    if inicio%2 == 0: inicio +=1 #garantizar que inicio comience en el primer impar del intervalo
    print(f'Los cuadrados perfectos e impares en el intervalo ({inicio},{final}) son:')
    for k in range(inicio, final + 1, 2):
        raiz = int(math.sqrt(k))
        if raiz*raiz == k:
            print(f'{k} es impar y cuadrado perfecto, su raiz es {raiz}')
#endregion

#region CODE 7 Code 7 Un string como fuente de datos. Recorrer los caracteres de un string
# cadena = "Bienvenido a Python"
# n=0
# print("Los caracteres de la cadena son")
# for c in cadena:
#     print(c, end='') #end='' indica terminar el print sin cambiar de linea y con una cadena vacía para el próximo print
#     n=n+1
# print(f'\nLa cadena tiene longitud de {n} caracteres')
#
# print()
# print("Recorriendo la cadena con un rango sobre la longitud")
# for i in range(len(cadena)):
#     print(f'En la posición {i} está el carácter {cadena[i]}')
#endregion

#region CLASE PRACTICA
# 1. Escriba un código que lea un número entero y calcule el factorial de ese número. Recuerde que el factorial de un número `n` es el producto de todos los números 1*2*3....*n. Ejemplo factorial de 4 debe escribir 24
# 2. Escriba un código que determine si un número que se da como entrada es un número primo. Recuerde que un número primo es aquel que solo es divisible por 1 y por él mismo. Ejemplo 13 es primo pero 49 no lo es porque es divisible por 7
# 3. Escriba un código que determine si un número es perfecto. Un número es perfecto si es igual a la suma de todos sus divisores sin incluirlo a él. Ejemplo 6 es perfecto porque 6 = 1+2+3 que son sus divisores
# 4. Entre los valores de un intervalo, escriba cuáles números en ese intervalo son primos. Note como aquí usará dos ciclos: uno más externo para recorrer los valores del intervalo
# 5. Escriba un código que a partir de un número que lee como entrada escriba cual es el número primo que le sigue
# 6. **Considere las formas de recorrer los caracteres del ejemplo del Code7. Escriba un código que determine si los caracteres de una cadena forman un palíndromo. Un palídromo es una cadena que se lee de igual forma de izquierda a derecha que de derecha a izquierda. Por ejemplo oso, larutanatural, dabalearrozalazorraelabad, 51AxyxA15, ??? son palíndromos
# 7 **Un código como f = datetime.today() nos da un valor datetime con .weekday() del módulo time nos da un número entero correspondiente al día de la semana en el que estamos. Dado tres enteros que correspondan al día, mes y año escriba qué día de la semana es.
#
# Los ejercicios marcados con ** tienen un mayor grado de dificultad. Los estudiantes que lo implementen y discutan correctamente con el profesor podrán recibir bonificación
#endregion