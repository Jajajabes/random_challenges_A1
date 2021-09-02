letras_deFelipe = (input())
letras_deJuana = (input())
letras_deMariana = (input())

PuntajeFe = 0
PuntajeJu = 0
cadena_final = ""


for pasatiempo in letras_deMariana:
    if pasatiempo in letras_deFelipe and pasatiempo in letras_deJuana:
        PuntajeFe += 1
        PuntajeJu += 1
        if PuntajeFe > PuntajeJu:
            cadena_final += "F"
        elif PuntajeJu > PuntajeFe:
            cadena_final += "J"
        else:
            cadena_final += "E" 
    elif pasatiempo in letras_deFelipe:
        PuntajeFe += 1
        if PuntajeFe > PuntajeJu:
            cadena_final += "F"
        elif PuntajeJu > PuntajeFe:
            cadena_final += "J"
        else:
            cadena_final += "E"
    elif pasatiempo in letras_deJuana:
        PuntajeJu += 1
        if PuntajeFe > PuntajeJu:
            cadena_final += "F"
        elif PuntajeJu > PuntajeFe:
            cadena_final += "J"
        else:
            cadena_final += "E"
    else:
        if PuntajeFe > PuntajeJu:
            cadena_final += "F"
        elif PuntajeJu > PuntajeFe:
            cadena_final += "J"
        else:
            cadena_final += "E"
print(cadena_final)