def ordenar(lista):
    tamanhos = []
    for i in range(len(lista)):
        tamanhos.insert(i, len(lista[i]))
    print(tamanhos)

    for i in range(len(tamanhos)):
        for j in range(len(tamanhos) - i):
            # if tamanhos[i]
            pass 

n = int(input())
casos = []
for i in range(n):
    casos.insert(i, str(input()))

for caso in casos:
    print(caso)
    palavras = caso.split(" ")
    ordenar(palavras)
#     incompleto
