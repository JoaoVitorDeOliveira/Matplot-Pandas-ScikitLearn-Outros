import pandas as pd 

f = open('salarios.csv', 'r')
dados = f.read()

#Dividiu as informações pelo enter
linhas = dados.split('\n')
full_data = []

for cadaLinha in linhas:
    #Dividiu as informações divididas por virgulas
    dividiLinhas = cadaLinha.split(",")
    full_data.append(dividiLinhas)

count = 0
for row in full_data:
    count += 1

print(full_data)
print(count)
