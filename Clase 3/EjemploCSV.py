# importar la libreria
import csv
# importar clase creada de persona
from Persona import Persona

# lista de personas
people = []

# leer los archivos csv
# with open(<<nombrearchivo.extension>>, <<modo de lectura>>)
# as <<nombre de variable donde se guarda el archivo>>
# delimiter para definir como se separan las columnas
# se obtiene cada linea con la funcion reader
csvfile = open('datos.lfp', 'r')
reader = csv.reader(csvfile, delimiter=',')
#ignorar encabezado
next(reader, None)

for row in reader:
    name = row[0]
    department = row[1]
    birthday_month = row[2]

    newPersona = Persona(name, department, birthday_month)
    people.append(newPersona)

for person in people:
    person.print_name()
