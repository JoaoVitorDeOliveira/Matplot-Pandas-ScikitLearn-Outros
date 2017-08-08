fileName = input("Digite o nome do arquivo: ")
fileName = fileName + ".txt"

arq = open(fileName, "w")
arq.write("Essa eh a frase nova do arquivo.")
arq = open(fileName, "r")
print(arq.read())
