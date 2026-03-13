"""
Sistema de Lista de Tareas
Gestiona tareas simples
"""


def mostrar_menu():
    """Muestra el menú"""
    print("\n=== LISTA DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    return input("Elige opción (1-5): ")


def agregar_tarea(tareas):
    """Agrega una tarea a la lista"""
    tarea = input("Ingresa la nueva tarea: ")
    tareas.append({"titulo": tarea, "completada": False})
    print("✓ Tarea agregada")


def ver_tareas(tareas):
    """Muestra todas las tareas"""
    if not tareas:
        print("No hay tareas")
        return

    print("\n=== TUS TAREAS ===")
    for i, tarea in enumerate(tareas, 1):
        estado = "✓" if tarea["completada"] else "○"
        print(f"{i}. [{estado}] {tarea['titulo']}")


def marcar_completada(tareas):
    """Marca una tarea como completada"""
    ver_tareas(tareas)
    if tareas:
        try:
            num = int(input("Número de tarea: "))
            if 1 <= num <= len(tareas):
                tareas[num - 1]["completada"] = True
                print("✓ Tarea marcada como completada")
            else:
                print("Número inválido")
        except ValueError:
            print("Debes ingresar un número")


def eliminar_tarea(tareas):
    """Elimina una tarea"""
    ver_tareas(tareas)
    if tareas:
        try:
            num = int(input("Número de tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                tarea = tareas.pop(num - 1)
                print(f"✓ Tarea '{tarea['titulo']}' eliminada")
            else:
                print("Número inválido")
        except ValueError:
            print("Debes ingresar un número")


def main():
    """Programa principal"""
    tareas = []

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
