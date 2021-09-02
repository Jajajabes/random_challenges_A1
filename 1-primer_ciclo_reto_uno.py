numero_de_manzanas = int(input())
numero_de_limones = 2*numero_de_manzanas+4
numero_de_duraznos = (numero_de_limones+numero_de_manzanas)//5
print (numero_de_manzanas, numero_de_limones, numero_de_duraznos)
if numero_de_duraznos > 0 and 20 >= numero_de_duraznos:
    print("uno")
elif numero_de_duraznos >= 21 and 31 > numero_de_duraznos:
    print("dos")
elif numero_de_duraznos >= 31 and 50 >= numero_de_duraznos:
    print("tres")
elif numero_de_duraznos > 50:
    print("cuatro")