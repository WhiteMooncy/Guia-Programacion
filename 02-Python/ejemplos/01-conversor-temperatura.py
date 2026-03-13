"""
Conversor de Temperaturas
Convierte entre Celsius, Fahrenheit y Kelvin
"""


def celsius_a_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit"""
    return (celsius * 9 / 5) + 32


def celsius_a_kelvin(celsius):
    """Convierte Celsius a Kelvin"""
    return celsius + 273.15


def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius"""
    return (fahrenheit - 32) * 5 / 9


def kelvin_a_celsius(kelvin):
    """Convierte Kelvin a Celsius"""
    return kelvin - 273.15


def menu():
    """Muestra el menú de opciones"""
    print("\n=== CONVERSOR DE TEMPERATURAS ===")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Kelvin a Celsius")
    print("5. Salir")
    return input("Elige opción (1-5): ")


def main():
    """Programa principal"""
    while True:
        opcion = menu()

        if opcion == "1":
            celsius = float(input("Ingresa grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")

        elif opcion == "2":
            celsius = float(input("Ingresa grados Celsius: "))
            kelvin = celsius_a_kelvin(celsius)
            print(f"{celsius}°C = {kelvin:.2f}K")

        elif opcion == "3":
            fahrenheit = float(input("Ingresa grados Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius:.2f}°C")

        elif opcion == "4":
            kelvin = float(input("Ingresa Kelvin: "))
            celsius = kelvin_a_celsius(kelvin)
            print(f"{kelvin}K = {celsius:.2f}°C")

        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
