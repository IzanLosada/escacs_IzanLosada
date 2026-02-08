# src/main.py
from src.board import *
from src.pieces import *
from src.validator import *

# Constants globals
BLANCAS = ["TB", "CB", "AB", "QB", "KB", "PB"]
NEGRAS = ["TN", "CN", "AN", "QN", "KN", "PN"]
LLETRES = ["A", "B", "C", "D", "E", "F", "G", "H"]

def crear_jugadors():
    """Demana els noms i retorna una llista."""
    j1 = input("Introdueix el nom del jugador 1 (Blanc): ")
    j2 = input("Introdueix el nom del jugador 2 (Negre): ")
    return [j1, j2]

def demanar_coordenada(missatge):
    """Gestiona l'entrada de fila i columna per separat per evitar errors."""
    while True:
        print(f"\n--- {missatge} ---")
        fila_input = input("Fila (1 - 8): ")
        
        # Validació de fila (numèrica)
        try:
            fila = int(fila_input) - 1
            if not (0 <= fila <= 7):
                print("Error: La fila ha d'estar entre 1 i 8.")
                continue
        except ValueError:
            print("Error: Introdueix un número vàlid per a la fila.")
            continue

        # Validació de columna (lletra)
        col_input = input("Columna (a - h): ").upper()
        if col_input not in LLETRES:
            print("Error: La columna ha de ser una lletra entre A i H.")
            continue
            
        col = LLETRES.index(col_input)
        return fila, col

def mostrar_resum(historial):
    """Imprimeix l'historial de moviments al final."""
    print("\n" + "="*30)
    print("      RESUM DE LA PARTIDA")
    print("="*30)
    for i, mov in enumerate(historial, 1):
        print(f"{i}. {mov}")

def gestionar_nova_partida():
    """Pregunta si es vol tornar a jugar i amb quins noms."""
    vol_jugar = input("\nVols jugar una altra partida? (SI/NO): ").upper()
    if vol_jugar != "SI":
        return False, None
    
    mateixos_noms = input("Voleu mantenir els mateixos noms? (SI/NO): ").upper()
    return True, mateixos_noms

def joc(jugadors):
    """Funció principal de la partida."""
    ronda, torn = 1, 0
    guanyador_nom = None
    taulell = crear_taulell()
    captures_b, captures_n = [], []
    historial = []

    while not guanyador_nom:
        print(f"\n{'*' * 20}")
        print(f"  RONDA {ronda} | Torn de: {jugadors[torn]}")
        print(f"{'*' * 20}")
        
        mostrar_taulell(taulell, captures_b, captures_n)

        # 1. Selecció de peça d'origen
        f_o, c_o = demanar_coordenada("ORIGEN")
        peça = comprovar_peça(taulell, f_o, c_o, torn, BLANCAS, NEGRAS)
        if peça is None: 
            continue

        # 2. Selecció de destí
        f_d, c_d = demanar_coordenada(f"DESTÍ ({peça})")
        
        if f_o == f_d and c_o == c_d:
            print("Error: L'origen i el destí són iguals.")
            continue

        # 3. Validació segons el tipus de peça (Clean Branching)
        es_valid = False
        if peça in ("PB", "PN"):
            es_valid = moviment_peo(taulell, f_o, c_o, f_d, c_d, torn, BLANCAS, NEGRAS)
        elif peça in ("CB", "CN"):
            es_valid = moviment_cavall(f_o, c_o, f_d, c_d)
        elif peça in ("TB", "TN"):
            es_valid = moviment_torre(taulell, f_o, c_o, f_d, c_d)
        elif peça in ("AB", "AN"):
            es_valid = moviment_alfil(taulell, f_o, c_o, f_d, c_d)
        elif peça in ("QB", "QN"):
            es_valid = moviment_reina(taulell, f_o, c_o, f_d, c_d)
        elif peça in ("KB", "KN"):
            es_valid = moviment_rei(f_o, c_o, f_d, c_d)

        if not es_valid:
            print(f"Error: Moviment il·legal per al {peça}.")
            continue

        # 4. Gestió de captures i foc amic
        desti_peça = taulell[f_d][c_d]
        if desti_peça != " ":
            if (torn == 0 and desti_peça in BLANCAS) or (torn == 1 and desti_peça in NEGRAS):
                print(f"Error: No pots capturar la teva pròpia peça ({desti_peça})!")
                continue
            
            # Registrar captura
            (captures_b if torn == 0 else captures_n).append(desti_peça)
            print(f"Captura! {jugadors[torn]} ha eliminat {desti_peça}")

        # 5. Executar moviment i guardar historial
        historial.append(f"{jugadors[torn]} ({peça}): {LLETRES[c_o]}{f_o+1} -> {LLETRES[c_d]}{f_d+1}")
        taulell[f_d][c_d], taulell[f_o][c_o] = peça, " "
        
        # 6. Comprovació de victòria
        b_restants, n_restants = comptar_fitxes(taulell)
        if b_restants == 0:
            guanyador_nom = jugadors[1]
        elif n_restants == 0:
            guanyador_nom = jugadors[0]
        else:
            # Canvi de torn
            torn = 1 if torn == 0 else 0
            if torn == 0: ronda += 1

    # Final de partida
    mostrar_taulell(taulell, captures_b, captures_n)
    print(f"\nFELICITATS! El guanyador és {guanyador_nom}.")
    mostrar_resum(historial)
    return guanyador_nom

if __name__ == "__main__":
    noms_jugadors = crear_jugadors()
    mentre_jugant = True
    
    while mentre_jugant:
        joc(noms_jugadors)
        
        tornar_a_començar, mateixos = gestionar_nova_partida()
        if not tornar_a_començar:
            print("Gràcies per jugar!")
            mentre_jugant = False
        elif mateixos == "NO":
            noms_jugadors = crear_jugadors()