from Node import *
from plots import *
import random
import timeit

#Stale
limit = 30000
list_limit = 10000

#Wygenerowanie losowej listy
lista = []
lista = [random.randint(0, limit) for i in range(list_limit)]

n_wyrazy = []
czas_insert = []
czas_find = []
czas_delete = []

n = 1000

#Wykorzystalem funkcje z modułu timeit zamiast z time (proccess_time), poniewaz process time dziwnie (sprawdzane na colabie dzialalo okej) 
# mial tylko dokladnosc 0.015625s i wykresy wygladaly bez sensu

while n <= list_limit:
    n_wyrazy.append(n)

    ##Zadanie wstawiania

    #Tworzenie drzewa
    start = timeit.default_timer()
    
    #Pierwszy element listy bedzie korzeniem drzewa
    Tree = Node(lista[0])
    for i in range(n - 1):
        Tree.insert(lista[i + 1])

    stop = timeit.default_timer()

    time = round(stop - start, 4)

    #Czas tworzenia drzewa binarnego
    print("Dla", n, "wyrazow, czas tworzenia drzewa wynosi:", time, "s")

    czas_insert.append(time)


    ##Zadanie wyszukiwania

    #Start timera
    start = timeit.default_timer()

    #Wyszukiwanie kazdego elementu do n elementu w liscie
    for item in lista[:n]:
        Tree.find_val(item)

    #Stop timera
    stop = timeit.default_timer()

    time = round(stop - start, 4)

    #Czas tworzenia wyszukiwania w drzewie
    print("Dla", n, "pierwszych wyszukiwanych wyrazow, czas wynosi:", time, "s")

    czas_find.append(time)


    ##Zadanie usuwania
    
    #Start timera
    start = timeit.default_timer()

    #Usuwanie kazdego elementu do n elementu w liscie
    for item in lista[:n]:
        deleteNode(Tree, item)

    #Stop timera
    stop = timeit.default_timer()

    time = round(stop - start, 4)

    #Czas tworzenia wyszukiwania w drzewie
    print("Dla", n, "pierwszych usuwanych wyrazow, czas wynosi:", time, "s")

    czas_delete.append(time)


    n += 1000

bar_PLOTSGIT(n_wyrazy, czas_insert, "Zależnośc czasu wstawiania elementów do drzewa", "Czas [s]", "Ilosc elementow [n]")
bar_PLOTSGIT(n_wyrazy, czas_find, "Zależnośc czasu wyszukiwania n elementów w drzewie", "Czas [s]", "Ilosc elementow [n]")
bar_PLOTSGIT(n_wyrazy, czas_delete, "Zależnośc czasu usuwania n elementów w drzewie", "Czas [s]", "Ilosc elementow [n]")