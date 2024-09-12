n = 3  # Definimos cuántos caracteres queremos
primeros_n = cadena[:n]  # "Mat" (Toma los primeros 3 caracteres)

# Para cadenas con longitud par e impar
medio = len(cadena) // 2  # Índice del medio de la cadena

# Si la longitud es par, obtenemos dos caracteres centrales
if len(cadena) % 2 == 0:
    caracteres_medio = cadena[medio-1:medio+1]  # "te" (Caracteres del medio si la longitud es par)
else:
    # Si la longitud es impar, obtenemos solo un carácter del medio
    caracteres_medio = cadena[medio]


ultimos_n = cadena[-n:]  # "lsa" (Obtiene los últimos 3 caracteres de la cadena)
