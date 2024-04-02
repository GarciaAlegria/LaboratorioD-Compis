import readyalex as read
import shuntingyard as sy
import dfa_minimization as dfa_min
import arbol
import dfa_directly as direct
import time
import pickle

def main():
    start_time = time.time()
    yalex_file = 'slr-1.yal' 
    content = read.read_yalex(yalex_file)
    if content:
        print("====================================================")
        print("Reguex del Archivo Yalex ==========================")
        print(content)
        print("====================================================")
        print("====================================================")
        postfix = sy.shunting_yard(content)
        print("Postfix de la regex ================================")
        print(postfix)
        print("====================================================")
        print("====================================================")
        print("Generando árbol de expresión...")
        stack, node_list, alfabeto = arbol.exec(postfix, True)
        print("Árbol de expresión generado y guardado como 'expression_tree.png'")
        print("=====================================================")
        print("=====================================================")
        print("Generando DFA...")
        
        # Construir el DFA directamente desde el árbol
        estadoscon, alfabetocon, Dtran, estado_inicialcon, estado_finalcon = direct.exec(stack, node_list, alfabeto)

        DFAdirect = {
            "states": estadoscon,
            "transitions": Dtran,
            "symbols": alfabetocon,
            "start_states": estado_inicialcon,
            "final_states": estado_finalcon
        }

        print("DFA Directo terminado")
        print("=====================================================")
        estadosAFD = set()
    for i in estadoscon:
        estadosAFD.add(str(i))

    alfabetoAFD = set()
    for i in alfabetocon:
        alfabetoAFD.add(str(i))

    transicionesAFD = set()
    for tran in Dtran:
        trans = ()
        for t in tran:
            trans = trans + (str(t),)
        transicionesAFD.add(trans)

    estado_inicialAFD = {str(estado_inicialcon)}

    estados_aceptacionAFD = set()
    for i in estado_finalcon:
        estados_aceptacionAFD.add(str(i))

    print("Creando DFA Minimizacion")

    new_states, symbols, new_transitions, newStart_states, newFinal_states = dfa_min.exec(estadosAFD, alfabetoAFD, transicionesAFD, estado_inicialAFD, estados_aceptacionAFD, True, True)

    print("DFA Minimizado terminado")

    DFAMin = {
        "states": new_states,
        "transitions": new_transitions,
        "symbols": symbols,
        "start_states": newStart_states,
        "final_states": newFinal_states
    }

    with open('DFAMin.pickle', 'wb') as f:
        pickle.dump(DFAMin, f)

    print("DFAMin guardado")

    end_time = time.time()

    time_taken = end_time - start_time

    print(f"\nTime taken by the operation is {time_taken} seconds")

if __name__ == "__main__":
    main()
