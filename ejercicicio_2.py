# Se generan 4 listas de numeros reales para ingresarlo a la función y probarlo, todos tienen 4 elementos
arreglo_1 = [1, 2.3, 3, 4]
arreglo_2 = [3, 6, 9, 12]
arreglo_3 = [2, 4.2, 6.5, 8]
arreglo_4 = [2, 4, 6, 8, 1] # este no tiene 4 para comprobar que si son diferentes, señalará el error
"""
dentro de la función "dot_product" se reciben dos listas, se calcula el producto de
los primeros terminos de cada una, y se suma con el producto de los segundos, así hasta
haberlo hecho con todos los terminos de las listas de igual tamaño,
"""
def dot_product(list_1, list_2) -> float: # ingresa una lista y retorna un valor real
    # se obtiene la cantidad de caracteres que tiene cada lista y se asigna a una variable
    x = len(list_1)
    y = len(list_2)
    n = x
    # se declara la variable suma, inicia en 0 y guardará el valor de la suma de productos
    suma : float = 0
    # se evalúa que la longitud de ambas listas sea igual, y se definen los casos
    if x != y: # si son diferentes, imprimirá que son arreglos de diferente tamaño y no calculará nada
        return print(f"Son arreglos de diferente tamaño, uno tiene {x} elementos y el otro {y} \n")
    else: 
        # si son iguales, accederá a cada numero de cada lista y los multiplicará, retornando el resultado del dot product
        for i in range(0, n, 1): #accede del primer elemento [0] al último [n-1]
            # la variable termino almacena el producto de los i números de la matriz
            termino = list_1[i] * list_2 [i] 
            # se actualiza la variable suma con el valor anterior o inicial, sumado con el nuevo termino
            suma += termino
        return print(f"el producto punto entre el arreglo {list_1} y {list_2} es de: {suma} \n")

if __name__ == "__main__":
    dp_1 = dot_product(arreglo_1, arreglo_2) # imprimirá -> el producto punto entre el arreglo [1, 2.3, 3, 4] y [3, 6, 9, 12] es de: 91.8
    dp_2 = dot_product(arreglo_1, arreglo_3) # imprimirá -> el producto punto entre el arreglo [1, 2.3, 3, 4] y [2, 4.2, 6.5, 8] es de: 63.16
    dp_3 = dot_product(arreglo_2, arreglo_3) # imprimirá -> el producto punto entre el arreglo [3, 6, 9, 12] y [2, 4.2, 6.5, 8] es de: 185.7
    dp_4 = dot_product(arreglo_3, arreglo_4) # imprimirá -> Son arreglos de diferente tamaño, uno tiene 4 elementos y el otro 5