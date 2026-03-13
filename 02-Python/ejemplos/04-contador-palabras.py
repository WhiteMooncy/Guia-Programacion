"""
Contador de Palabras en un Archivo
Lee un archivo de texto y cuenta palabras y caracteres
"""


def contar_palabras(archivo):
    """
    Lee un archivo y cuenta palabras

    Args:
        archivo (str): Ruta del archivo

    Returns:
        dict: Estadísticas del archivo
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()

        palabras = contenido.split()
        caracteres = len(contenido)
        palabras_unicas = len(set(palabras))

        return {
            "palabras_totales": len(palabras),
            "caracteres": caracteres,
            "palabras_unicas": palabras_unicas,
            "lineas": len(contenido.split("\n")),
        }
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo}' no encontrado")
        return None


def contar_frecuencia(archivo, top=10):
    """
    Cuenta la frecuencia de palabras

    Args:
        archivo (str): Ruta del archivo
        top (int): Top N palabras más frecuentes
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read().lower()

        # Limpiar caracteres especiales
        caracteres_especiales = ".,!?;:\"'\n"
        for char in caracteres_especiales:
            contenido = contenido.replace(char, " ")

        palabras = contenido.split()

        # Contar frecuencias
        frecuencias = {}
        for palabra in palabras:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

        # Ordenar por frecuencia
        ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

        print(f"\n{'PALABRA':<20} {'FRECUENCIA':<10}")
        print("-" * 30)
        for palabra, frecuencia in ordenadas[:top]:
            if len(palabra) > 2:  # Ignorar palabras muy cortas
                print(f"{palabra:<20} {frecuencia:<10}")

    except FileNotFoundError:
        print(f"Error: Archivo '{archivo}' no encontrado")


def crear_archivo_ejemplo():
    """Crea un archivo de ejemplo"""
    texto = """Python es un lenguaje de programación versátil.
Python es muy popular para desarrollo web.
Python se usa en ciencia de datos.
Python tiene una comunidad muy grande.
Python es fácil de aprender y poderoso."""

    with open("ejemplo.txt", "w", encoding="utf-8") as f:
        f.write(texto)
    print("✓ Archivo 'ejemplo.txt' creado")


def main():
    """Programa principal"""
    print("=== CONTADOR DE PALABRAS ===\n")

    # Crear archivo de ejemplo si no existe
    import os

    if not os.path.exists("ejemplo.txt"):
        crear_archivo_ejemplo()

    # Contar estadísticas
    stats = contar_palabras("ejemplo.txt")

    if stats:
        print("ESTADÍSTICAS DEL ARCHIVO:")
        print(f"Total de palabras: {stats['palabras_totales']}")
        print(f"Caracteres: {stats['caracteres']}")
        print(f"Palabras únicas: {stats['palabras_unicas']}")
        print(f"Líneas: {stats['lineas']}")

        # Mostrar palabras más frecuentes
        print("\nPALABRAS MÁS FRECUENTES:")
        contar_frecuencia("ejemplo.txt", top=5)


if __name__ == "__main__":
    main()
