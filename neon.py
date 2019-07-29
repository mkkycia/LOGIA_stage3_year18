def neon_pom(lista):
    pom = lista[0]
    naj = 0
    for x in lista[1:]:
        pom = pom + 2
        naj = max(naj, pom + x)
        pom = max(pom, x)
    return naj

def trans(lista):
    kolumna = []
    for i in range(len(lista[0])):
        wiersz = [lista[j][i] for j in range(len(lista[0]))]
        kolumna.append(wiersz)
    return kolumna

def neon(lista):
    x = max([neon_pom(e) for e in lista])
    pom = trans(lista)
    y = max([neon_pom(e) for e in pom])
    return max(x, y) 

print(neon([10, 4, 5, 7, 1, 4, 1]))
