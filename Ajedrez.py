blancas = ["TB", "CB", "AB", "QB", "KB", "PB"]  # Llistes fixes
negras = ["TN", "CN", "AN", "QN", "KN", "PN"]
lletres = ["A", "B", "C", "D", "E", "F", "G", "H"]

def crear_jugadors():
    jugadors = []  # Llista de jugadors
    j1 = input("Introdueix el nom del jugador 1 (Blanc): ")
    j2 = input("Introdueix el nom del jugador 2 (Negre): ")

    jugadors.append(j1) # Afegim els jugadors
    jugadors.append(j2)

    print(f"Jugador 1: {jugadors[0]}, Jugador 2: {jugadors[1]}") 
    print("Noms assignats, comença la partida!")

    return jugadors

def crear_taulell():
    taulell = []

    for i in range(8): # Creem el taulell
        fila = []
        for j in range(8):
            fila.append(" ")
        taulell.append(fila)

    taulell[1] = ["PB"] * 8 # Creem peons a la fila 1
    taulell[0] = ["TB", "CB", "AB", "QB", "KB", "AB", "CB", "TB"] # I la resta de peces una fila per davant

    taulell[7] = ["TN", "CN", "AN", "QN", "KN", "AN", "CN", "TN"]
    taulell[6] = ["PN"] * 8

    return taulell

def mostrar_taulell(taulell): 
    print("\n    a    b    c    d    e    f    g    h") # Per mostrar el taulell fem els prints perque es vegi amb sentit
    print("  +" + "----+" * 8)

    for i in range(8):
        print(f"{i + 1} |", end="") # Deixem les separacions
        for peça in taulell[i]:
            if peça == " ":
                print("    |", end="")
            else:
                print(f" {peça} |", end="")
        print(f" {i + 1}")
        print("  +" + "----+" * 8)

    print("    a    b    c    d    e    f    g    h\n")

def comprovar_peça(taulell, fila, columna, torn, blancas, negras): # Funció per comprovar color de peça amb torn
    peça = taulell[fila][columna]

    if peça == " ": # Si no hi ha peça a la posició seleccionada
        print("No hi ha cap peça en aquesta posició!")
        return None

    if peça in blancas and torn == 0: # Si la peça és del torn corresponent
        print("Peça correcta (blanca)")
        return peça # La retornem com a correcta

    if peça in negras and torn == 1:
        print("Peça correcta (negra)")
        return peça

    print("Peça equivocada") # En cas que no compleixi cap condició anterior haurà escollit una peça de color equivocat
    return None

def comptar_fitxes(taulell): # Funció per comptar fitxes
    blanques = 0 # Comptadors
    negres = 0

    for fila in taulell: # Comprovem peçes per fila al taulell
        for peça in fila:
            if peça in blancas: # Comprovem el color i les afegim al comptador
                blanques += 1
            elif peça in negras:
                negres += 1

    return blanques, negres # Returnem els comptadors

def moviment_peo(taulell, fila, col, fila_dest, col_dest, torn, blancas, negras):
    if torn == 0:  # Blanques
        # Captura diagonal
        if fila_dest == fila + 1 and abs(col_dest - col) == 1:
            # En cas de mover-se en diagonal, haurà de comprovar que hi hagi peça negra
            if taulell[fila_dest][col_dest] in negras:
                return True  # Si és així retornem True
            else:
                return False

        # Moviment recte
        if col == col_dest:  # Comprovem que només es mogui en la mateixa columna
            if fila == 1 and fila_dest == fila + 2:  # En cas de ser el primer moviment sumarà 2
                # Comprovem que la posició de davant estigui buida i no hi hagi opció de matar
                if taulell[fila + 1][col] == " " and taulell[fila_dest][col] == " ":
                    return True
                else:
                    return False

            elif fila_dest == fila + 1:  # En qualsevol altre cas només es podrà anar cap endavant
                if taulell[fila_dest][col] == " ":
                    return True
                else:
                    return False

    else:  # Negres
        # Captura diagonal
        if fila_dest == fila - 1 and abs(col_dest - col) == 1:
            # En cas de mover-se en diagonal, haurà de comprovar que hi hagi peça blanca
            if taulell[fila_dest][col_dest] in blancas:
                return True
            else:
                return False

        # Moviment recte
        if col == col_dest:  # Comprovem que només es mogui en la mateixa columna
            if fila == 6 and fila_dest == fila - 2:  # En cas de ser el primer moviment sumarà 2
                # Comprovem que la posició de davant estigui buida i no hi hagi opció de matar
                if taulell[fila - 1][col] == " " and taulell[fila_dest][col] == " ":
                    return True
                else:
                    return False

            elif fila_dest == fila - 1:  # En qualsevol altre cas només es podrà anar cap endavant
                if taulell[fila_dest][col] == " ":
                    return True
                else:
                    return False

    return False

def moviment_cavall(fila, col, fila_dest, col_dest):
    df = abs(fila_dest - fila)  # Calculem valor absolut de fila i columna
    dc = abs(col_dest - col)
    
    # Posem les uniques opcions correctes
    if (df == 2 and dc == 1) or (df == 1 and dc == 2):
        return True
    else:
        return False

def moviment_torre(taulell, fila, col, fila_dest, col_dest):
    if fila != fila_dest and col != col_dest: # Comprovem que de la columna o fila només una sigui diferent
        return False

    # Moviment horitzontal
    if fila == fila_dest:
        if col_dest > col: # Si va endavant
            for c in range(col + 1, col_dest): # Bucle per comprovar recorregut
                if taulell[fila][c] != " ": # Si no està buit donarà false
                    return False
        else: # Si va enrere
            for c in range(col - 1, col_dest, -1):
                if taulell[fila][c] != " ":
                    return False

    # Moviment vertical
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
    if abs(fila_dest - fila) != abs(col_dest - col):  # Si no es mou mateixes files que columnes no serà vàlid
        return False

    if fila_dest > fila: # Determinem la direcció de moviment
        dir_f = 1 # Endavant
    else:
        dir_f = -1 # Enrere

    if col_dest > col:
        dir_c = 1 # Esquerra
    else:
        dir_c = -1 # Dreta

    f = fila + dir_f # Noves posicions
    c = col + dir_c

    while f != fila_dest and c != col_dest: # Recorregut
        if taulell[f][c] != " ": # Si no estàn buides
            return False # Moviment invàlid
        f += dir_f
        c += dir_c

    return True

def moviment_reina(taulell, fila, col, fila_dest, col_dest, torn, blancas, negras):
    # Pot fer tots els moviments d'un alfil o una torre
    if moviment_torre(taulell, fila, col, fila_dest, col_dest, torn, blancas, negras):
        return True
    if moviment_alfil(taulell, fila, col, fila_dest, col_dest, torn, blancas, negras):
        return True
    return False # Qualsevol altre

def moviment_rei(fila, col, fila_dest, col_dest):
    df = abs(fila_dest - fila) # Calculem valors absoluts del moviment
    dc = abs(col_dest - col)

    return df <= 1 and dc <= 1 # En cas de ser menors o igual a 1 els retornem

def posicio_desti():
    while True:
        fila_desti = input("Fila (1 - 8): ") # Demanem fila destí
        try:
            fila_desti = int(fila_desti) - 1 # Li restem 1 per adaptar-lo a la llista
        except ValueError:
            print("Introdueix un número")
            continue

        if fila_desti < 0 or fila_desti > 7: # Comprovem que no surti del taulell
            print("Fila invàlida")
            continue

        columna_desti = input("Columna (a - h): ").upper() # Demanem columna destí

        if columna_desti not in lletres: # Si la columna no es troba a la llista de lletres
            print("Columna invàlida")
            continue

        col = lletres.index(columna_desti) # Agafem l'index de la columna que serà la columna
        return fila_desti, col
    
def otraPartida(): 
    otra = ""
    while otra != "SI" and otra != "NO": 
        otra = input("Vols jugar una altra partida? SI/NO ").upper()

    if otra == "NO": # Si decideix no jugar una altra finalitzem partida
        print("Partida finalitzada.")
        return False, None # Returnem si es vol jugar una altra partida y també no a nous noms

    nouNoms = ""
    while nouNoms != "SI" and nouNoms != "NO": # Demanem i retornem nous noms en cas de ser necesaris
        nouNoms = input("Voleu jugar amb els mateixos noms? SI/NO ").upper()

    return True, nouNoms

def joc():
    ronda = 1 # Comptadors, variable de guanyador...
    guanyador = False
    torn = 0

    print(f"RONDA {ronda}") 

    while not guanyador:
        mostrar_taulell(taulell_def)
        print(f"Torn del jugador {torn + 1}, {jugadors[torn]}")

        fila, col = posicio_desti() # Demanem la posició per la fitxa

        peça_origen = comprovar_peça(taulell_def, fila, col, torn, blancas, negras) # Fem les comprovacions necessàries

        if peça_origen is None: # En cas de retornar none la peça serà invàlida i tornarà a començar
            continue

        fila_dest, col_dest = posicio_desti()
        
        if fila == fila_dest and col == col_dest: # En cas de coincidir posició actual i destí ho mostrem
            print("La posició destí no pot ser la mateixa que l'origen")
            continue

        # Corregido: pasamos todos los parámetros necesarios
        if peça_origen in ("PB", "PN"): # Moviment per peó
            if not moviment_peo(taulell_def, fila, col, fila_dest, col_dest, torn, blancas, negras):
                print("Moviment de peó invàlid")
                continue

        if peça_origen in ("CB", "CN"): # Moviment per cavall
            if not moviment_cavall(fila, col, fila_dest, col_dest):  # No necesita taulell ni colores
                print("Moviment de cavall invàlid")
                continue

        if peça_origen in ("TB", "TN"): # Moviment per torre
            if not moviment_torre(taulell_def, fila, col, fila_dest, col_dest, torn, blancas, negras):
                print("Moviment de torre invàlid")
                continue
            
        if peça_origen in ("AB", "AN"): # Moviment per alfil
            if not moviment_alfil(taulell_def, fila, col, fila_dest, col_dest, torn, blancas, negras):
                print("Moviment d'alfil invàlid")
                continue

        if peça_origen in ("QB", "QN"): # Moviment per la reina
            if not moviment_reina(taulell_def, fila, col, fila_dest, col_dest, torn, blancas, negras):
                print("Moviment de reina invàlid")
                continue

        if peça_origen in ("KB", "KN"): # Moviment pel rei
            if not moviment_rei(fila, col, fila_dest, col_dest):
                print("Moviment de rei invàlid")
                continue

        if taulell_def[fila_dest][col_dest] != " ": # En cas d'anar a una posició amb fitxa
            if torn == 0 and taulell_def[fila_dest][col_dest] in blancas: # En cas de ser del mateix color serà invàlid
                print("No pots matar una peça blanca!")
                continue
            if torn == 1 and taulell_def[fila_dest][col_dest] in negras:
                print("No pots matar una peça negra!")
                continue

        taulell_def[fila_dest][col_dest] = peça_origen # En cas que tot sigui valid s'executa el moviment
        taulell_def[fila][col] = " "
        
        blanques, negres = comptar_fitxes(taulell_def) # Comprovem si queden fitxes en cada moviment al taulell

        if blanques == 0: # Si no queden d'algun color guanya l'altre jugador
            print(f"GUANYADOR: {jugadors[1]} (Negres)")
            guanyador = True
            break

        if negres == 0: 
            print(f"GUANYADOR: {jugadors[0]} (Blanques)")
            guanyador = True
            break

        torn += 1 

        if torn > 1: # En arribar al segon torn cambiem de torn i ronda
            ronda += 1
            torn = 0

if __name__ == "__main__":
    jugadors = crear_jugadors() # Creem els jugadors
    seguir = True
    while seguir == True: # Mentre es pugui es seguirà
        taulell_def = crear_taulell() # Creem i mostrem taulell
        mostrar_taulell(taulell_def)
        joc()
        otra, nousNoms = otraPartida() 
        
        if otra == True and nousNoms == "NO": # En cas de voler cambiar noms
            jugadors = crear_jugadors() # Executem de nou la funció de crear jugadors