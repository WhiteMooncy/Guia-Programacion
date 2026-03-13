# 🔵 Fase 1: Lógica Básica con Pseint

**Duración:** 2-3 semanas  
**Nivel:** Principiante  
**Objetivo:** Entender conceptos fundamentales de programación sin sintaxis complicada

---

## 📚 Tabla de Contenidos

1. [¿Qué es Pseint?](#qué-es-pseint)
2. [Instalación](#instalación)
3. [Conceptos Básicos](#conceptos-básicos)
4. [Ejemplos](#ejemplos)
5. [Ejercicios](#ejercicios)

---

## ¿Qué es Pseint?

**Pseint** es una herramienta educativa que permite escribir **pseudocódigo** (código en español casi natural) para entender lógica de programación sin preocuparte por la sintaxis complicada de lenguajes reales.

### Ventajas

✅ Sintaxis en español  
✅ Enfocado en lógica, no en sintaxis  
✅ Gratuito  
✅ Multiplataforma (Windows, Linux, Mac)  
✅ Interfaz amigable para principiantes

---

## 🔧 Instalación

### Windows / Linux / Mac

1. Visita: https://pseint.sourceforge.net/
2. Descarga la versión para tu sistema
3. Instala siguiendo los pasos
4. ¡Abre y comienza!

---

## 💡 Conceptos Básicos

### 1. Variables y Tipos de Datos

**Concepto:** Un lugar donde almacenar información.

```pseudocode
Algoritmo MiPrimerPrograma
    Definir nombre Como Texto
    Definir edad Como Entero
    Definir altura Como Real
    Definir es_estudiante Como Logico

    nombre <- "Juan"
    edad <- 25
    altura <- 1.75
    es_estudiante <- Verdadero

    Escribir "Nombre: ", nombre
    Escribir "Edad: ", edad
FinAlgoritmo
```

**Tipos de datos:**

- `Texto` - Palabras ("Hola", "Mundo")
- `Entero` - Números sin decimales (25, 100, -5)
- `Real` - Números con decimales (1.75, 3.14)
- `Lógico` - Verdadero o Falso

---

### 2. Operadores

#### Aritméticos

```pseudocode
Algoritmo Aritmetica
    Definir a, b Como Entero
    a <- 10
    b <- 3

    Escribir "Suma: ", a + b        // 13
    Escribir "Resta: ", a - b       // 7
    Escribir "Multiplicación: ", a * b  // 30
    Escribir "División: ", a / b    // 3.33
    Escribir "Módulo: ", a MOD b    // 1
    Escribir "Potencia: ", a ^ b    // 1000
FinAlgoritmo
```

#### Comparación

```pseudocode
10 > 5      // Verdadero (mayor que)
10 < 5      // Falso (menor que)
10 >= 10    // Verdadero (mayor o igual)
10 <= 5     // Falso (menor o igual)
10 == 10    // Verdadero (igual)
10 <> 5     // Verdadero (diferente)
```

#### Lógicos

```pseudocode
Verdadero Y Falso      // Falso (ambos deben ser verdaderos)
Verdadero O Falso      // Verdadero (al menos uno es verdadero)
NO Verdadero           // Falso (niega la expresión)
```

---

### 3. Entrada y Salida

```pseudocode
Algoritmo EntradaSalida
    Definir nombre Como Texto
    Definir edad Como Entero

    // Escribir en pantalla
    Escribir "¿Cuál es tu nombre?"

    // Leer desde teclado
    Leer nombre

    Escribir "¿Cuántos años tienes?"
    Leer edad

    // Mostrar resultado
    Escribir "Hola ", nombre, ", tienes ", edad, " años"
FinAlgoritmo
```

---

### 4. Condicionales (If/Else)

```pseudocode
Algoritmo ValidarEdad
    Definir edad Como Entero

    Escribir "Ingresa tu edad: "
    Leer edad

    Si edad >= 18 Entonces
        Escribir "Eres mayor de edad"
    SiNo Si edad >= 13 Entonces
        Escribir "Eres adolescente"
    SiNo
        Escribir "Eres niño"
    FinSi
FinAlgoritmo
```

---

### 5. Bucles (For y While)

#### For - Repetir N veces

```pseudocode
Algoritmo TablaMultiplicar
    Definir numero, i Como Entero

    Escribir "Tabla de multiplicar del: "
    Leer numero

    Para i <- 1 Hasta 10 Hacer
        Escribir numero, " x ", i, " = ", numero * i
    FinPara
FinAlgoritmo
```

#### While - Repetir mientras condición sea verdadera

```pseudocode
Algoritmo Contador
    Definir i Como Entero
    i <- 1

    Mientras i <= 10 Hacer
        Escribir i
        i <- i + 1
    FinMientras
FinAlgoritmo
```

---

### 6. Funciones

```pseudocode
// Función sin retorno
Función saludar(nombre)
    Escribir "Hola, ", nombre
FinFunción

// Función con retorno
Función suma(a, b) Como Entero
    Definir resultado Como Entero
    resultado <- a + b
    Retornar resultado
FinFunción

// Programa principal
Algoritmo Principal
    Definir respuesta Como Entero

    saludar("Juan")

    respuesta <- suma(5, 3)
    Escribir "Resultado: ", respuesta
FinAlgoritmo
```

---

## 💻 Ejemplos Completos

### Ejemplo 1: Conversor de Temperaturas

```pseudocode
Algoritmo ConvertirTemperatura
    Definir celsius, fahrenheit Como Real

    Escribir "Ingresa grados Celsius: "
    Leer celsius

    fahrenheit <- (celsius * 9/5) + 32

    Escribir celsius, "°C = ", fahrenheit, "°F"
FinAlgoritmo
```

**Ejecución:**

```
Ingresa grados Celsius: 0
0°C = 32°F
```

---

### Ejemplo 2: Número Mayor de Tres

```pseudocode
Algoritmo NumeroMayor
    Definir a, b, c, mayor Como Entero

    Escribir "Ingresa tres números: "
    Leer a, b, c

    mayor <- a

    Si b > mayor Entonces
        mayor <- b
    FinSi

    Si c > mayor Entonces
        mayor <- c
    FinSi

    Escribir "El número mayor es: ", mayor
FinAlgoritmo
```

---

### Ejemplo 3: Serie de Fibonacci

```pseudocode
Algoritmo Fibonacci
    Definir n, i, a, b, c Como Entero

    Escribir "¿Cuántos números de Fibonacci? "
    Leer n

    a <- 0
    b <- 1

    Para i <- 1 Hasta n Hacer
        Escribir a
        c <- a + b
        a <- b
        b <- c
    FinPara
FinAlgoritmo
```

---

## 🎯 Ejercicios

### Nivel Básico ⭐

1. **Calculadora Simple**
    - Lee dos números
    - Realiza suma, resta, multiplicación, división
    - Muestra resultados

2. **Conversor de Unidades**
    - Kilómetros a millas
    - Kilos a libras

3. **Validador de Mayoría de Edad**
    - Lee edad
    - Indica si es mayor o menor de edad

### Nivel Intermedio ⭐⭐

4. **Números Pares e Impares**
    - Lee N números
    - Cuenta cuántos son pares y cuántos impares

5. **Promedio de Calificaciones**
    - Lee 5 notas
    - Calcula promedio
    - Indica si aprobó (≥60)

6. **Tabla de Multiplicar**
    - Lee un número
    - Muestra su tabla de multiplicar del 1 al 10

### Nivel Avanzado ⭐⭐⭐

7. **Números Primos**
    - Lee un número
    - Determina si es primo

8. **Pirámide de Números**
    - Lee altura
    - Dibuja pirámide numérica

9. **Adivina el Número**
    - Programa piensa un número (1-100)
    - Usuario intenta adivinarlo
    - Indica si es mayor o menor

---

## 📖 Estructura Recomendada

**Semana 1:**

- Variables y tipos de datos
- Operadores básicos
- Entrada/salida
- Ejercicios 1-3

**Semana 2:**

- Condicionales
- Bucles
- Ejercicios 4-6

**Semana 3:**

- Funciones
- Problemas complejos
- Ejercicios 7-9

---

## 🔗 Recursos Adicionales

- **Documentación oficial:** https://pseint.sourceforge.net/
- **Tutorial YouTube:** Busca "Pseint tutorial español"
- **Comunidad:** Foros de programación educativa

---

**¿Listo para pasar a la siguiente fase?** 👉 [Fase 2: Python](../02-Python/README.md)
