# importar libreria
import graphviz

grafo = graphviz.Digraph('ejemplo', filename="grafo");

grafo.attr(rankdir="LR")

grafo.node('a', '''<
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
        </TABLE>>''', shape="none", margin="0");

grafo.node('b', shape="circle", color="blue")

grafo.edge('a', 'b', label="union", shape="record", style="dotted", color="red")
grafo.view()