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
    
