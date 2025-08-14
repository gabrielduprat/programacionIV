def contar_palabras(texto:str)->int:
    return len(texto.split())

def invertir(texto:str)->str:
    return texto[::-1]

#palabras que cominezan con una letra dada
def palabras_comienza_con(texto:str,letra:str)->list:
    return [palabra for palabra in texto.split() if palabra.startswith(letra)]

# contar palabras que se repiten
def contar_palabras_repetidas(texto:str)->dict:
    return {palabra:texto.count(palabra) for palabra in texto.split()} # explicacion de la funcion
#que hace palabra:numero de veces que aparece

def contar_repetidas_basico(texto: str) -> list[tuple[str, int]]:
    palabras = texto.lower().split()
    resultado = []
    usadas = []
    for palabra in palabras:
        if palabra not in usadas:
            usadas.append(palabra)
            contador = 0
            for p in palabras:
                if p == palabra:
                    contador += 1
            resultado.append((palabra, contador))
    
    return resultado
