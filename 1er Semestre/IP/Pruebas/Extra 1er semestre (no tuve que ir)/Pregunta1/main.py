from typing import List, Tuple, Optional

def encontrar_pieza(tablero: List[List[str]], pieza: str) -> Optional[Tuple[int, int]]:
    """
    Busca una pieza específica en el tablero y devuelve sus coordenadas (fila, columna).
    Retorna None si no la encuentra.
    """
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == pieza:
                return (i, j)
    return None

def hay_pieza_intermedia(tablero: List[List[str]], 
                        inicio: Tuple[int, int], 
                        fin: Tuple[int, int]) -> bool:
    """
    Verifica si hay alguna pieza entre dos posiciones (excluyendo los extremos).
    Asume que las posiciones están alineadas (misma fila, columna o diagonal).
    """
    fila_inicio, col_inicio = inicio
    fila_fin, col_fin = fin
    
    # Determinar dirección del movimiento
    delta_fila = 0 if fila_fin == fila_inicio else (1 if fila_fin > fila_inicio else -1)
    delta_col = 0 if col_fin == col_inicio else (1 if col_fin > col_inicio else -1)
    
    # Avanzar un paso desde el inicio
    fila_actual = fila_inicio + delta_fila
    col_actual = col_inicio + delta_col
    
    # Verificar todas las casillas intermedias hasta llegar al destino
    while (fila_actual, col_actual) != (fila_fin, col_fin):
        if tablero[fila_actual][col_actual] is not None:
            return True  # Hay una pieza bloqueando
        fila_actual += delta_fila
        col_actual += delta_col
    
    return False  # No hay piezas intermedias

def dama_amenaza(tablero: List[List[str]]) -> bool:
    """
    Determina si la dama negra ("DN") pone en jaque al rey blanco ("RB").
    
    Retorna True si:
    - Están en la misma fila, columna o diagonal
    - No hay piezas entre ellas
    
    Retorna False en cualquier otro caso.
    """
    # Buscar posiciones de las piezas
    pos_dama = encontrar_pieza(tablero, "DN")
    pos_rey = encontrar_pieza(tablero, "RB")
    
    # Si no se encuentra alguna pieza, no hay jaque
    if pos_dama is None or pos_rey is None:
        return False
    
    fila_dama, col_dama = pos_dama
    fila_rey, col_rey = pos_rey
    
    # Verificar si están en la misma fila
    misma_fila = (fila_dama == fila_rey)
    # Verificar si están en la misma columna
    misma_columna = (col_dama == col_rey)
    # Verificar si están en diagonal (diferencia de filas = diferencia de columnas)
    misma_diagonal = (abs(fila_dama - fila_rey) == abs(col_dama - col_rey))
    
    # Si no están alineados de ninguna forma, no hay amenaza
    if not (misma_fila or misma_columna or misma_diagonal):
        return False
    
    # Si están alineados, verificar que no haya piezas entre ellos
    return not hay_pieza_intermedia(tablero, pos_dama, pos_rey)



def cargar_tablero_desde_archivo(ruta_archivo: str) -> List[List[str]]:
    """
    Carga un tablero desde un archivo de texto.
    Formato esperado: 8 líneas con elementos separados por comas.
    None se representa como 'None' (string) en el archivo.
    """
    tablero = []
    with open(ruta_archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            elementos = [None if x.strip() == 'None' else x.strip() 
                        for x in linea.split(',')]
            tablero.append(elementos)
    return tablero


tablero_jaque_diagonal = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, "DN", None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, "RB", None],
        [None, None, None, None, None, None, None, None]
    ]
    
print(f"Jaque diagonal: {dama_amenaza(tablero_jaque_diagonal)}")  # True
    
    # Ejemplo 2: No jaque (misma diagonal pero pieza intermedia)
tablero_pieza_intermedia = [
        [None, None, None, None, None, None, None, None],
        [None, None, "DN", None, None, None, None, None],
        [None, None, None, "PN", None, None, None, None],  # Peón bloqueando
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, "RB", None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    
print(f"Pieza intermedia: {dama_amenaza(tablero_pieza_intermedia)}")  # False
    
    # Ejemplo 3: No jaque (ni en fila, columna ni diagonal)
tablero_sin_amenaza = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, "DN", None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, "RB", None, None, None, None, None, None],  # Rey en otra posición
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    
print(f"Sin amenaza: {dama_amenaza(tablero_sin_amenaza)}")  # False
    
    # Ejemplo 4: Jaque horizontal
tablero_jaque_horizontal = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        ["DN", None, None, None, None, None, "RB", None],  # Misma fila
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    
print(f"Jaque horizontal: {dama_amenaza(tablero_jaque_horizontal)}")  # True
