from typing import List, Dict
import json

def open_json(file_path: str) -> List[Dict]:
    """
    Abre un archivo JSON y devuelve su contenido como una lista de diccionarios.

    :param file_path: Ruta al archivo JSON.
    :return: Lista de diccionarios representando los datos del JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def preferidas(lista_films: List[Dict], genero: str, fecha: int) -> List[Dict]:
    """
    Filtra una lista de películas para devolver solo aquellas que coinciden con el género y la fecha especificados ordenadas de forma descendente por rating.

    :param lista_films: Lista de diccionarios que representan películas.
    :param genero: Género de las películas a filtrar.
    :param fecha: Fecha de lanzamiento de las películas a filtrar.
    :return: Lista de diccionarios que coinciden con el género y la fecha especificados.
    """
    # Su código aquí
    pass



if __name__ == "__main__":

    print(preferidas(open_json("movies_1.json"), "Sci-Fi", 2020))
    # [
    #     {
    #         "title": "Quantum Horizon",
    #         "year": 2024,
    #         "ranking": 54000.0 
    #         // Cálculo: (8.5 * 1000) + (4.5M / 100) + 500 (Bono Original) = 8500 + 45000 + 500
    #     },
    #     {
    #         "title": "Galactic Empire V",
    #         "year": 2020,
    #         "ranking": 38900.0
    #         // Cálculo: (7.9 * 1000) + (3.1M / 100) + 0 = 7900 + 31000
    #     }
    # ]


    print(preferidas(open_json("movies_1.json"), "Thriller", 2023))
    # [
    #     {
    #         "title": "Super Fast Cars 9",
    #         "year": 2023,
    #         "ranking": 85500.0
    #         // (5.5 * 1000) + (8M / 100) = 5500 + 80000.
    #     },
    #     {
    #         "title": "Midnight Whispers",
    #         "year": 2024,
    #         "raking": 26500.0
    #         // (6.0 * 1000) + (2M / 100) + 500 = 6000 + 20000 + 500.
    #     }
    # ]


    print(preferidas(open_json("movies_1.json"), "Comedy", 2020))
    # []


    print(preferidas(open_json("movies_1.json"), "Drama", 2000))
    # [
    #     {
    #         "title": "Romantic Sunset",
    #         "year": 2023,
    #         "ranking": 12200.0
    #         // (7.2 * 1000) + (500k / 100) = 7200 + 5000
    #     }
    # ]