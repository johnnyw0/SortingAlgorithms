import random
import timeit

def selection_sort(vetor):
    for i in range(len(vetor)):                             #selection sort
        pos = i
        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[pos]:
                pos = j
        vetor[i], vetor[pos] = vetor[pos], vetor[i]
    return vetor
   
def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        valor = vetor[i]
        while vetor[i-1] > valor and i > 0:                #insertion sort
            vetor[i] = vetor[i-1]
            i -= 1
        vetor[i] = valor
    return vetor

def bubble_sort(vetor):
    for i in range(len(vetor)-1):
        mudou = False
        for j in range(len(vetor)-i-1):                    #bubble sort
            if vetor[j] > vetor[j+1]:
                aux = vetor[j+1]
                vetor[j+1] = vetor[j]
                vetor[j] = aux
                mudou = True 
        if not mudou: break
    return vetor

vet50 = [random.randint(1, 5000) for i in range(50)]                        #definição de vetores para testar os métodos de ordenação
vet500 = [random.randint(1, 5000) for i in range(500)]
vet5000 = [random.randint(1, 5000) for i in range(5000)]

ord50 = list(range(1, 51))
ord500 = list(range(1, 501))
ord5000 = list(range(1, 5001))

inv50 = list(range(50, 0, -1))
inv500 = list(range(500, 0, -1))
inv5000 = list(range(5000, 0, -1))

iguais50 = [1]*50
iguais500 = [1]*500
iguais5000 = [1]*5000

def compare_functions(vetor):                                   #função para ordenar os vetores e comparar os resultados
    import timeit

    setup_code1 = f"""
from __main__ import selection_sort
from __main__ import {vetor}
"""
    setup_code2 = f"""
from __main__ import insertion_sort
from __main__ import {vetor}
"""
    setup_code3 = f"""
from __main__ import bubble_sort
from __main__ import {vetor}
"""
    stmt_code1 = f"selection_sort({vetor}[:])"
    stmt_code2 = f"insertion_sort({vetor}[:])"
    stmt_code3 = f"bubble_sort({vetor}[:])"


    times1 = timeit.timeit(stmt=stmt_code1, setup=setup_code1, number=100)
    times2 = timeit.timeit(stmt=stmt_code2, setup=setup_code2, number=100)
    times3 = timeit.timeit(stmt=stmt_code3, setup=setup_code3, number=100)

    print(f"Vetor: {vetor}")
    print(f"Ordenação por seleção: {times1}")
    print(f"Ordenação por inserção: {times2}")
    print(f"Ordenação por bolha: {times3}")

compare_functions("vet50")
compare_functions("vet500")
compare_functions("vet5000")

compare_functions("ord50")
compare_functions("ord500")
compare_functions("ord5000")

compare_functions("inv50")
compare_functions("inv500")
compare_functions("inv5000")

compare_functions("iguais50")
compare_functions("iguais500")
compare_functions("iguais5000")