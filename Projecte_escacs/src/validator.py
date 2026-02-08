# src/validator.py

def comprovar_peça(taulell, fila, columna, torn, blancas, negras):
    peça = taulell[fila][columna]
    if peça == " ":
        print("No hi ha cap peça en aquesta posició!")
        return None
    if peça in blancas and torn == 0:
        print("Peça correcta (blanca)")
        return peça
    if peça in negras and torn == 1:
        print("Peça correcta (negra)")
        return peça
    print("Peça equivocada")
    return None