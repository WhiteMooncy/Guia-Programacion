"""
Juego de Adivinanza
Adivina el número secreto entre 1 y 100
"""

import random


def jugar():
    """Ejecuta el juego"""
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    intentos_lista = []

    print("=" * 40)
    print("ADIVINA EL NÚMERO")
    print("Tengo un número entre 1 y 100")
    print("¿Puedes adivinarlo?")
    print("=" * 40)

    while not adivinado:
        try:
            intento = int(input("\nTu intento: "))

            # Validar rango
            if intento < 1 or intento > 100:
                print("⚠ El número debe estar entre 1 y 100")
                continue

            intentos += 1
            intentos_lista.append(intento)

            # Comparar
            if intento < numero_secreto:
                print("📈 El número es MAYOR")
                diferencia = numero_secreto - intento
                if diferencia > 10:
                    print("   (Mucho mayor)")
            elif intento > numero_secreto:
                print("📉 El número es MENOR")
                diferencia = intento - numero_secreto
                if diferencia > 10:
                    print("   (Mucho menor)")
            else:
                print("\n🎉 ¡GANASTE! 🎉")
                print(f"El número era: {numero_secreto}")
                print(f"Intentos: {intentos}")
                print(f"Tus intentos: {intentos_lista}")
                adivinado = True

                # Evaluar desempeño
                if intentos <= 5:
                    print("🏆 ¡Excelente!")
                elif intentos <= 10:
                    print("👍 ¡Muy bien!")
                else:
                    print("📚 Próxima vez mejor")

        except ValueError:
            print("⚠ Debes ingresar un número válido")


def menu_principal():
    """Menú principal"""
    while True:
        print("\n" + "=" * 40)
        print("JUEGO DE ADIVINANZA")
        print("=" * 40)
        print("1. Jugar")
        print("2. Instrucciones")
        print("3. Salir")

        opcion = input("Elige opción (1-3): ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("\nINSTRUCCIONES:")
            print("1. Yo pienso un número entre 1 y 100")
            print("2. Tú intentas adivinarlo")
            print("3. Yo te digo si es mayor o menor")
            print("4. ¡Ganas cuando aciertas!")
        elif opcion == "3":
            print("\n¡Gracias por jugar! 👋")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu_principal()
