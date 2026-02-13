#region REVIEW TIPO STRING y PRINT
# import math
# a = 3
# b = 4
# c = math.sqrt(a*a + b*b)
#
# print("El cateto", a, "el cateto", b, "la hipotenusa es", c)
# #Los argumentos que no son string se convierten a string.
# print("El cateto " + str(a) + " el cateto " + str(b) + " la hipotenusa es " + str(c))
# #Aquí el argumento es una sola string resultado de la concatenación
# print(f'El cateto {a} el cateto {b} la hipotenusa es {c}')
# #El string f' indica un formato de cadena donde las expresiones entre llaves se evaluan y se concatenan a la cadena
# #Todo valor en Python es convertible a string
#endregion

#region REVIEW INPUT. Lectura(entrada) de string. Expresiones y Variables
# s=input('entra un string que convertiré a float --> ') #el resultado del input lo asignamos a una variable
# print('el tipo de s es',type(s))
# a=float(s) #lo puedo convertir a float si tiene el formato de un float y ASIGNARLO a una VARIABLE
# print('el tipo de a es',type(a))
# print('Como a es es un float le puedo sumar 1.11, a+1.11 es4.3 ', a+1.11)
# b=float(input('entra otro float -->'))
# print(f'a es {a} y b es {b} la suma de los dos es {a+b}')
# #f' indica una formato especial de string en el que las expresiones que aparecen entre llaves {, } se computan y su valor se convierte a tring
#endregion

#region REVIEW TIPO BOOL
# a=int(input("Dame la longitud de un posible lado de un triangulo --> "))
# b=int(input('Dame la longitud de otro posible lado de un triangulo --> '))
# c=int(input('Dame la longitud de un tercer posible lado de un triangulo --> '))
# print(f'Que los valores {a}, {b} y {c} forman un triangulo es {a+b>c and b+c>a and c+a>b}')
#endregion

#region CONDICIONALES IF AVERIGUAR SI TRES ENTEROS PUEDEN SER LOS LADOS DE UN TRIANGULO
# import math
# a=int(input("Dame la longitud de un posible lado --> "))
# b=int(input('Dame la longitud de otro posible lado --> '))
# c=int(input('Dame la longitud de un tercer posible lado --> '))
# if (a+b>c and a+c>b and b+c>a):
#     print(f'Triangulo de lados {a} + {b} y {c}')
#     p = a+b+c
#     print(f'El perímetro es {p}')
#     sp = p/2
#     area = math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
#     print(f'El área es {area}')
# else:
#     print(f'{a}, {b} y {c} NO pueden forman un triangulo !!')
# print("Después de una condicional seguimos ....")
#endregion

#region CONDICIONALES ANIDADAS
# a=int(input("Dame la longitud de posible lado de un triangulo --> "))
# b=int(input('Dame la longitud de otro posible lado --> '))
# c=int(input('Dame la longitud de un tercer posible lado --> '))
# if (a+b>c and a+c>b and b+c>a):
#     print(f"{a}, {b} y {c} Forman un triángulo")
#     if (a==b and b==c):
#         print('Los tres lados son iguales es EQUILATERO')
#     elif (a==b or b==c):
#         print('Dos lados iguales es ISOSCELES')
#     else:
#         print('Los tres lados desiguales es ESCALENO')
#         # print(f'Su perimetro es {a + b + c}') #Pruebe y descomente esta línea y comente la siguiente
#     print(f'Su perimetro es {a+b+c}')
# else:
#     print(f"{a} + {b} y {c} NO FORMAN UN TRIANGULO")
# print("Después de una condicional seguimos ....")
#endregion

#region LA IMPORTANCIA DE LA SANGRÍA (INDENTACION)
# a=int(input("Dame la longitud de un posible lado de un triangulo --> "))
# b=int(input('Dame la longitud de otro posible lado de un triangulo --> '))
# c=int(input('Dame la longitud de un tercer posible lado de un triangulo --> '))
# if (a+b>c and a+c>b and b+c>a): #comodidad de Python para combinar comparaciones los operadores aritméticos tienen priodiad sobre los de comparación
#     print(f"{a} + {b} y {c} Pueden formar un triangulo")
#     print(f'  Su perimetro es {a+b+c}')
#     if (a==b and b==c): print('  El triangulo es equilátero')
#     elif (a==b or b==c or a==c): print('  El triangulo es isosceles')
#     else: print('  El triangulo es escaleno')
#     print("Ya averiguamos que SÍ forman triángulo") #Sangría correcta. Comentar esta linea y descomentar la siguiente para probar un error común
# # print("Ya averiguamos que SÍ forman triángulo") #Sangría incorrecta
# print("Continuamos....")
#endregion

#region EL MAYOR Y EL MENOR DE TRES NÚMEROS
# print("Vamos a entrar tres números enteros para calcular cuál es el menor y cuál es el mayor")
# n1 = int(input("Ingresa un numero: "))
# n2 = int(input("Ingresa segundo numero: "))
# n3 = int(input("Ingresa tercer numero: "))
# mayor = n1
# if n2 > mayor:
#     mayor = n2
# if n3 > mayor:
#     mayor = n3
# menor = n1
# if n2 < menor:
#     menor = n2
# if n3 < menor:
#     menor = n3
# print(f'El mayor de {n1}, {n2} y {n3} es {mayor} y el menor es {menor}')
#endregion

#region MEDIR TU VELOCIDAD DE TECLEO
#Cómo medir el tiempo que demoras en teclear una cadena
# import time
# inicio = time.time()  # instante justo antes del input
# nombre1 = input("Escribe tu nombre --> ")
# t1 = time.time() - inicio #tiempo transcurrido mientras teclea el nombre
#
# inicio = time.time()  # instante justo antes del input
# nombre2 = input("Vuelvelo a teclear --> ")
# t2 = time.time() - inicio
#
# if nombre1 == nombre2: #si lo tecleó dos veces seguidas igual lo damos como correcto
#     if t1<t2:
#         print(f'Hola {nombre1} te has demorado {t1:.3f} segs en teclear tu nombre')
#         print(f'a una velocidad de {t1/len(nombre1):.3f} caracteres x segundo')
#     else:
#         print(f'Hola {nombre2} te has demorado {t2:.3f} segs en teclear tu nombre')
#         print(f'a una velocidad de {t2/len(nombre2): .3f} caracteres x segundo')
# else: print('Lo siento parece que no has tecleado bien el nombre')
#endregion

#region PROBLEMAS PARA CLASE PRACTICA
#1 Leer tres enteros que deben ser el dia, el mes y el año de una fecha. DETERMINAR SI FORMAN UNA FECHA CORRECTA
#  Escribir la fecha en el formato 15/9/2025
#  Escribir la fecha en el formato 15 de septiembre de 2025

#2 Escriba la fecha del día siguiente
#  Si lo enteros fuesen 30, 4 y 2025 debería escribir 1/5/2025

#3 Escriba la fecha del día anterior

#4 Lea cuatro cadenas (string). Escribalas ordenadas alfabéticamente de menor a mayor

#5 Entre cuatro enteros que son el día y el mes de dos fechas de mismo año. Calcule la diferencia de días que hay las dos fechas

#6 Pida la entrada de una cadena que sirva de contraseña. Para ello debe tener 8 caracteres o más y al manos una letra y un dígito
#  Recuerde que se puede referir a un caracter específico de la posición n de una cadena s con la notación s[n] y que los caracteres
#  mantienen el orden entre las letras minusculas, mayúsculas y entre los dígitos
# s = input("Introduce la contraseña: ")
# if len(s) >= 8:
#     # Comprobar letra en los primeros 8 caracteres
#     tiene_letra = (
#         ('a' <= s[0] <= 'z') or ('A' <= s[0] <= 'Z') or
#         ('a' <= s[1] <= 'z') or ('A' <= s[1] <= 'Z') or
#         ('a' <= s[2] <= 'z') or ('A' <= s[2] <= 'Z') or
#         ('a' <= s[3] <= 'z') or ('A' <= s[3] <= 'Z') or
#         ('a' <= s[4] <= 'z') or ('A' <= s[4] <= 'Z') or
#         ('a' <= s[5] <= 'z') or ('A' <= s[5] <= 'Z') or
#         ('a' <= s[6] <= 'z') or ('A' <= s[6] <= 'Z') or
#         ('a' <= s[7] <= 'z') or ('A' <= s[7] <= 'Z')
#     )
#     # Comprobar dígito en los primeros 8 caracteres
#     tiene_digito = (
#         ('0' <= s[0] <= '9') or ('0' <= s[1] <= '9') or
#         ('0' <= s[2] <= '9') or ('0' <= s[3] <= '9') or
#         ('0' <= s[4] <= '9') or ('0' <= s[5] <= '9') or
#         ('0' <= s[6] <= '9') or ('0' <= s[7] <= '9')
#     )
#
#     if tiene_letra:
#         if tiene_digito:
#             print("La contraseña es válida.")
#         else:
#             print("La contraseña debe tener al menos un dígito.")
#     else:
#         print("La contraseña debe tener al menos una letra.")
# else:
#     print("La contraseña debe tener al menos 8 caracteres.")
#endregion