from regex import *
from graphviz import Digraph

class AFD(object):

    def __init__(self, name, title):
        self.regex = None
        self.states = []
        self.transitions = []
        self.initial_state = []
        self.final_states = {}
        self.symbols = []
        self.afd_name = name
        self.title = title

    # Se realiza la simulacion con el algoritmo del libro
    def simulation(self, filename):
        file = open(filename, 'r').read()
        file_stack = []
        for i in file:
            file_stack.append(ord(i))
        characters_list = []
        last_token = None
        while(len(file_stack) != 0):
            characters_list.append(file_stack.pop(0))
            set_final = self.simulate_string(characters_list)

            if(set_final):
                last_final = set_final.pop()
                last_token = self.final_states[last_final]
            else:
                look_ahead = False
                if(len(file_stack) != 0):
                    characters_list.append(file_stack.pop(0))
                    look_ahead = True
                set_final_look_ahead = self.simulate_string(characters_list)
                if(set_final_look_ahead):
                    last_final = set_final_look_ahead.pop()
                    last_token = self.final_states[last_final]
                else:
                    if(look_ahead):
                        file_stack.insert(0, characters_list.pop())
                    if(last_token):
                        file_stack.insert(0, characters_list.pop())
                        token_string = ""
                        for i in characters_list:
                            token_string += chr(i)
                        print(repr(token_string) + " " + last_token)
                        characters_list = []
                        last_token = None
                    else:
                        error_char = chr(characters_list[0])
                        print(repr(error_char) + " " + "Error Lexico")
                        characters_list = []
        if(len(characters_list) != 0 and last_token):
            token_string = ""
            for i in characters_list:
                token_string += chr(i)
            print(repr(token_string) + " " + last_token)
    # Se realiza la simulacion con el algoritmo del libro para una cadena
    def simulate_string(self, string):
        # Se inicializan los estados con e_closure del inicial
        states = [self.initial_state]
        # Se inicia el conteo de caracteres de la cadena
        character_count = 0
        # Mientras hayan caracteres para verificar en el string
        while(character_count < len(string)):
            # Se toman los estados devueltos por e_closure del move con el caracter
            states = self.move(states, string[character_count])
            # Se pasa al siguiente caracter
            character_count += 1
        # Se hacen dos sets para lograr hacer operaciones de conjuntos entre ellos
        set_states = set(states)
        set_final_states = set(self.final_states)
        # Se verifica que los estados encontrados se encuentren en el conjunto de estados finales
        if(set_states.intersection(set_final_states).__len__() != 0):
            return set_states.intersection(set_final_states)
        else:
            return False
    
    # Se utiliza el algoritmo de e-closure para calcular move
    def move(self, states, character):
        # Se inicia el stack con los estados de T
        states_stack = states
        # Se inicia sin estados
        states_result = []
        # Se itera mientra el stack no se encuentre vacio
        while(len(states_stack) != 0):
            # Se saca el estado t
            state = states_stack.pop()
            # Se revisa en cada transicion
            for i in self.transitions:
                # Se revisa que tenga transicion con el caracter
                if(i[0] == state and i[1] == character):
                    # Si el estado no esta en los resultados se ingresa
                    if(i[2] not in states_result):
                        states_result.append(i[2])
        # Se retorna el resultado
        return states_result

    # Funcion para graficar el automata
    def graphAF(self):
        
        # Se realiza el titulo del automata
        description = ("AFD")
        graph = Digraph()
        graph.attr(rankdir="LR", labelloc="t", label=description)
        final_states_keys = list(self.final_states.keys())
        # Por cada estado se crea la imagen para graficarlo
        for state in self.states:
            if(state in self.initial_state):
                graph.node(str(state), str(state), shape="circle", style="filled")
            if(state in final_states_keys):
                graph.node(str(state), str(state), shape="doublecircle", style="filled")
            else:
                graph.node(str(state), str(state), shape="circle")

        # Se crean las transiciones de los estados
        for transition in self.transitions:
            graph.edge(str(transition[0]), str(transition[2]), label=str(transition[1]))

        # Se renderiza
        graph.render(f"./images/{self.afd_name}" + self.title, format="png", view=True)