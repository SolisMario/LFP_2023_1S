class AFD:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}
        self.alfabeto = {'a','b'}
        self.transiciones = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q2', 'b': 'q1'},
            'q2': {'a': 'q1', 'b': 'q2'}
        }
        self.estado_inicial = 'q0'
        self.estados_finales = {'q0', 'q2'}

    def analizar(self, cadena):
        estado_actual = self.estado_inicial
        for char in cadena:
            if char not in self.alfabeto:
                return False
            estado_actual = self.transiciones[estado_actual][char]
        return estado_actual in self.estados_finales
    
dfa = AFD()
print(dfa.analizar('aabbaa'))  # True
print(dfa.analizar('baaabbaa'))  # False
print(dfa.analizar('aaa'))  # False
print(dfa.analizar('abba'))  # True