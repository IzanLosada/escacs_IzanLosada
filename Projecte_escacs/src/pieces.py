def moviment_peo(taulell, fila, col, fila_dest, col_dest, torn, blancas, negras):
    if torn == 0:  # Blanques
        if fila_dest == fila + 1 and abs(col_dest - col) == 1:
            if taulell[fila_dest][col_dest] in negras:
                return True
            else:
                return False
        if col == col_dest:
            if fila == 1 and fila_dest == fila + 2:
                if taulell[fila + 1][col] == " " and taulell[fila_dest][col] == " ":
                    return True
                else:
                    return False
            elif fila_dest == fila + 1:
                if taulell[fila_dest][col] == " ":
                    return True
                else:
                    return False
    else:  # Negres
        if fila_dest == fila - 1 and abs(col_dest - col) == 1:
            if taulell[fila_dest][col_dest] in blancas:
                return True
            else:
                return False
        if col == col_dest:
            if fila == 6 and fila_dest == fila - 2:
                if taulell[fila - 1][col] == " " and taulell[fila_dest][col] == " ":
                    return True
                else:
                    return False
            elif fila_dest == fila - 1:
                if taulell[fila_dest][col] == " ":
                    return True
                else:
                    return False
    return False

def moviment_cavall(fila, col, fila_dest, col_dest):
    df = abs(fila_dest - fila)
    dc = abs(col_dest - col)
    if (df == 2 and dc == 1) or (df == 1 and dc == 2):
        return True
    else:
        return False

def moviment_torre(taulell, fila, col, fila_dest, col_dest):
    if fila != fila_dest and col != col_dest:
        return False
    if fila == fila_dest:
        if col_dest > col:
            for c in range(col + 1, col_dest):
                if taulell[fila][c] != " ":
                    return False
        else:
            for c in range(col - 1, col_dest, -1):
                if taulell[fila][c] != " ":
                    return False
    else:
        if fila_dest > fila:
            for f in range(fila + 1, fila_dest):
                if taulell[f][col] != " ":
                    return False
        else:
            for f in range(fila - 1, fila_dest, -1):
                if taulell[f][col] != " ":
                    return False
    return True

def moviment_alfil(taulell, fila, col, fila_dest, col_dest):
    if abs(fila_dest - fila) != abs(col_dest - col):
        return False
    dir_f = 1 if fila_dest > fila else -1
    dir_c = 1 if col_dest > col else -1
    f, c = fila + dir_f, col + dir_c
    while f != fila_dest and c != col_dest:
        if taulell[f][c] != " ":
            return False
        f += dir_f
        c += dir_c
    return True

def moviment_reina(taulell, fila, col, fila_dest, col_dest):
    if moviment_torre(taulell, fila, col, fila_dest, col_dest):
        return True
    if moviment_alfil(taulell, fila, col, fila_dest, col_dest):
        return True
    return False

def moviment_rei(fila, col, fila_dest, col_dest):
    df = abs(fila_dest - fila)
    dc = abs(col_dest - col)
    return df <= 1 and dc <= 1