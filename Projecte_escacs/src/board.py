from src.main import blancas, negras  

def crear_taulell():
    taulell = []
    for i in range(8):
        fila = []
        for j in range(8):
            fila.append(" ")
        taulell.append(fila)

    taulell[1] = ["PB"] * 8
    taulell[0] = ["TB", "CB", "AB", "QB", "KB", "AB", "CB", "TB"]
    taulell[7] = ["TN", "CN", "AN", "QN", "KN", "AN", "CN", "TN"]
    taulell[6] = ["PN"] * 8
    return taulell

def mostrar_taulell(taulell, peces_blanques_capturades, peces_negres_capturades): 
    print("\n    a    b    c    d    e    f    g    h")
    print("  +" + "----+" * 8)
    for i in range(8):
        print(f"{i + 1} |", end="")
        for peça in taulell[i]:
            if peça == " ":
                print("    |", end="")
            else:
                print(f" {peça} |", end="")
        print(f" {i + 1}")
        print("  +" + "----+" * 8)
    print("    a    b    c    d    e    f    g    h\n")

    print(f"Peces capturades per les blanques: {peces_blanques_capturades}")
    print(f"Peces capturades per les negres: {peces_negres_capturades}")

def comptar_fitxes(taulell):
    blanques = 0
    negres = 0
    for fila in taulell:
        for peça in fila:
            if peça in blancas:
                blanques += 1
            elif peça in negras:
                negres += 1
    return blanques, negres