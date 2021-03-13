num_primo=int(input('Ingresa un número: '))
criba=list(range(2,num_primo+1))
print(criba)
contador=2

for i in criba:
    for j in criba:
        if j%i==0:
            #Se quita el número de la lista
            pass
        else:   
            pass
        contador+=1

