n=int(input())
digitado=[]
pf=[]
acerto1=0
acerto2=0
acerto3=0
certos=[
    ("o","n","e"),
    ("t","w","o"),
    ("t","h","r","e","e"),
]
for i in range(n):
    digitado.insert(i, input())
for i in range(len(digitado)):
    splitado=digitado[i]
    for j in range(len(digitado)-1):
        if len(splitado)==3:
            if(splitado[j]==certos[0][j]):
                acerto1+=1
            elif(splitado[j]==certos[1][j]):
                acerto2+=1
        elif len(splitado)==5:
            if(splitado[j]==certos[2][j]):
                acerto3+=1
        if(acerto1>=2):
            pf.insert(i,'1')
            acerto1=0
        elif(acerto2>=2):
            pf.insert(i,'2')
            acerto2=0
        elif(acerto3>=2):
            pf.insert(i,'3')
            acerto3=0
    print("{}".format(pf[i]))