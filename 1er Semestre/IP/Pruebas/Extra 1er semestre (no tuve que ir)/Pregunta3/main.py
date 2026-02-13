from typing import List, Tuple
import math

def joyero(
    cadena: List[float],
    max_valor_gema: float = float("inf"),
    min_valor_gema: float = float("-inf")
) -> Tuple[float, int, int]:
    """
    Encuentra el subarreglo continuo con máxima suma que cumpla con las restricciones
    de valor mínimo y máximo por gema usando dividir y vencerás.
    
    Retorna: (valor_máximo, índice_inicio, cantidad_eslabones)
    """
    
    def es_valido(val: float) -> bool:
        return min_valor_gema <= val <= max_valor_gema
    
    def solve(left: int, right: int) -> Tuple[float, int, int]:
        # Caso base: rango inválido
        if left > right:
            return (float('-inf'), -1, 0)
            
        # Caso base: un solo elemento
        if left == right:
            val = cadena[left]
            if es_valido(val):
                return (val, left, 1)
            else:
                return (float('-inf'), -1, 0)
        
        # Dividir
        mid = (left + right) // 2
        
        # Conquistar: resolver mitades izquierda y derecha recursivamente
        left_best = solve(left, mid)
        right_best = solve(mid + 1, right)
        
        # Combinar: calcular mejor subarreglo que cruce el punto medio
        
        # 1. Mejor sufijo de la mitad izquierda (termina en 'mid')
        best_suffix_sum = float('-inf')
        best_suffix_start = -1
        current_sum = 0
        
        for i in range(mid, left - 1, -1):
            val = cadena[i]
            if not es_valido(val):
                break  # No podemos cruzar una gema inválida
            current_sum += val
            if current_sum > best_suffix_sum:
                best_suffix_sum = current_sum
                best_suffix_start = i
        
        # 2. Mejor prefijo de la mitad derecha (empieza en 'mid + 1')
        best_prefix_sum = float('-inf')
        best_prefix_end = -1
        current_sum = 0
        
        for i in range(mid + 1, right + 1):
            val = cadena[i]
            if not es_valido(val):
                break  # No podemos cruzar una gema inválida
            current_sum += val
            if current_sum > best_prefix_sum:
                best_prefix_sum = current_sum
                best_prefix_end = i
        
        # 3. Armar candidato cruzado
        cross_best = (float('-inf'), -1, 0)
        
        if best_suffix_sum != float('-inf') and best_prefix_sum != float('-inf'):
            # Cruzado completo (incluye elementos de ambos lados)
            total_sum = best_suffix_sum + best_prefix_sum
            len_left = mid - best_suffix_start + 1
            len_right = best_prefix_end - (mid + 1) + 1
            cross_best = (total_sum, best_suffix_start, len_left + len_right)
        elif best_suffix_sum != float('-inf'):
            # Solo sufijo válido (el elemento mid+1 es inválido o no existe)
            cross_best = (best_suffix_sum, best_suffix_start, mid - best_suffix_start + 1)
        elif best_prefix_sum != float('-inf'):
            # Solo prefijo válido (el elemento mid es inválido o no existe)
            cross_best = (best_prefix_sum, mid + 1, best_prefix_end - (mid + 1) + 1)
        
        # Elegir el mejor entre los tres candidatos
        candidates = [left_best, right_best, cross_best]
        valid_candidates = [c for c in candidates if c[0] != float('-inf')]
        
        if not valid_candidates:
            return (float('-inf'), -1, 0)
        
        # Desempate: mayor suma > menor índice > menor longitud
        best = valid_candidates[0]
        for c in valid_candidates[1:]:
            if c[0] > best[0]:
                best = c
            elif c[0] == best[0]:
                if c[1] < best[1]:  # Menor índice de inicio
                    best = c
                elif c[1] == best[1] and c[2] < best[2]:  # Menor longitud
                    best = c
        
        return best
    
    if not cadena:
        return (float('-inf'), -1, 0)
    
    return solve(0, len(cadena) - 1)


### Pequeño conjunto de casos de prueba ###

def comprueba_joyero():
    resp1 = joyero([5,-1,3,-6,3])
    print(f"resp1: {resp1}, esperado: (7, 0, 3)")
    
    resp2 = joyero([-3,-1,-2,-6,-4], min_valor_gema=0)
    print(f"resp2: {resp2}, esperado: (-inf, -1, 0)")
    
    resp3 = joyero([-3,-1,-2,-6,-4], -2, -4)
    print(f"resp3: {resp3}, esperado: (-2, 2, 1)")
    
    resp4 = joyero([3,1,2,6,4], 4, 2)
    print(f"resp4: {resp4}, esperado: (4, 4, 1)")
    
    resp5 = joyero([3,1,2,6,4], max_valor_gema=4, min_valor_gema= 1)
    print(f"resp5: {resp5}, esperado: (6, 0, 3)")
    
    resp6 = joyero([3])
    print(f"resp6: {resp6}, esperado: (3, 0, 1)")
    
    resp7 = joyero([5], 4)
    print(f"resp7: {resp7}, esperado: (-inf, -1, 0)")
    
    resp8 = joyero([-1, -6, -3, -5, -2, -7, 8, 1, 3])
    print(f"resp8: {resp8}, esperado: (12, 6, 3)")

comprueba_joyero()