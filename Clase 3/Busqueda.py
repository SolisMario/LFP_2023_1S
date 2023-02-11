# busqueda lineal
def busqueda_lineal(arr, n, elemento):
    # iterar el arreglo
    for i in range(n):
        # revisar que el elemento en la posicion i sea el buscado
        if arr[i] == elemento:
            print('Valor encontrado en la posicion', i)
            return True
    # elemento no encontrado
    return False

arreglo = [4,6,7,3,10,5,0,1]
busqueda_lineal(arreglo, 8, 5) # encontrado
print(busqueda_lineal(arreglo, 8, 23)) # no encontrado

def busqueda_binaria(arr, n, elemento):
    # indice para iterar
    i = 0

    # inicio y fin de la seccion en la que se busca
    start = 0
    end = n - 1

    # iteramos sobre el arreglo
    while i < n:
        # encontrar indice posicion del medio
        middle = (start + end) // 2

        # comprobar si la posicion del medio tienen el elemento
        if arr[middle] == elemento:
            return True
        elif arr[middle] < elemento:
            # eliminar la parte de la izquierda
            start = middle + 1
        else:
            # eliminar la parte de la derecha
            end = middle - 1
        
        i += 1
    
    return False

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
element_to_be_searched = 9
print(busqueda_binaria(arr, n, element_to_be_searched))