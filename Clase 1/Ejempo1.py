# # Listas
# # Copiar una lista
# # Forma incorrecta - copiando referenia
# list1 = [0,1,2,3,4,5]
# list2 = list1

# list1[2] = 22
# print(list2)

# # Forma correcta - copiando el valor con slice [:]
# list1 = [0,1,2,3,4,5]
# list2 = list1[:]

# list1[2] = 22
# print(list1)
# print(list2)

# # Forma correcta - copiando el valor con copy()
# list1 = [0,1,2,3,4,5]
# list2 = list1.copy()

# list1[2] = 22
# print(list1)
# print(list2)

# Archivos
# Apertura de archivo
archivo = open('archivo.txt')
# Leer linea
line = archivo.readline()
print('Linea 1', line)
line = archivo.readline()
print('Linea 2', line)
# Cerrar archivo
archivo.close()

# Lectura completa
archivo = open('archivo.txt')
txt = archivo.read()
print('--------- Contenido Completo ----------')
print(txt)
archivo.close()

# Lectura con ciclos de iteracion
#ciclo while
archivo = open('archivo.txt')
line = '$'
print('---Con ciclo while---')
while line != '':
    line = archivo.readline()
    print(line)
archivo.close()