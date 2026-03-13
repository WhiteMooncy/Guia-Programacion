# 🚀 Guía de Aprendizaje: De Cero a Programador

Una ruta de aprendizaje progresiva para dominar programación desde lógica básica hasta desarrollo profesional.

---

## 📊 Roadmap General

```
Fase 1: Lógica Básica (Pseint) → 2-3 semanas
    ↓
Fase 2: Python Fundamentals → 4-6 semanas
    ↓
Fase 3: Programación Orientada a Objetos (POO) → 3-4 semanas
    ↓
Fase 4: Especialización (Frontend/Backend/Datos)
    ├─ Backend: JavaScript/Node.js → SQL → Bases de Datos
    ├─ Frontend: HTML/CSS/JavaScript → React
    └─ Datos: Pandas/NumPy → Machine Learning
```

---

# FASE 1: LÓGICA BÁSICA (Pseint)

## ¿Qué es Pseint?

Herramienta para escribir **pseudocódigo** en español. Perfecto para aprender lógica sin preocuparse por la sintaxis de un lenguaje real.

### Instalación

- **Descargar:** https://pseint.sourceforge.net/
- **Plataforma:** Windows, Linux, Mac
- **Costo:** Gratuito

### Conceptos Clave

#### 1. Variables y Tipos de Datos

```pseudocode
Algoritmo Programa
    // Declarar variables
    Definir nombre Como Texto
    Definir edad Como Entero
    Definir altura Como Real
    Definir activo Como Logico

    // Asignar valores
    nombre <- "Juan"
    edad <- 25
    altura <- 1.75
    activo <- Verdadero

    Escribir "Nombre:", nombre
    Escribir "Edad:", edad
FinAlgoritmo
```

#### 2. Operadores Básicos

```pseudocode
Algoritmo Operadores
    Definir a, b Como Entero
    a <- 10
    b <- 3

    // Aritméticos
    Escribir "Suma:", a + b          // 13
    Escribir "Resta:", a - b         // 7
    Escribir "Multiplicación:", a * b // 30
    Escribir "División:", a / b      // 3.33
    Escribir "Módulo:", a MOD b      // 1

    // Comparación
    Escribir a > b                   // Verdadero
    Escribir a == b                  // Falso

    // Lógicos
    Escribir Verdadero Y Falso       // Falso
    Escribir Verdadero O Falso       // Verdadero
    Escribir NO Verdadero            // Falso
FinAlgoritmo
```

#### 3. Condicionales

```pseudocode
Algoritmo CondicionalSi
    Definir calificacion Como Entero
    calificacion <- 75

    Si calificacion >= 90 Entonces
        Escribir "Excelente"
    SiNo Si calificacion >= 70 Entonces
        Escribir "Bueno"
    SiNo Si calificacion >= 60 Entonces
        Escribir "Aprobado"
    SiNo
        Escribir "Reprobado"
    FinSi
FinAlgoritmo
```

#### 4. Bucles

```pseudocode
Algoritmo Bucles
    Definir i, suma Como Entero
    suma <- 0

    // FOR: Contar del 1 al 10
    Para i <- 1 Hasta 10 Hacer
        suma <- suma + i
    FinPara
    Escribir "Suma del 1 al 10:", suma

    // MIENTRAS: Mientras se cumpla condición
    i <- 1
    Mientras i <= 5 Hacer
        Escribir "Número:", i
        i <- i + 1
    FinMientras
FinAlgoritmo
```

#### 5. Funciones/Procedimientos

```pseudocode
Función saludar(nombre)
    Escribir "Hola, ", nombre
FinFunción

Función suma(a, b) Como Entero
    Retornar a + b
FinFunción

Algoritmo Principal
    saludar("Juan")
    Escribir "Resultado:", suma(5, 3)
FinAlgoritmo
```

### 🎯 Ejercicios Fase 1

#### Nivel Básico

1. **Conversor de Temperaturas** - Convertir Celsius a Fahrenheit
2. **Calculadora Básica** - Suma, resta, multiplicación, división
3. **Validador de Edad** - Verificar si es mayor de edad
4. **Tabla de Multiplicar** - Mostrar tabla de multiplicar del 1-10

#### Nivel Intermedio

5. **Número Mayor de Tres** - Encontrar el máximo entre 3 números
6. **Serie de Fibonacci** - Mostrar primeros N números
7. **Contador de Dígitos** - Contar cuántos dígitos tiene un número
8. **Palíndromo** - Verificar si un número es palíndromo

#### Nivel Avanzado

9. **Números Primos** - Encontrar primos hasta N
10. **Pirámide de Números** - Mostrar patrón piramidal

### 📚 Recursos

- **Documentación:** https://pseint.sourceforge.net/index.php
- **Tutoriales:** YouTube "Pseint tutorial español"
- **Práctica:** HackerRank (pseudocódigo conceptual)

### ⏱️ Duración Recomendada

- **Semana 1:** Variables y operadores (ejercicios 1-3)
- **Semana 2:** Condicionales y bucles (ejercicios 4-8)
- **Semana 3:** Funciones y problemas complejos (ejercicios 9-10)

---

# FASE 2: PYTHON FUNDAMENTALS

## ¿Por qué Python?

- **Sintaxis simple** - Fácil de aprender
- **Versátil** - Web, datos, IA, automatización
- **Demanda laboral** - Uno de los más buscados
- **Comunidad** - Enorme soporte online

### Instalación

```bash
# Descargar desde https://www.python.org
# Versión recomendada: 3.11+
# Marcar "Add Python to PATH"

# Verificar instalación
python --version
```

### Conceptos Clave

#### 1. Sintaxis Básica y Variables

```python
# Variables
nombre = "Juan"
edad = 25
altura = 1.75
activo = True

# Print
print("Hola", nombre)
print(f"Tengo {edad} años")  # f-string

# Input
nombre = input("¿Cuál es tu nombre? ")
```

#### 2. Tipos de Datos

```python
# Enteros
numero = 42

# Flotantes
pi = 3.14159

# Strings
mensaje = "Hola mundo"
mensaje_multilinea = """Línea 1
Línea 2
Línea 3"""

# Booleanos
verdadero = True
falso = False

# Listas
frutas = ["manzana", "plátano", "naranja"]
numeros = [1, 2, 3, 4, 5]

# Tuplas (inmutables)
coordenadas = (10, 20)

# Diccionarios
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Sets (sin duplicados)
numeros_unicos = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
```

#### 3. Operadores

```python
# Aritméticos
print(10 + 5)    # 15
print(10 - 5)    # 5
print(10 * 5)    # 50
print(10 / 5)    # 2.0
print(10 // 3)   # 3 (división entera)
print(10 % 3)    # 1 (módulo)
print(2 ** 3)    # 8 (exponente)

# Comparación
10 > 5       # True
10 == 10     # True
10 != 5      # True

# Lógicos
True and False   # False
True or False    # True
not True         # False
```

#### 4. Condicionales

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
```

#### 5. Bucles

```python
# FOR
for i in range(1, 6):  # 1 a 5
    print(i)

# FOR con lista
frutas = ["manzana", "plátano", "naranja"]
for fruta in frutas:
    print(fruta)

# WHILE
i = 0
while i < 5:
    print(i)
    i += 1

# Control de bucles
for i in range(10):
    if i == 5:
        break      # Salir del bucle
    if i == 2:
        continue   # Saltarse esta iteración
    print(i)
```

#### 6. Funciones

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

presentar("María")              # Usa edad=25
presentar("Carlos", edad=30)    # Cambia edad

# *args y **kwargs
def suma_variable(*numeros):
    return sum(numeros)

print(suma_variable(1, 2, 3, 4, 5))  # 15

def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

imprimir_datos(nombre="Juan", edad=25, ciudad="Madrid")
```

#### 7. Manejo de Listas

```python
numeros = [1, 2, 3, 4, 5]

# Acceso
print(numeros[0])      # 1
print(numeros[-1])     # 5 (último)

# Slicing
print(numeros[1:4])    # [2, 3, 4]
print(numeros[:3])     # [1, 2, 3]

# Métodos
numeros.append(6)       # Agregar
numeros.remove(3)       # Remover
numeros.sort()          # Ordenar
numeros.reverse()       # Invertir

# List comprehension
cuadrados = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

#### 8. Manejo de Diccionarios

```python
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceso
print(persona["nombre"])           # Juan
print(persona.get("edad"))         # 25
print(persona.get("país", "N/A"))  # N/A (valor por defecto)

# Agregar/Modificar
persona["teléfono"] = "123456789"
persona["edad"] = 26

# Iterar
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

#### 9. Manejo de Excepciones

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ValueError:
    print("Debes ingresar un número válido")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operación finalizada")
```

#### 10. Archivos

```python
# Leer archivo
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# Escribir archivo
with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, esto es una prueba\n")

# Agregar a archivo
with open("archivo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Línea adicional\n")
```

### 🎯 Ejercicios Fase 2

#### Nivel Básico

1. **Conversor de Temperatura** - Celsius a Fahrenheit
2. **Calculadora** - Con suma, resta, multiplicación, división
3. **Validador de Contraseña** - Verificar requisitos
4. **Promedio de Notas** - Calcular promedio de una lista

#### Nivel Intermedio

5. **Tabla de Multiplicar Interactiva** - Usuario elige número
6. **Fibonacci hasta N** - Mostrar serie
7. **Palabras Clave en Archivo** - Leer y contar palabras
8. **Juego de Adivinanza** - Adivinar número aleatorio

#### Nivel Avanzado

9. **Análisis de Datos** - Leer CSV, calcular estadísticas
10. **Sistema de Gestión de Contactos** - Crear, guardar, buscar

### 📚 Recursos

- **Documentación:** https://docs.python.org/3/
- **Tutorial Interactivo:** https://www.codecademy.com/learn/learn-python-3
- **Práctica:** https://www.codewars.com (Python)
- **Videotutoriales:** "Python para principiantes" en YouTube

### ⏱️ Duración Recomendada

- **Semana 1-2:** Tipos de datos y operadores
- **Semana 2-3:** Condicionales y bucles
- **Semana 3-4:** Funciones y listas
- **Semana 4-5:** Diccionarios y excepciones
- **Semana 5-6:** Archivos y proyectos

---

# FASE 3: ORIENTACIÓN A OBJETOS (OOP)

## Conceptos Clave

### 1. Clases y Objetos

```python
class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def cumpleaños(self):
        self.edad += 1

# Crear objeto
juan = Persona("Juan", 25)
juan.saludar()
juan.cumpleaños()
```

### 2. Herencia

```python
class Animal:
    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")

perro = Perro()
perro.hacer_sonido()  # Guau guau
```

### 3. Encapsulación

```python
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo())  # 1500
```

### 🎯 Ejercicios Fase 3

1. Sistema de Biblioteca - Gestionar libros y préstamos
2. Red Social Simple - Usuarios, publicaciones, seguidores
3. Tienda Online - Productos, carrito, facturación
4. Juego de Rol - Personajes, inventario, combate

### ⏱️ Duración Recomendada: 3-4 semanas

---

# FASE 4: ESPECIALIZACIÓN

Elige una ruta según intereses:

## 🔧 BACKEND (Recomendado para empezar)

### Paso 1: JavaScript/Node.js (1-2 meses)

- Sintaxis básica
- Asincronía (Promises, async/await)
- Express.js (framework web)

### Paso 2: Bases de Datos (2-3 semanas)

- **SQL Básico** (SELECT, INSERT, UPDATE, DELETE)
- **MongoDB** (bases de datos NoSQL)

### Paso 3: APIs REST (1 mes)

- Crear API con Express
- Autenticación (JWT)
- Despliegue (Heroku, Render)

### Recursos

- https://nodejs.org/
- https://www.sqlzoo.net/ (SQL interactivo)
- https://www.mongodb.com/

---

## 🎨 FRONTEND

### Paso 1: HTML/CSS (2-3 semanas)

- Estructura HTML5
- Estilos CSS3
- Responsive Design

### Paso 2: JavaScript Avanzado (3-4 semanas)

- DOM manipulation
- Eventos
- Fetch API

### Paso 3: React (4-6 semanas)

- Componentes
- State y Props
- Hooks

### Recursos

- https://developer.mozilla.org/
- https://react.dev/
- https://www.freecodecamp.org/

---

## 📊 DATOS E IA

### Paso 1: Librerías Python (2-3 semanas)

- NumPy (cálculos numéricos)
- Pandas (análisis de datos)
- Matplotlib (visualización)

### Paso 2: Machine Learning Básico (1 mes)

- Scikit-learn
- Conceptos: clasificación, regresión
- Datasets públicos

### Paso 3: Deep Learning (Opcional, avanzado)

- TensorFlow/Keras
- Redes neuronales

### Recursos

- https://numpy.org/
- https://pandas.pydata.org/
- https://www.kaggle.com/ (datasets)

---

# 📅 CRONOGRAMA RECOMENDADO

```
SEMANA 1-3:   Pseint (Lógica)
SEMANA 4-9:   Python Fundamentals
SEMANA 10-12: OOP en Python

MESES 4-5:    Especialización elegida (Backend/Frontend/Datos)
MESES 6+:     Proyectos reales
```

---

# 🎓 Consejos de Aprendizaje

1. **Practica diariamente** - 1-2 horas mínimo
2. **Haz proyectos pequeños** - No solo tutoriales
3. **Lee código de otros** - GitHub es tu amigo
4. **Entiende el "por qué"** - No memorices, comprende
5. **Únete a comunidades** - Stack Overflow, Discord, Reddit
6. **Resuelve problemas** - CodeWars, LeetCode, HackerRank
7. **Documenta tu código** - Comenta y explica
8. **No abandones si falla** - Los errores son aprendizaje

---

# 🛠️ Herramientas Recomendadas

| Herramienta    | Uso                  | Enlace                        |
| -------------- | -------------------- | ----------------------------- |
| VS Code        | Editor de código     | https://code.visualstudio.com |
| Git            | Control de versiones | https://git-scm.com           |
| GitHub         | Repositorios         | https://github.com            |
| Replit         | Código online        | https://replit.com            |
| Codepen        | Frontend             | https://codepen.io            |
| ChatGPT/Claude | Dudas                | https://chat.openai.com       |

---

# 📚 Proyectos Progresivos

### Nivel 1 (Pseint + Python Básico)

- Calculadora
- Lista de tareas
- Juego de adivinanza

### Nivel 2 (Python + OOP)

- Sistema de biblioteca
- Gestor de contactos
- Mini tienda online

### Nivel 3 (Backend)

- API REST de blog
- Sistema de usuarios
- Chat simple

### Nivel 4 (Full Stack)

- Red social básica
- E-commerce completo
- Aplicación de producción

---

# ✅ Checklist de Progreso

### Fase 1: Pseint

- [ ] Entiendo variables y tipos de datos
- [ ] Puedo escribir condicionales complejos
- [ ] Manejo bucles sin problemas
- [ ] Puedo crear funciones reutilizables
- [ ] Resuelvo problemas lógicos sin código real

### Fase 2: Python Fundamentals

- [ ] Domino sintaxis de Python
- [ ] Trabajo con listas y diccionarios
- [ ] Creo funciones modulares
- [ ] Manejo excepciones correctamente
- [ ] Leo y escribo archivos

### Fase 3: OOP

- [ ] Creo clases y objetos
- [ ] Entiendo herencia
- [ ] Implemento encapsulación
- [ ] Diseño arquitectura de clases

### Fase 4: Especialización

- [ ] Completo primeros proyectos
- [ ] Entiendo frameworks básicos
- [ ] Puedo crear proyectos reales
- [ ] Contribuyo a código open source

---

# 🤝 Contactos y Ayuda

Si tu amigo tiene dudas:

1. **Stack Overflow** - Pregunta específica
2. **Discord de programación** - Comunidad activa
3. **Reddit** - r/learnprogramming
4. **ChatGPT/Claude** - Explica conceptos
5. **Tutores online** - Si necesita ayuda personalizada

---

**¡Éxito en el aprendizaje! 🎉**

_Actualizado: Marzo 2026_
