n = int(input())
linguas = []
traducoes = []

for i in range(n):
    linguas.insert(i, str(input()))
    traducoes.insert(i, str(input()))

# for i in range(len(linguas)):
#     print("lingua: {}\ntradução: {}".format(linguas[i], traducoes[i]))

m = int(input())
criancas = []
idioma = []
for i in range(m):
    criancas.insert(i, str(input()))
    idioma.insert(i, str(input()))

for i in range(len(criancas)):
    print(criancas[i])
    for j in range(len(linguas)):
        if(linguas[j] == idioma[i]):
            print(traducoes[linguas.index(linguas[j])])
            print()