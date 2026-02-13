from typing import Dict, Tuple
import json, os

def load_json(file_name: str) -> Dict:
    route = os.path.join(os.path.dirname(__file__), file_name)
    with open(route, "r", encoding = "utf-8") as f:
        return json.load(f)
    return data

def write_in_json(file_name: str, file):
    with open(file_name, "w", encoding='utf-8') as fd:
        json.dump(file, fd, indent=4, ensure_ascii=False)

def actualiza_inventario() -> Tuple[float, float]:
    inventario = load_json("inventario.json")
    operaciones = load_json("operaciones.json")
    
    ganancia_total = 0.0
    inversion_total = 0.0
    
    for operacion in operaciones:
        accion = operacion["acción"]
        nombre_producto = operacion["producto"]
        cantidad = operacion["cantidad"]
        producto = inventario[nombre_producto]
        
        if accion == "venta":
            precio = producto["precio_de_venta"]
            costo = producto["precio_de_costo"]
            ganancia = (precio - costo) * cantidad
            ganancia_total += ganancia
            producto["disponibilidad"] -= cantidad
            
        elif accion == "compra":
            costo = producto["precio_de_costo"]
            inversion_total += costo * cantidad
            producto["disponibilidad"] += cantidad
    
    return (ganancia_total, inversion_total)


print(actualiza_inventario())
