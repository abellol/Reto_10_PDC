# Reto 10: Listas 
### Soy Alejandro Bello y pertenezco al grupo de "Fenomenoides", adjunto nuestro logo: 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>
y a continuación observará la solucion a los retos planteados referente al tema de Listas en Python, una aclaración es que para cada reto se crearon listas predeterminadas para ver como se comporta el código si recibe diferentes tipos de datos dentro de las listas.

## 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
Para el desarrollo de este ejercicio, se define una función que usa bucles `for` para recorrer los elementos de cada lista y poder sumarlos todos y se usa el método `len` para poder tener exactamente la longitud de cada lista; siendo esto vital para calcular el promedio. 


$$media(x) = \sum_{i=1}^{n}x_i\frac{1}{n}$$

```python
# Se generan 4 listas de numeros reales para ingresarlo a la función y probarla
arreglo_1 = [0.4, 2.5, 4.8, 6, 8.3, 10, 12, 14]
arreglo_2 = [1, 3, 5, 7, 9, 11, 13]
arreglo_3 = [3.8, 6.2, 9, 12, 15]
arreglo_4 = [1, 2.6, 3, 4, 3.4, 5]

"""
Dentro de la función "promedio_reales" se reciben listas, asigna como denominador a la cantidad de datos
y como numerador a la suma de todos los elementos en la lista, retorna como resultado el valor de ese cociente.
"""
def promedio_reales(list) -> float: # ingresa una lista y retorna un valor real
    # Se declara la variable suma, que inicia en 0 y guardará cada valor que se suma
    suma :float = 0 
    # Se declara la variable denominador, que será el total de datos en la lista (el denominador en el promedio)
    denominador = len(list)
    # para cada elemento en la lista se suma con el anterior (inició en 0)
    for i in list:
        suma += i
    prom = suma / denominador
    # retorna el promedio calculado con la función, dentro de un string que lo hace más claro
    return print(f"El promedio de la lista: {list}, es de: {prom}") 

if __name__ == "__main__":
    promedio_1 = promedio_reales(arreglo_1) # imprime -> El promedio de la lista: [0.4, 2.5, 4.8, 6, 8.3, 10, 12, 14], es de: 7.25
    promedio_2 = promedio_reales(arreglo_2) # imprime -> El promedio de la lista: [1, 3, 5, 7, 9, 11, 13], es de: 7.0
    promedio_3 = promedio_reales(arreglo_3) # imprime -> El promedio de la lista: [3.8, 6.2, 9, 12, 15], es de: 9.2
    promedio_4 = promedio_reales(arreglo_4) # imprime -> El promedio de la lista: [1, 2.6, 3, 4, 3.4, 5], es de: 3.1666666666666665
```
## 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
En este ejercicio se utilizó el metodo `len` para obtener la cantidad de elementos dentro de la lista, permitiendo calcular el producto punto, que es la multiplicación de dos matrices (en este caso del mismo tamaño), donde se multiplican los primeros terminos, se suman con el producto de los segundos y etc...
```python
# Se generan 4 listas de numeros reales para ingresarlo a la función y probarla, todas tienen 4 elementos
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
```
## 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
Para el desarrollo de este algoritmo se utiliza el metodo `count` para obtener la cantidad total de ceros, por otro lado con un bucle `while` se controla que con los metodos `remove` y `append` se remuevan y agreguen al final la misma cantidad de ceros.
```python
# se generan 4 listas para ingresalas a la función y probarla
arreglo_1 = [1, 2, 0, 3, 4, 5]
arreglo_2 = [0, 2.5, 0, 4, 0.1, 6.0, 0]
arreglo_3 = ["agua", "no", "hay", "en", "bogota"]
arreglo_4 = [1, 0, "pez", 3, 4, 0]

"""
Dentro de la función "ceros_final", se recibe una lista, se hace un conteo de cuantos
ceros hay dentro de ella; luego se eliminan y se añade la misma cantidad al final
"""
def ceros_final (list) -> list: # se define la funcion que recibe y entrega una lista
    # en primer lugar se imprime la lista ingresada 
    print(f"la lista inicial es {list}") 
    # se declaran e inicializan dos variables iteradoras
    i : float = 1 # para eliminar los ceros
    u : float = 1 # para agregar los ceros 
    # dentro de una variable se guarda el valor de ceros contados en el arreglo
    n = list.count(0)
    # con un bucle se controla que se remueva y agregue la misma cantidad de ceros contada
    while i and u <= n: 
        list.remove(0)
        i +=1
        list.append(0)
        u +=1
    # al final retorna la lista ya ordenada con todos los ceros al final; y la cantidad total de estos
    return print(f"en la lista ya ordenada {list} hay {n} ceros al final \n")

if __name__ == "__main__":
    lista_1 = ceros_final(arreglo_1) 
    """
    imprime -> la lista inicial es [1, 2, 0, 3, 4, 5]
               en la lista ya ordenada [1, 2, 3, 4, 5, 0] hay 1 ceros al final 

    """
    lista_2 = ceros_final(arreglo_2) 
    """
    imprime -> la lista inicial es [0, 2.5, 0, 4, 0.1, 6.0, 0]
               en la lista ya ordenada [2.5, 4, 0.1, 6.0, 0, 0, 0] hay 3 ceros al final

    """
    lista_3 = ceros_final(arreglo_3) 
   
    """
    imprime -> la lista inicial es ['agua', 'no', 'hay', 'en', 'bogota']
               en la lista ya ordenada ['agua', 'no', 'hay', 'en', 'bogota'] hay 0 ceros al final
    """
    
    lista_3 = ceros_final(arreglo_4) 
    """
    imprime -> la lista inicial es [1, 0, 'pez', 3, 4, 0]
               en la lista ya ordenada [1, 'pez', 3, 4, 0, 0] hay 2 ceros al final
    """
```
