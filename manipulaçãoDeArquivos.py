arq1 = open("arquivo-dsc.txt", "r")
print(arq1.read())
print(arq1.tell())
quantLetras = arq1.tell()


if quantLetras > 10:
    print("Esse arquivo é grande")
else:
    print("Esse arquivo é pequeno")


arq2 = open("arquivo-dsc.txt", "a")
arq2.write(" e uma menor ainda")
#arq2.close()

arq2 = open("arquivo-dsc.txt", "r")
print(arq2.read())
