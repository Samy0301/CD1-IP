#RECORRIDO POR LOS TIPOS BÁSICOS O BUILT-IN DE PYTHON

#region El tipo STRING
#un string o cadena es una secuencia de carateres de cualquier longitud encerrada entre comillas simples o dobles
#es el argumento principal de la función print que escribe la cadena en la consola o ventana de salida
# print('Bienvenido a Python')
# print("Espero que te diviertas")
# print('Los puedo poner en una misma linea', 'Bienvenido a Python', "Espero que te diviertas")
# print("tar...."*4 + "mudeo") #string*n repite el string n veces, + concatena dos strings
#Hay muchas operaciones con string que iremos viendo durante el curso, ver tabla en los slides
#endregion

#region Los tipos numéricos INT y FLOAT
# print(2025) #INT (enteros) se escriben con la secuencia de dígitos sin punto decimal
# print(3.141516) #FLOAT (reales) se escriben con parte fraccionario, punto decimal
# print(-999)
# print("El valor de PI es", 3.141592) #se pueden combinar string y numéricos en un mismo print
#endregion

#region EXPRESIONES
# #Sobre los numéricos se pueden aplicar todas las operaciones aritméticas con los símbolos conocidos
# import math #importar módulo biblioteca de operaciones aritméticas en este ejemplo para usar sqrt
# print("La hipotenusa del triangulo con catetos 4 y 3 es", math.sqrt(4**2+3**2))
# #la operacion ** tiene prioridad sobre las operaciones * y /
# #que a su vez tienen prioridad sobre las operaciones + y -
# print(4+2*3+2)
# print((4+2)*(3+2)) #se pueden usar paréntesis para indicar la prioridad
# print(4+(2*3)+2) #No escatime el uso de paréntesis si con eso su código puede verse más claro
# print(4/3, 4/2) #La división de enteros da un número fraccionario float
# print(13/3, 13//3, 4//2) #El operador // da el cociente entero de la división
# print(11%3, 4%2) #El operador % da el resto de la división
# print(10**57, "(** es el operado potencia. 10 elevado a la 57, es el estimado de átomos en el sistema solar") #los n'meros pueden ser de cualquier tamaño
# print(int("100")+99) #se puede convertir un string a un entero con la operación int
# print(str(10)+"99") #se puede convertir un entero a string con str. La operacion + sobre string concatena los dos string
# print("La longitud de Hola Python es", len("Hola Python")) #len da la longitud de la cadena
#endregion

#region El tipo BOOL
# print(100>3) #True los simbolos >, <, >=, <=, == se usan para comparar con el criterio de orden
# print(-2<=5) #True
# print(4>2>3) #False
# print(100<200==200) #True
# print("abc"=="ABC") #False Python es sensitivo a las mayúsculas y minúsculas
# print("miguel" < "manual") #las cadenas se comparan segun el codigo de los caracteres
# print("MKM" < "MKM*")
# print("abc"<"abc$" and 100<200) #el operando and da True solo si los dos operandos son True
# print(1>0 and -1>1) #si uno de los operando es False el resultado del and es False
# print(0<1 or -1>1) #el operando or da True si cualquiera de los dos operandos es True
# print(True or False and False ) #el operador and tiene prioridad sobre or
# print(False or True and False ) #el operador and tiene prioridad sobre or
#endregion

#region VARIABLES y ASIGNACION
import math

# cateto1 = 3
# # #una variable es nombre formado por letras y dígitos que se pone a la izquierda de una operacion = (asignación)
# # ## a la que se le puede asignar (guardar en memoria) el valor resultante de computar la expresión de la parte derecha
# cateto2 = 4
# hipotenusa = math.sqrt((cateto1**2) + (cateto2**2)) #cuando la variable se usa en parte derecha se esta usando  el valor en ella "guardado"
#
# a = 100
# b = a
# print(f' a es {a} b es {b}') #f' es un tipo de formato que hace que se evaluen las expresiones que están entre llaves { } y se conviertan a string
# a += 100 #sumo 100 al valor que está en b
# b = b + 200 #sumo 200 al valor que está en a
# print(f' a es {a} b es {b}')
# print(f' a+100 es {a+100} pero a es {a}') #la expresión a+100 se computa pero no cambia el valor de a
#
# a = "Ahora el valor de a soy yo, una cadena"
# print(f' a es {a}')
#
# x=y=z=1000 #Asignando un mismo valor a tres variables
# print(f'Los valores de x y z son iguales es {x==y and y==z}')
# y="ABC"
# print(f'Los valores de x y z son iguales es {x==y and y==z}')

#endregion

#region HACIENDO LOS PROGRAMAS MÁS FLEXIBLES. ENTRADA DE DATOS POR CONSOLE
# s = input("Bienvenido a Python. Entra tu nombre --> ") #lo que se teclea es leido como string hasta que se teclea cambio de linea
# print (f'Hola {s}')
# print (f'Tu nombre tiene una longitud de {len(s)} caracteres')

print('Escribe tres números para sumarlos')
a = int(input("primer numero --> "))
b = int(input("segundo numero --> "))
c = int(input("tercer numero --> "))
print(f'la suma de {a} , {b} y {c} es {a+b+c}')

# #Si la cadena de entrada no corresponde con el formato de un número la operación int dará excepción
# #más adelante veremos cómo tratar esta situación
#endregion

#region EL MODULO TIME
#Cómo medir el tiempo que demoras en teclear una cadena
# import time
# inicio = time.time()  # instante justo antes del input
# nombre = input("Escribe tu nombre --> ")
# fin = time.time()    # instante justo después del input
# duracion = fin - inicio
# print(f"Te has demorado {duracion} segundos en teclear tu nombre.")
# print(f"Te has demorado {duracion:.3f} segundos en teclear tu nombre.") #redondea a 3 digitos después del punto
#
# #Calcular la velocidad de teclear
# print(f'Estas tecleando a una velocidad de {duracion/len(nombre):2.4f} caracteres x seg.')
#endregion

#region PREGUNTAS CON EJERCICIOS PARA HACER
#Escriba un código que ilustre todas las operaciones aritméticas
#Escriba un código que ilustre todas las operaciones de comparación
#Escriba un código que ilustre todas las operaciones lógicas
#Escriba un código que lea tres números longitudes de segmentos y determine si pueden formar un triángulo
#Amplie el código anterior para que escriba el perímetro del triángulo
#Teclee los coeficientes de un polinomio a_x**2+b__x+c  y calcule el valor del polinomio para un cierto valor de x
#¿Qué se le ocurre hacer para saber si ha tecleado bien el nombre?
#Explore y pruebe distintas funciones de los módulos time y math
#endregion