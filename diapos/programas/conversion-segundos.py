def convertir_segundos(segundos):
    horas = segundos / (60 * 60)
    minutos = (segundos / 60) % 60
    segundos = segundos % 60
    return horas, minutos, segundos
