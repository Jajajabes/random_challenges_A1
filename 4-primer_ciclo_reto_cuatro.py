import json

entrada_inventario = input()
entrada_inventario = json.loads(entrada_inventario)
entrada_requerido_sin_convertir = input() 
entrada_requerido = entrada_requerido_sin_convertir.split(" ")
llaves_inventario = entrada_inventario.keys()
comparacion_existencia_llaves = set(entrada_requerido) & set(llaves_inventario)
lista_con_valores_encontrados = []


        
for i in llaves_inventario:
    for ii in entrada_requerido:
        if ii == i:
            llave_encontrada = ii
            llave_encontrada_valor = entrada_inventario[llave_encontrada]
            lista_con_valores_encontrados.append(llave_encontrada_valor)
def funcion_sumar_valores_encontrados(x):
    laSuma = 0
    for i in x:
        laSuma = laSuma + i
    return laSuma

funcion_sumar_valores_encontrados(lista_con_valores_encontrados)
print(funcion_sumar_valores_encontrados(lista_con_valores_encontrados))

for i in entrada_requerido:
    if i in comparacion_existencia_llaves:
        print(i, end=" ")