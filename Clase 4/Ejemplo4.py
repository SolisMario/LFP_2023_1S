# importar la libreria
import csv
import graphviz
# importar clase creada de persona
from Persona import Persona

# lista de personas
people = []

csvfile = open('datos.lfp', 'r')
reader = csv.reader(csvfile, delimiter=',')
#ignorar encabezado
next(reader, None)

for row in reader:
    id = row[0]
    name = row[1]
    department = row[2]
    birthday_month = row[3]
    sub = row[4]

    newPersona = Persona(id, name, department, birthday_month, sub)
    people.append(newPersona)

for person in people:
    person.print_name()

def graphRelations(people):
    grafo = graphviz.Digraph('ejemplo', filename="grafo");
    grafo.attr(rankdir="LR")
    for person in people:
        grafo.node(str(person.name), f'''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
            <TR>
                <TD COLSPAN="2"><FONT COLOR="red">{person.name}</FONT></TD>
            </TR>
            <TR>
                <TD><FONT COLOR="red">{person.department}</FONT></TD>
                <TD><FONT COLOR="red">{person.birthday_month}</FONT></TD>
            </TR>
        </TABLE>>''', shape="none")

        subordinados = person.sub.split(':')
        for sub in subordinados:
            if (sub != ''):
                grafo.edge(str(person.name), sub)

    grafo.view()

graphRelations(people)
