from typing import List
import json


def captura_maxima_corona_blanca(tablero: List[List[str]]) -> int:
    pass


def load_json(file_name:str):
    with open(file_name, "r") as fd:
        data = json.load(fd)
    return data

if __name__ == "__main__":
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    RESET = "\033[0m"

    ejemplos = load_json("ejemplos.json")
    for indice, ejemplo in enumerate(ejemplos):
        tab, sol = ejemplo
        result = captura_maxima_corona_blanca(tab)
        print(
            f"{VERDE} Ejemplo {indice+1} correcto {RESET}"
            if result == sol
            else f"{ROJO} Ejemplo {indice+1} errado, esperado:{sol} resp:{result} {RESET}"
        )