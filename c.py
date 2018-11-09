leds = [
    6,
    2,
    5,
    5,
    4,
    5,
    6,
    3,
    7,
    6    
]
entradas = []
n = int(input())
if  1 <= n or n <= 1000 :
    for i in range(n):
        entradas.insert(len(entradas), str(input()))
n_leds = 0

for i in range(len(entradas)):
    n_leds = 0
    numero = entradas[i]
    for j in range(len(numero)):        
        n_leds += int(leds[int(numero[j])])
    print("{} leds".format(n_leds))
    
