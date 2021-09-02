lista_llamadas = input("ingrese lista: ").split(" ")
lista_llamadas.append("")
anterior, M = "",0
LIST_MH, LIST_VARMH = [],[]
for i in range (len(lista_llamadas)):
    var = lista_llamadas[i]
    if var != anterior:
        LIST_VARMH.append(str(M))
        LIST_MH.append(var)
        M = 1
    else: M += 1
    anterior = var
LIST_VARMH.pop(0)
LIST_MH.pop()
print(" ".join(LIST_MH) + "\n" + " ".join(LIST_VARMH))