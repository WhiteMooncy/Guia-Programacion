"""
Sistema de Gestión de Contactos
Almacena, busca y modifica contactos
"""


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 40)
    print("GESTOR DE CONTACTOS")
    print("=" * 40)
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Editar contacto")
    print("6. Guardar y salir")
    return input("Elige opción: ")


def agregar_contacto(contactos):
    """Agrega un nuevo contacto"""
    print("\n--- NUEVO CONTACTO ---")
    nombre = input("Nombre: ").strip()

    # Verificar si ya existe
    if nombre.lower() in [c["nombre"].lower() for c in contactos]:
        print("⚠ Este contacto ya existe")
        return

    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()

    contacto = {"nombre": nombre, "telefono": telefono, "email": email}

    contactos.append(contacto)
    print("✓ Contacto agregado")


def ver_contactos(contactos):
    """Muestra todos los contactos"""
    if not contactos:
        print("No hay contactos")
        return

    print("\n" + "=" * 60)
    print(f"{'NOMBRE':<20} {'TELÉFONO':<15} {'EMAIL':<25}")
    print("=" * 60)

    for contacto in contactos:
        print(
            f"{contacto['nombre']:<20} {contacto['telefono']:<15} {contacto['email']:<25}"
        )
    print("=" * 60)


def buscar_contacto(contactos):
    """Busca un contacto por nombre"""
    nombre = input("¿Nombre a buscar?: ").strip().lower()

    resultados = [c for c in contactos if nombre in c["nombre"].lower()]

    if not resultados:
        print("No encontrado")
        return

    print("\nRESULTADOS:")
    for contacto in resultados:
        print(f"\nNombre: {contacto['nombre']}")
        print(f"Teléfono: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")


def eliminar_contacto(contactos):
    """Elimina un contacto"""
    nombre = input("¿Nombre a eliminar?: ").strip().lower()

    for i, contacto in enumerate(contactos):
        if contacto["nombre"].lower() == nombre:
            contactos.pop(i)
            print(f"✓ {contacto['nombre']} eliminado")
            return

    print("No encontrado")


def editar_contacto(contactos):
    """Edita un contacto existente"""
    nombre = input("¿Nombre a editar?: ").strip().lower()

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre:
            print("Deja en blanco para no cambiar")

            nuevo_nombre = input("Nuevo nombre: ").strip()
            if nuevo_nombre:
                contacto["nombre"] = nuevo_nombre

            nuevo_telefono = input("Nuevo teléfono: ").strip()
            if nuevo_telefono:
                contacto["telefono"] = nuevo_telefono

            nuevo_email = input("Nuevo email: ").strip()
            if nuevo_email:
                contacto["email"] = nuevo_email

            print("✓ Contacto actualizado")
            return

    print("No encontrado")


def guardar_contactos(contactos):
    """Guarda contactos en un archivo"""
    try:
        with open("contactos.txt", "w", encoding="utf-8") as f:
            for contacto in contactos:
                f.write(
                    f"{contacto['nombre']}|{contacto['telefono']}|{contacto['email']}\n"
                )
        print("✓ Contactos guardados")
    except Exception as e:
        print(f"Error al guardar: {e}")


def cargar_contactos():
    """Carga contactos de un archivo"""
    try:
        contactos = []
        with open("contactos.txt", "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 3:
                    contacto = {
                        "nombre": partes[0],
                        "telefono": partes[1],
                        "email": partes[2],
                    }
                    contactos.append(contacto)
        return contactos
    except FileNotFoundError:
        return []


def main():
    """Programa principal"""
    contactos = cargar_contactos()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            ver_contactos(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            editar_contacto(contactos)
        elif opcion == "6":
            guardar_contactos(contactos)
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
