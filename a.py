tempo = int(input())
segundos = 0
minutos = 0
horas = 0
while tempo >= 60:
    while tempo >= 3600:
        horas += 1
        tempo -= 3600
    minutos += 1
    tempo -= 60

segundos = tempo
print("{}:{}:{}".format(horas, minutos, segundos))
