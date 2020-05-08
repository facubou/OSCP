#FrecuencyAnalyzer
#from collections import Counter, defaultdict
import sys

texto = sys.argv[1]
texto = texto.replace(" ", "")
tupla = []

'''
lista = Counter(texto)
print (lista)
l=sorted(lista.items(), reverse=True, key=lambda x: x[1])
print (l)

for i, e in l:
    tupla.append(i)

#lista = lista.keys()

print (tupla)

'''

diccionario={}

for letra in texto:

    if diccionario.has_key(letra):
        diccionario[letra]=diccionario[letra]+1
    else:
        diccionario[letra]=1

l=sorted(diccionario.items(), reverse=True, key=lambda x: x[1])

for i, e in l:
    tupla.append(i)
print (tupla)
