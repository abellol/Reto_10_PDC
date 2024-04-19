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

```math
media(x) = \dfrac{\sum_{i=1}^{n} x_i}{n}
```
```python
# Se generan 4 listas de numeros enteros para ingresarlo a la función y probarlo
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
