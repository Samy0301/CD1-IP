#region LISTAS VARIAS
# enteros = [20, 10, 4, 30, -5]
# print(enteros)
# print(type(enteros)) #lo único que dice del tipo es que es list pero no del tipo de los elementos
# print(f'El valor en la posición {3} es {enteros[3]}')
#
# mis_preferidos = ["chocolate", "almendra", "coco"]
# print(f'Soy {mis_preferidos} tengo {len(mis_preferidos)} valores de tipo {type(mis_preferidos[0])}')
#
# mejunje = [100, True, "María", -10.25]
# print(mejunje)
#
# lista_vacia = []
# print(f'Soy lista_vacia {lista_vacia} tengo longitud {len(lista_vacia)}')
#
# pi = 3.14
# lista = [pi*2, enteros[2], len(mis_preferidos)]
# print(lista)
#
# superlista = [100, enteros, 1000]
# print(superlista)
#endregion

#region RECORRER LOS ELEMENTOS DE UNA LISTA
# enteros = [20, 10, 4, 30, -5, 22, -15, 33]
# menor = mayor = enteros[0] #Habría que asegurarse que la lista tiene al menos un elemento
# for k in enteros:
#     if k < menor:
#         menor = k
#     elif k > mayor:
#         mayor = k
# print(f'La lista es {enteros} el menor es {menor} y el mayor es {mayor}')
#
# #Usando la posición
# enteros = [20, 10, 40, 30, -15, 22, 0, 33]
# # enteros = [20, 20, 20] #probar con esta otra variante
# # enteros = [-1] #probar con esta otra variante
# menor = mayor = enteros[0] #Habría que asegurarse que la lista tiene al menos un elemento
# pos_menor = pos_mayor = 0
# for i in range(len(enteros)):
#     if enteros[i] < menor:
#         menor = enteros[i]
#         pos_menor = i
#     elif enteros[i] > mayor:
#         mayor = enteros[i]
#         pos_mayor = i
# print(f'La lista es {enteros} el menor es {menor} está en la posición {pos_menor} y el mayor es {mayor}'
#       f' está en la posición {pos_mayor}')
#endregion

#region CREACION DE UNA LISTA
# enteros = [20, 10, 40, 30, -15, 22, 0, 33]
# enteros = enteros + [555]
# print(enteros)
# enteros.append(111)
# print(enteros)
#
# #Dos formas de crear listas con las cadenas que empiezan con determinada letra
# print()
# nombres = ["Juana", "María", "carlos", "Ana", "Bertha", "ada", "Augusta", "Calixto"]
# print(nombres)
# nombres_con_a = []
# nombres_con_b = []
# for nombre in nombres:
#     if nombre[0] == 'A' or nombre[0] == 'a':
#         nombres_con_a.append(nombre)
#     elif nombre[0] == 'B' or nombre[0] == 'b':
#         nombres_con_b += [nombre]
# print(f'Empiezan con A o a {nombres_con_a}')
# print(f'Empiezan con B o b {nombres_con_b}')
#endregion

#region EXPRESION LISTA. FORMA DIRECTA DE CREAR UNA LISTA
# nombres = ["Juana", "María", "carlos", "Ana", "Bertha", "ada", "Augusta", "Calixto"]
# print(nombres)
# nombres_con_a = []
# nombres_con_b = []
# for nombre in nombres:
#     if nombre[0] == 'A' or nombre[0] == 'a':
#         nombres_con_a.append(nombre)
#     elif nombre[0] == 'B' or nombre[0] == 'b':
#         nombres_con_b += [nombre]
# print(f'Empiezan con A o a {nombres_con_a}')
# print(f'Empiezan con B o b {nombres_con_b}')
# nombres_con_c = [x for x in nombres if x[0] == "C"or x[0] == "c"]
# print(f'Empiezan con C o c {nombres_con_c}')
# nombres_con_d = [x for x in nombres if x[0] == "D"or x[0] == "d"]
# print(f'Empiezan con D o d {nombres_con_d}')
#endregion

#region COMPARAR EL TIEMPO QUE DEMORAN LAS TRES VARIANTES
# import time
# n = 10_000_000
#
# numeros_concat = []
# inicial = time.time()
# for k in range(n):
#     numeros_concat += [k]
# demora = time.time() - inicial
# print(f'con concat para {n} son {demora} segs')
#
# numeros_append = []
# inicial = time.time()
# for k in range(n):
#     numeros_append.append(k)
# demora = time.time() - inicial
# print(f'con apped para  {n} son {demora} segs')
#
# inicial = time.time()
# numeros = [k for k in range(n)]
# demora = time.time() - inicial
# print(f'en directo para {n} son {demora} segs')
#
# print(f'Que las tres listas son iguales es {numeros_concat==numeros_append==numeros}')
#endregion

#region CREACION E INICALIZACION DE UNA LISTA CON VALORES ALEATORIOS
# import random
# n = 10
# m = 100
# enteros = [random.randint(0, m) for _ in range(n)]
# print(f'Una lista de {n} elementos con valores enteros entre 0 y {m} {enteros}')
# #cambiamos valor de m para que haya repetidos
# m = 3
# conrepetidos = [random.randint(0, m) for _ in range(n)]
# print(f'Una lista de {n} elementos con valores enteros entre 0 y {m} {conrepetidos}')
#endregion

#region MUTABILIDAD DE LAS LISTAS
# #Una misma lista y dos copias
# lista = [10, 20, 30]
# otra_lista = lista
# una_copia = [10, 20, 30]
# segunda_copia = [x for x in lista]
# print(lista)
# print(otra_lista)
# print(una_copia)
# print(segunda_copia)
# print(f'lista==otra_lista==una_copia==segunda_copia es {lista==otra_lista==una_copia==segunda_copia}') #el resultado debe ser true porque aunque on realmente tres listas son iguales componente a componente
# print()
#
# # #Probando la mutabilidad de las listas cambiando valores en cierta posición
# lista = [10, 20, 30]
# lista[1] = 22
# otra_lista[2] = 33
# print('Hago un cambio (mutable) en una componente de lista y en una componente de otra_lista (se reflejan en ambos)')
# print(f'lista {lista}')
# print(f'otra_lista {otra_lista}')
# print(f'una_copia {una_copia}')
# print(f'segunda_copia {segunda_copia}')
# print(f'lista==otra_lista es {lista==otra_lista}') #sigue siendo true porque lista y otra_lista son la misma lista
# print(f'lista==una_copia es {lista==una_copia}') #la lista modificada ya no son iguales a una_copia
# print(f'una_copia==segunda_copia es {una_copia==segunda_copia}') #las dos copias siguen siendo iguales entre sí porque lo son componente a componente
# print()
#
# una_copia[0] = 1000
# print('Hago un cambio (mutable) en una componente de una_copia. No debe reflejarse en la otra copia)')
# print(f'lista {lista}')
# print(f'otra_lista {otra_lista}')
# print(f'una_copia {una_copia}')
# print(f'segunda_copia {segunda_copia}')
# print(f'Luego de los cambios una_copia==segunda_copia es {una_copia==segunda_copia}')
# #como una_copia y segunda_copia no eran la misma lista luego de un cambio ya no son necesariamente iguales
# print()
#endregion

#region EJERCICIOS
# 1. Genere una lista con los impares de un intervalo
# 2. Vaya leyendo con input una secuencia de enteros hasta que teclee solo cambio de linea. Cree una lista con todos los valores enteros leídos
# 3. Lea una secuencia de enteros donde el primer valor que se lea es la cantidad de enteros que se escribirá a continuación, escriba el resultado de la suma y del producto de todos ellos
# 4. A partir de una lista de cadenas genere una lista con aquellas cadenas que tengan longitud mayor que un valor N
# 5. A partir de una lista de enteros, que puede tener valores repetidos, genere una lista con los mismos valores pero sin repetidos
#
# 6. *A partir de una lista1 y una lista2 genere una lista comunes que contenga solo los valores que están en ambas listas
# 7. *Si una lista polinomio `p` de longitud `n+1` representa los coeficientes de un polinomio de grado `n `calcule el valor del polinomio para un cierto valor `x`. Es decir que el valor a calcular sería `p[n]*(x**n) + p[n-1]*(x**(n-1)) + ... p[1]*x + p[0]`
# 8. *A partir de una lista de valores enteros genere una lista con los mismos valores pero ordenada de menor a mayor. No use la función sort de Python
#endregion