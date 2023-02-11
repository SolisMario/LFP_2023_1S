# Secuencias de escape
parrafo = 'Lorem Ipsum is simply dummy text of the printing and typesetting \nindustry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. \tIt has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
print(parrafo)

# Iteradores
# a*b 
#   - b > reconocida
#   - ab > reconocida
#   - aaaaaaaab > reconocida
#   - abb > no reconocida

# importar modulo re
import re

patron = re.compile('foo')

texto = """ bar foo bar
foo barbarfoo
foofoo foo bar
"""
# match devuelve none porque no hay coincidencias al inicio del texto 
print(patron.match(texto))

# search encuentra la primera coincidencia en cualquier posicion
print(patron.search(texto))

# findall devuelve la lista de valores que hacen match en todo el texto
print(patron.findall(texto))

# finditer
fi = patron.finditer(texto)
for iter in fi:
    # group(): devuelve el valor que coincide en el objeto
    # start(): posicion de inicio del valor que coincide
    # end(): posicion de fin del valor que coincide
    # span(): tupla de de inicio y fin del valor
    print(iter.group(), iter.start(), iter.end(), iter.span())