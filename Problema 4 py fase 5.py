def contar_titulos(catalogo, umbral_calificacion, anio_limite):
    """Cuenta los títulos con calificación >= umbral y año >= año límite."""
    contador = 0
    for titulo in catalogo:
        anio = titulo[1]
        calificacion = titulo[2]
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador += 1
    return contador


# Matriz: [Título, Año de lanzamiento, Calificación (1 a 10), Género]
catalogo = [
    ["Inception", 2010, 9, "Ciencia ficción"],
    ["Parasite", 2019, 9, "Thriller"],
    ["Coco", 2017, 8, "Animación"],
    ["The Room", 2003, 3, "Drama"],
    ["Dune", 2021, 8, "Ciencia ficción"],
    ["Titanic", 1997, 8, "Romance"],
    ["Oppenheimer", 2023, 9, "Drama"],
    ["Cats", 2019, 4, "Musical"],
]

umbral = int(input("Ingrese la calificación mínima (1 a 10): "))
while umbral < 1 or umbral > 10:
    print("valor inválido. Debe estar entre 1 a 10.")
    umbral = int (input("Ingrese la calificación mínima (1 a 10): "))
anio_limite = int(input("Ingrese el año límite: "))

total = contar_titulos(catalogo, umbral, anio_limite)
print(f"Títulos que cumplen ambos criterios: {total}")
