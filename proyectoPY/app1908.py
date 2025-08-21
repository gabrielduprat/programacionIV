# crear los siguientes diccionarios de compreension
# numeros del 1 al 10 como clave y hacer el calculo de su cuadrado como valor
# numeros pares del 1 al 20 y su cubo como valor

numeros = {x: x**2 for x in range(11)}  # crear diccionario
numeros_par = {x: x**3 for x in range(21) if x % 2 == 0}  # crear diccionario

print(numeros)
print(numeros_par)

# crear diccionario de comprension de alumnos con notas y agruparlos por alumno
grupo_alumnos={}
entrada = [('gabri', 9), ('hipo', 5), ('gabri', 8)]
alumnos = set(alumno for alumno, _ in entrada)
print(alumnos)
for a in alumnos:
    grupo_alumnos[a] = {nota for nombre, nota in entrada if nombre == a}
print(grupo_alumnos)

#calcular el promedio de notas por alumno
promedio = {alumno: sum(notas)/len(notas) for alumno, notas in grupo_alumnos.items()}
print(promedio)

entrada = [
    ('gabri', {'parcial': 9}, {'recu': 8}, {'trabajoP': 7}),
    ('gabri', {'parcial': 8}, {'recu': 9}, {'trabajoP': 6}),
    ('hipo', {'parcial': 5}, {'recu': 7}, {'trabajoP': 6}),
    ('hipo', {'parcial': 6}, {'recu': 6}, {'trabajoP': 7})
]

# Obtener nombres únicos de alumnos
alumnos = set(alumno for alumno, *_ in entrada)

# Diccionario final
grupo_alumnos = {}

for a in alumnos:
    parciales = [p['parcial'] for nombre, p, _, _ in entrada if nombre == a]
    recus = [r['recu'] for nombre, _, r, _ in entrada if nombre == a]
    trabajos = [t['trabajoP'] for nombre, _, _, t in entrada if nombre == a]

    grupo_alumnos[a] = {
        'parcial': sum(parciales) / len(parciales),
        'recu': sum(recus) / len(recus),
        'trabajoP': sum(trabajos) / len(trabajos)
    }

print(grupo_alumnos)



