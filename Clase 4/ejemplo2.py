# Generar grafo sin libreria graphviz
import os
# abrir archivo modo escritura
file = open("grafo.dot", "w")
# escribir en el archivo el grafo
file.write('''digraph G {
    rankdir=LR
    a [
        shape=none
        margin=0
        label=<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
            <TR>
                <TD COLSPAN="3"><FONT COLOR="red">TRES</FONT></TD>
            </TR>
            <TR>
                <TD><FONT COLOR="red">uno</FONT></TD>
                <TD><FONT COLOR="red">uno</FONT></TD>
                <TD><FONT COLOR="red">uno</FONT></TD>
            </TR>
            <TR>
                <TD><FONT COLOR="red">uno</FONT></TD>
                <TD><FONT COLOR="red">uno</FONT></TD>
                <TD><FONT COLOR="red">uno</FONT></TD>
            </TR>
        </TABLE>>
    ]

    b [shape=circle style=filled color=blue]

    c [
        shape=none
        margin=0
        label=<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
            <TR>
                <TD COLSPAN="3"><FONT COLOR="red">TRES</FONT></TD>
            </TR>
            <TR>
                <TD><FONT COLOR="red">uno</FONT></TD>
                <TD><FONT COLOR="red">uno</FONT></TD>
                <TD><FONT COLOR="red">uno</FONT></TD>
            </TR>
            <TR>
                <TD><FONT COLOR="red">uno</FONT></TD>
                <TD><FONT COLOR="red">uno</FONT></TD>
                <TD><FONT COLOR="red">uno</FONT></TD>
            </TR>
        </TABLE>>
    ]

    d [shape=circle style=filled color=blue]

    a -> b [label=union shape=record style=dotted color=red ]
    c -> d [label=union shape=record style=dotted color=red ]
    c -> b
}''')
#@ cerrar el archivo
file.close()
# ejecutar el comando dot 
os.system("dot -Tpdf grafo.dot -o  grafo.pdf")