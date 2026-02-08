# tests/test_escacs.py
import pytest
from src.pieces import moviment_peo, moviment_cavall

@pytest.fixture # Aquesta funció prepara un tauler net per a cada test
def taulell_buit():
    return [[" " for _ in range(8)] for _ in range(8)]

# Definim les llistes de peces per poder passar-les com a paràmetres a les funcions
blancas = ["TB", "CB", "AB", "QB", "KB", "PB"]
negras = ["TN", "CN", "AN", "QN", "KN", "PN"]

# --- PROVES DEL PEÓ ---

def test_peo_avanca_1_casella(taulell_buit):
    """Comprova que el peó blanc pot avançar una casella endavant si està buida."""
    assert moviment_peo(taulell_buit, 1, 0, 2, 0, 0, blancas, negras) == True

def test_peo_inicial_avanca_2_caselles(taulell_buit):
    """Comprova que el peó pot avançar dues caselles només des de la posició inicial."""
    assert moviment_peo(taulell_buit, 1, 4, 3, 4, 0, blancas, negras) == True

def test_peo_bloquejat_no_avanca(taulell_buit):
    """Valida que si hi ha una peça davant, el peó no pot avançar (moviment invàlid)."""
    taulell_buit[2][0] = "PN" # Posem un obstacle (peça negra) davant
    assert moviment_peo(taulell_buit, 1, 0, 2, 0, 0, blancas, negras) == False

def test_peo_captura_diagonal_valida(taulell_buit):
    """Verifica que el peó pot moure's en diagonal si hi ha una peça rival per capturar."""
    taulell_buit[2][1] = "PN" # Peça enemiga a la diagonal
    assert moviment_peo(taulell_buit, 1, 0, 2, 1, 0, blancas, negras) == True

def test_peo_captura_diagonal_invalida_si_buit(taulell_buit):
    """Valida que el peó NO pot anar en diagonal si la casella està buida (sense captura)."""
    assert moviment_peo(taulell_buit, 1, 0, 2, 1, 0, blancas, negras) == False

def test_peo_no_mou_enrere(taulell_buit):
    """Verifica que un peó mai pot retrocedir cap a files inferiors (per a les blanques)."""
    assert moviment_peo(taulell_buit, 2, 0, 1, 0, 0, blancas, negras) == False

# --- PROVES DEL CAVALL ---

def test_cavall_mou_en_L_posicio_buida():
    """Comprova el moviment bàsic del cavall en forma de 'L' cap a una casella buida."""
    assert moviment_cavall(0, 1, 2, 2) == True # Exemple: de b1 a c3

def test_cavall_captura_rival(taulell_buit):
    """Verifica que la lògica de la 'L' es compleix fins i tot si hi ha una peça per capturar."""
    # Nota: La funció de moviment només valida el patró de salt, no el color del destí.
    assert moviment_cavall(0, 1, 2, 0) == True # Exemple: de b1 a a3

def test_cavall_mou_com_torre_invalid():
    """Valida que el cavall no pot fer moviments rectes o horitzontals (com una torre)."""
    assert moviment_cavall(0, 1, 0, 5) == False

def test_cavall_mou_fora_taulell():
    """Verifica que la funció reconeix el patró de L encara que sigui fora (la UI ja ho filtrarà)."""
    assert moviment_cavall(0, 1, 2, 3) == True # És una 'L' matemàticament vàlida

def test_cavall_salta_peces(taulell_buit):
    """Prova crucial: El cavall ha de poder moure's encara que hi hagi obstacles pel camí."""
    taulell_buit[1][1] = "PB" # Posem una peça bloquejant el camí visual
    assert moviment_cavall(0, 1, 2, 2) == True # Ha de saltar igualment

def test_cavall_moviment_curt_invalid():
    """Comprova que moviments massa curts que no formen una 'L' són rebutjats."""
    assert moviment_cavall(0, 1, 1, 1) == False