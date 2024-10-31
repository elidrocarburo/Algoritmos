print ("-" *20)
print(" Algoritmo de WARSHALL")
print ("-" *20)

ver=int(input("numero de vertices del grafo: "))
print("-"*30)
data= []

for i in range(ver):
    print(f"......fila {i+1}.....")
    data.append([])
    for e in range (ver):
        valor=int(input(f"ingresa los valores del grafo {e+1}:"))
        data[i].append(valor)

for k in range(ver):
    for i in range (ver):
        for j in range(ver):
            data[i][j] = data[i][j] or (data[i][k] and data[k][j])

print("-" *30)
print("....cierre transitivo.... ")

for i in data: print(i)
