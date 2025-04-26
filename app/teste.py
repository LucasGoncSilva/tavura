lista = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 20},
    {"nome": "Carlos", "idade": 30}
]

# Ordenando pela idade
ordenada = sorted(lista, key=lambda x: x["idade"])

print(ordenada)