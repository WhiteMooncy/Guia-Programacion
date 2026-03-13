# 🟢 Fase 2: Python Fundamentals

**Duración:** 4-6 semanas  
**Nivel:** Principiante  
**Objetivo:** Dominar los fundamentos de Python y programación

---

## 📚 Tabla de Contenidos

1. [Instalación](#instalación)
2. [¿Por qué Python?](#por-qué-python)
3. [Primeros Pasos](#primeros-pasos)
4. [Conceptos Fundamentales](#conceptos-fundamentales)
5. [Ejemplos](#ejemplos)
6. [Ejercicios](#ejercicios)

---

## ✅ Instalación

### Windows / Mac / Linux

1. Visita: https://www.python.org
2. Descarga Python 3.11 o superior
3. **IMPORTANTE:** Marca "Add Python to PATH"
4. Instala

### Verificar Instalación

Abre terminal y ejecuta:

```bash
python --version
```

Deberías ver algo como: `Python 3.11.0`

---

## 💡 ¿Por qué Python?

✅ **Sintaxis simple** - Código limpio y legible  
✅ **Versátil** - Web, datos, IA, automatización  
✅ **Demanda laboral** - Uno de los más buscados  
✅ **Comunidad** - Enorme soporte online  
✅ **Librerías** - Miles disponibles

---

## 🚀 Primeros Pasos

### 1. Crear un Archivo .py

Crea `hola_mundo.py`:

```python
print("Hola, mundo!")
```

### 2. Ejecutar en Terminal

```bash
python hola_mundo.py
```

**Resultado:**

```
Hola, mundo!
```

---

## 💻 Conceptos Fundamentales

### 1. Variables y Tipos de Datos

```python
# Strings (texto)
nombre = "Juan"
apellido = 'García'

# Números enteros
edad = 25
año = 2026

# Números flotantes (decimales)
altura = 1.75
peso = 70.5

# Booleanos (verdadero/falso)
es_estudiante = True
tiene_coche = False

# Imprimir variables
print(nombre)
print(f"Tengo {edad} años")  # f-string (recomendado)
```

---

### 2. Tipos de Datos Complejos

#### Listas

```python
# Crear lista
frutas = ["manzana", "plátano", "naranja"]
numeros = [1, 2, 3, 4, 5]

# Acceder a elementos
print(frutas[0])      # manzana
print(frutas[-1])     # naranja (último)

# Modificar
frutas[1] = "fresa"

# Agregar
frutas.append("kiwi")

# Remover
frutas.remove("manzana")

# Longitud
print(len(frutas))    # 3
```

#### Tuplas (inmutables)

```python
# No se pueden modificar
coordenadas = (10, 20)
print(coordenadas[0])  # 10
```

#### Diccionarios

```python
# Clave: valor
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceder
print(persona["nombre"])      # Juan
print(persona.get("edad"))    # 25

# Agregar
persona["profesión"] = "Programador"

# Iterar
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

#### Sets (sin duplicados)

```python
numeros = {1, 2, 3, 3, 4}
print(numeros)  # {1, 2, 3, 4} (sin duplicado 3)
```

---

### 3. Operadores

```python
# Aritméticos
print(10 + 5)    # 15
print(10 - 5)    # 5
print(10 * 5)    # 50
print(10 / 5)    # 2.0
print(10 // 3)   # 3 (división entera)
print(10 % 3)    # 1 (módulo/resto)
print(2 ** 3)    # 8 (exponente)

# Comparación
print(10 > 5)    # True
print(10 < 5)    # False
print(10 >= 10)  # True
print(10 == 10)  # True
print(10 != 5)   # True

# Lógicos
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
```

---

### 4. Control de Flujo

#### Condicionales

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")

# Operador ternario
estado = "Adulto" if edad >= 18 else "Menor"
print(estado)
```

#### Bucles FOR

```python
# Rango
for i in range(1, 6):  # 1 a 5
    print(i)

# Lista
frutas = ["manzana", "plátano", "naranja"]
for fruta in frutas:
    print(fruta)

# Con índice
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
```

#### Bucles WHILE

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

#### Control de Bucles

```python
for i in range(10):
    if i == 5:
        break       # Salir del bucle
    if i == 2:
        continue    # Saltarse esta iteración
    print(i)        # Imprime: 0, 1, 3, 4
```

---

### 5. Funciones

```python
# Función simple
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Juan")

# Función con retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # 8

# Parámetros por defecto
def presentar(nombre, edad=25):
    print(f"{nombre} tiene {edad} años")

presentar("María")          # Usa edad=25
presentar("Carlos", 30)     # Cambia edad

# Múltiples retornos
def obtener_datos():
    return "Juan", 25

nombre, edad = obtener_datos()

# *args - número variable de argumentos
def suma_variable(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(suma_variable(1, 2, 3, 4, 5))  # 15

# **kwargs - argumentos nombrados
def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

imprimir_datos(nombre="Juan", edad=25, ciudad="Madrid")
```

---

### 6. Manejo de Excepciones

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Debes ingresar un número válido")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print("Cálculo exitoso")
finally:
    print("Operación finalizada")
```

---

### 7. Trabajar con Archivos

```python
# Leer archivo
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# Escribir archivo
with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, esto es una prueba\n")
    archivo.write("Segunda línea\n")

# Agregar a archivo
with open("archivo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Línea adicional\n")

# Leer línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```

---

## 💻 Ejemplos Completos

### Ejemplo 1: Conversor de Temperaturas

Ver: [`ejemplos/01-conversor-temperatura.py`](ejemplos/01-conversor-temperatura.py)

```python
# Conversor de Celsius a Fahrenheit
celsius = float(input("Ingresa grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

---

### Ejemplo 2: Lista de Tareas

Ver: [`ejemplos/02-lista-tareas.py`](ejemplos/02-lista-tareas.py)

```python
tareas = []

while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige opción: ")

    if opcion == "1":
        tarea = input("Nueva tarea: ")
        tareas.append(tarea)
    elif opcion == "2":
        if tareas:
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas")
    elif opcion == "3":
        if tareas:
            num = int(input("Número de tarea a eliminar: "))
            tareas.pop(num - 1)
    elif opcion == "4":
        break
```

---

### Ejemplo 3: Juego de Adivinanza

Ver: [`ejemplos/03-juego-adivinanza.py`](ejemplos/03-juego-adivinanza.py)

```python
import random

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("Adivina el número entre 1 y 100")

while not adivinado:
    intento = int(input("Tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("El número es mayor")
    elif intento > numero_secreto:
        print("El número es menor")
    else:
        print(f"¡Ganaste en {intentos} intentos!")
        adivinado = True
```

---

## 🎯 Ejercicios

### Nivel Básico ⭐

1. **Calculadora**
    - Suma, resta, multiplicación, división
2. **Validador de Contraseña**
    - Mínimo 8 caracteres
    - Al menos una mayúscula
    - Al menos un número

3. **Promedio de Notas**
    - Lee 5 notas
    - Calcula promedio

### Nivel Intermedio ⭐⭐

4. **Contador de Palabras**
    - Lee un archivo
    - Cuenta palabras
    - Muestra palabras más frecuentes

5. **Sistema de Calificaciones**
    - Almacena estudiantes y notas
    - Calcula promedios
    - Busca estudiantes

6. **Generador de Tablas de Multiplicar**
    - Lee número
    - Genera su tabla
    - Guarda en archivo

---

## 📖 Estructura Recomendada

**Semana 1-2:** Tipos de datos, operadores, condicionales  
**Semana 2-3:** Bucles, funciones  
**Semana 3-4:** Listas y diccionarios  
**Semana 4-5:** Excepciones y archivos  
**Semana 5-6:** Proyectos integradores

---

**¿Listo para la siguiente fase?** 👉 [Fase 3: OOP](../03-OOP/README.md)
