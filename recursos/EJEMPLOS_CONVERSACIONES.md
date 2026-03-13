# 🎓 Ejemplos Reales: Aprende Usando Claude

> **Conversaciones reales con Claude desde Fase 1 hasta proyectos complejos.**

---

## 📚 Ejemplo 1: Concepto Básico (Fase 1-2)

### Contexto

El estudiante está en Fase 2, acaba de aprender listas y se confunde con diccionarios.

### Conversación

#### 🧑 ESTUDIANTE

```
Hola, estoy en Fase 2 aprendiendo Python.

Vi diccionarios en ejemplos pero no entiendo
la diferencia con listas.

Tengo esto:

LISTA:
datos = ["Juan", 25, "Carlos", 30]

DICCIONARIO:
datos = {"Juan": 25, "Carlos": 30}

¿Por qué usar uno o el otro?
¿Cómo acceso los datos?

Soy principiante.
```

#### 🤖 CLAUDE

```
¡Excelente pregunta! Es confuso al principio.

ANALOGÍA SIMPLE:

Lista = Carrito de compras
- Orden importa: [manzana, leche, pan]
- Posición: elemento 0 es manzana
- Accedes por NÚMERO: carrito[0]

Diccionario = Directorio telefónico
- Nombre → Teléfono
- {"Juan": 1234, "María": 5678}
- Accedes por NOMBRE: directorio["Juan"]

CÓDIGO - LISTAS:

persona = ["Juan", 25, "Ingeniero", "Madrid"]
print(persona[0])  # "Juan"
print(persona[1])  # 25

¿Problema? Si cambias el orden, todo falla.

CÓDIGO - DICCIONARIOS:

persona = {
    "nombre": "Juan",
    "edad": 25,
    "profesión": "Ingeniero",
    "ciudad": "Madrid"
}
print(persona["nombre"])  # "Juan"
print(persona["edad"])    # 25

¿Ventaja? Orden no importa, es claro qué es qué.

CUÁNDO USAR CADA UNA:

Usa LISTA cuando:
- Orden importa (1er, 2do, 3er lugar)
- Datos del mismo tipo
- Ej: [1, 2, 3, 4, 5] (números)
- Ej: ["rojo", "azul", "verde"] (colores)

Usa DICCIONARIO cuando:
- Datos tienen etiquetas
- Búsqueda rápida
- Ej: {"edad": 25, "nombre": "Juan"}
- Ej: {"usuario": "carlos", "contraseña": "123"}

EJEMPLO PRÁCTICO - LISTA:

calificaciones = [8, 9, 7, 10]  # 4 estudiantes
print(calificaciones[0])  # Primera nota: 8
print(calificaciones[3])  # Cuarta nota: 10

EJEMPLO PRÁCTICO - DICCIONARIO:

calificaciones = {
    "María": 8,
    "Carlos": 9,
    "Juan": 7,
    "Ana": 10
}
print(calificaciones["María"])  # 8
print(calificaciones["Juan"])   # 7

¿VES LA DIFERENCIA?

Con lista: Solo sé que es 8, ¿de quién?
Con diccionario: Sé que María tiene 8.

COMBINAR AMBAS:

# Lista de diccionarios = PODEROSO
estudiantes = [
    {"nombre": "María", "edad": 20, "nota": 8},
    {"nombre": "Carlos", "edad": 21, "nota": 9},
    {"nombre": "Juan", "edad": 19, "nota": 7}
]

print(estudiantes[0])  # {"nombre": "María", ...}
print(estudiantes[0]["nombre"])  # "María"
print(estudiantes[1]["nota"])  # 9
```

#### 🧑 ESTUDIANTE

```
¡Ahora lo entiendo! Una pregunta:

¿Cómo itero (recorro) un diccionario?
Con listas uso: for x in lista

¿Con diccionarios?
```

#### 🤖 CLAUDE

```
¡Buena pregunta de seguimiento!

RECORRER DICCIONARIO:

# OPCIÓN 1: Solo las claves (llaves)
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

for clave in diccionario:
    print(clave)

RESULTADO:
nombre
edad
ciudad

# OPCIÓN 2: Clave y valor (mejor)
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

RESULTADO:
nombre: Juan
edad: 25
ciudad: Madrid

# OPCIÓN 3: Solo valores
for valor in diccionario.values():
    print(valor)

RESULTADO:
Juan
25
Madrid

EJEMPLO PRÁCTICO:

notas = {
    "María": 8,
    "Carlos": 9,
    "Juan": 7
}

print("Mostrar todos:")
for nombre, nota in notas.items():
    print(f"{nombre} tiene nota {nota}")

RESULTADO:
María tiene nota 8
Carlos tiene nota 9
Juan tiene nota 7

RECORRER LISTA DE DICCIONARIOS:

estudiantes = [
    {"nombre": "María", "nota": 8},
    {"nombre": "Carlos", "nota": 9},
    {"nombre": "Juan", "nota": 7}
]

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    nota = estudiante["nota"]
    print(f"{nombre}: {nota}")

O más corto:

for est in estudiantes:
    print(f"{est['nombre']}: {est['nota']}")
```

---

## 💻 Ejemplo 2: Generar Código (Fase 2)

### Contexto

El estudiante quiere crear una función para validar contraseña.

### Conversación

#### 🧑 ESTUDIANTE

```
Soy Fase 2 (intermedio).

Necesito una función en Python que valide contraseñas.

Requisitos:
- Mínimo 8 caracteres
- Al menos 1 mayúscula
- Al menos 1 número
- Al menos 1 símbolo (!@#$%^&*)

Si es válida: True
Si no: False

¿Puedes ayudarme?
```

#### 🤖 CLAUDE

```
¡Claro! Aquí va:

def validar_contraseña(contraseña):
    """
    Valida si una contraseña cumple requisitos

    Args:
        contraseña (str): Contraseña a validar

    Returns:
        bool: True si es válida, False si no
    """

    # REQUISITO 1: Mínimo 8 caracteres
    if len(contraseña) < 8:
        return False

    # REQUISITO 2: Al menos 1 mayúscula
    tiene_mayuscula = False
    for caracter in contraseña:
        if caracter.isupper():  # ¿Es mayúscula?
            tiene_mayuscula = True
            break

    if not tiene_mayuscula:
        return False

    # REQUISITO 3: Al menos 1 número
    tiene_numero = False
    for caracter in contraseña:
        if caracter.isdigit():  # ¿Es número?
            tiene_numero = True
            break

    if not tiene_numero:
        return False

    # REQUISITO 4: Al menos 1 símbolo
    simbolos = "!@#$%^&*"
    tiene_simbolo = False
    for caracter in contraseña:
        if caracter in simbolos:
            tiene_simbolo = True
            break

    if not tiene_simbolo:
        return False

    # Si llegó aquí, cumple todo
    return True


# EJEMPLOS DE USO:

print(validar_contraseña("Abc123!"))      # False (7 caracteres)
print(validar_contraseña("Abc1234!"))     # True ✓
print(validar_contraseña("abc1234!"))     # False (sin mayúscula)
print(validar_contraseña("ABC12345"))     # False (sin símbolo)
print(validar_contraseña("Abcdefgh!"))    # False (sin número)
```

#### 🧑 ESTUDIANTE

```
¿Hay forma más corta? Tu código es muy largo.
```

#### 🤖 CLAUDE

```
¡Sí! Con funciones incorporadas es más corto:

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    tiene_simbolo = any(c in "!@#$%^&*" for c in contraseña)

    return tiene_mayuscula and tiene_numero and tiene_simbolo


# O INCLUSO MÁS CORTA (avanzado):

def validar_contraseña(pwd):
    return (
        len(pwd) >= 8 and
        any(c.isupper() for c in pwd) and
        any(c.isdigit() for c in pwd) and
        any(c in "!@#$%^&*" for c in pwd)
    )

EXPLICACIÓN DE LA VERSIÓN CORTA:

any(c.isupper() for c in pwd)
= "¿hay algún carácter que sea mayúscula?"

and = todas las condiciones deben ser True

Es la misma lógica, solo más compacta.

CUÁNDO USARLA:

Para aprender: Usa versión larga
Para producción: Usa versión corta
```

---

## 🐛 Ejemplo 3: Debugging (Fase 2)

### Contexto

El estudiante tiene código que falla y no sabe por qué.

### Conversación

#### 🧑 ESTUDIANTE

```
Tengo un error y no sé qué está mal.

Error:
Traceback (most recent call last):
  File "programa.py", line 15, in <module>
    print(resultado[0])
TypeError: 'NoneType' object is not subscriptable

Mi código:
def obtener_numeros(texto):
    numeros = []
    for caracter in texto:
        if caracter.isdigit():
            numeros.append(caracter)

resultado = obtener_numeros("Hola123")
print(resultado[0])

¿Qué está mal? No retorno None, ¿verdad?
```

#### 🤖 CLAUDE

```
Buena observación. El problema es SUTIL:

Tu función SÍ retorna numeros (la lista).
PERO, Python retorna None si no hay return explícito.

PROBLEMA DETECTADO:

def obtener_numeros(texto):
    numeros = []
    for caracter in texto:
        if caracter.isdigit():
            numeros.append(caracter)
    # ← FALTA: return numeros

Cuando la función termina sin return, retorna None.

SOLUCIÓN:

def obtener_numeros(texto):
    numeros = []
    for caracter in texto:
        if caracter.isdigit():
            numeros.append(caracter)
    return numeros  # ← AGREGADO

resultado = obtener_numeros("Hola123")
print(resultado)      # ['1', '2', '3']
print(resultado[0])   # '1'

POR QUÉ ESE ERROR:

TypeError: 'NoneType' object is not subscriptable

= Intentas hacer resultado[0]
  pero resultado es None
  y None no tiene índices (no es lista)

LECCIÓN:

Siempre que una función debe retornar algo,
asegúrate de tener return.
```

#### 🧑 ESTUDIANTE

```
Entendido. Pero tengo otra duda:

¿Por qué resultado = ["1", "2", "3"] en lugar de [1, 2, 3]?

Quiero números, no strings.
```

#### 🤖 CLAUDE

```
¡Excelente observación!

PROBLEMA:

caracter.isdigit()
isdigit() devuelve True/False si es dígito

PERO caracter es string "1", no número 1

SOLUCIÓN:

def obtener_numeros(texto):
    numeros = []
    for caracter in texto:
        if caracter.isdigit():
            numeros.append(int(caracter))  # ← CONVERTIR A INT
    return numeros

resultado = obtener_numeros("Hola123")
print(resultado)      # [1, 2, 3]
print(resultado[0])   # 1
print(type(resultado[0]))  # <class 'int'>

MEJOR AÚN (más Pythonic):

def obtener_numeros(texto):
    return [int(c) for c in texto if c.isdigit()]

MÁS CORTA Y CLARA
```

---

## 🚀 Ejemplo 4: Proyecto Pequeño (Fase 2-3)

### Contexto

El estudiante quiere crear su primer "proyecto real".

### Conversación

#### 🧑 ESTUDIANTE

```
Estoy en Fase 2, casi en Fase 3 (OOP).

Quiero hacer un proyecto pequeño que sea ÚTIL.

Idea: Contador de palabras de un archivo

El programa debe:
1. Pedir nombre del archivo
2. Leer el archivo
3. Contar palabras totales
4. Contar líneas
5. Contar caracteres
6. Mostrar palabra más repetida
7. Guardar resultados en archivo salida

¿Cómo lo estructura? ¿Por dónde empiezo?

Nivel: Intermedio (Fase 2 casi completo)
```

#### 🤖 CLAUDE

```
¡Excelente proyecto! Es práctico y tiene desafíos.

ESTRUCTURA GENERAL:

1. FUNCIONES necesarias:
   - leer_archivo(nombre)
   - contar_palabras(texto)
   - contar_lineas(texto)
   - palabra_mas_repetida(texto)
   - guardar_resultados(resultados, archivo)

2. FLUJO PRINCIPAL:
   - Solicitar nombre archivo
   - Leer archivo
   - Calcular estadísticas
   - Mostrar resultados
   - Guardar resultados

3. MANEJO DE ERRORES:
   - ¿Existe el archivo?
   - ¿Archivo está vacío?
   - ¿Permisos para escribir salida?

VAMOS POR PASOS:

PASO 1 - Leer archivo:

def leer_archivo(nombre):
    try:
        with open(nombre, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"Error: No existe '{nombre}'")
        return None
    except Exception as e:
        print(f"Error al leer: {e}")
        return None

PASO 2 - Contar palabras y líneas:

def analizar_texto(texto):
    palabras = texto.split()  # ['palabra1', 'palabra2', ...]
    lineas = texto.split('\n')
    caracteres = len(texto)

    return {
        'palabras': len(palabras),
        'lineas': len(lineas),
        'caracteres': caracteres
    }

PASO 3 - Palabra más repetida:

def palabra_mas_repetida(texto):
    palabras = texto.lower().split()

    # Contar repeticiones
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    # Encontrar máxima
    if contador:
        mas_repetida = max(contador, key=contador.get)
        repeticiones = contador[mas_repetida]
        return (mas_repetida, repeticiones)
    return (None, 0)

PASO 4 - Guardar resultados:

def guardar_resultados(resultados, archivo_salida):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write("=== ANÁLISIS DE TEXTO ===\n")
            archivo.write(f"Palabras: {resultados['palabras']}\n")
            archivo.write(f"Líneas: {resultados['lineas']}\n")
            archivo.write(f"Caracteres: {resultados['caracteres']}\n")
            archivo.write(f"Palabra más repetida: {resultados['palabra_mas_frecuente'][0]} ")
            archivo.write(f"({resultados['palabra_mas_frecuente'][1]} veces)\n")
        print("✓ Resultados guardados")
    except Exception as e:
        print(f"Error al guardar: {e}")

PASO 5 - Programa principal:

def main():
    nombre_entrada = input("Archivo a analizar: ")

    # Leer
    contenido = leer_archivo(nombre_entrada)
    if contenido is None:
        return

    # Analizar
    stats = analizar_texto(contenido)
    palabra, repeticiones = palabra_mas_repetida(contenido)

    stats['palabra_mas_frecuente'] = (palabra, repeticiones)

    # Mostrar
    print("\n=== RESULTADOS ===")
    print(f"Palabras: {stats['palabras']}")
    print(f"Líneas: {stats['lineas']}")
    print(f"Caracteres: {stats['caracteres']}")
    print(f"Palabra más repetida: {palabra} ({repeticiones} veces)")

    # Guardar
    archivo_salida = input("Archivo salida: ")
    guardar_resultados(stats, archivo_salida)

if __name__ == "__main__":
    main()
```

#### 🧑 ESTUDIANTE

```
Wow, eso es mucho. ¿Puedo separarlo en archivos?

Y... ¿Hay forma de hacerlo más simple al principio?
```

#### 🤖 CLAUDE

```
¡SÍ! Empecemos simple:

VERSIÓN FÁCIL (solo lo esencial):

contenido = open("archivo.txt").read()

palabras = contenido.split()
print(f"Total: {len(palabras)} palabras")

VERSIÓN INTERMEDIA (agregando funciones):

def leer(nombre):
    return open(nombre).read()

def contar(texto):
    return len(texto.split())

contenido = leer("archivo.txt")
total = contar(contenido)
print(f"Total: {total}")

VERSIÓN AVANZADA (con manejo de errores):

def leer(nombre):
    try:
        return open(nombre).read()
    except FileNotFoundError:
        print("Archivo no existe")
        return None

if leer("archivo.txt"):
    contenido = leer("archivo.txt")
    total = len(contenido.split())
    print(f"Total: {total}")

SEPARAR EN ARCHIVOS (Fase 3):

main.py:
    from funciones import *

    archivo = input("¿Cuál?")
    contenido = leer(archivo)
    print(len(contenido.split()))

funciones.py:
    def leer(nombre):
        return open(nombre).read()

RECOMENDACIÓN:

1. Haz versión SIMPLE primero (funciona)
2. Agrega manejo de errores
3. Extrae a funciones
4. Luego separa en archivos

No intentes todo a la vez.
```

---

## 📌 Plantilla: Cómo Debes Comunicarte

```
Nombre: [Tu nombre]
Nivel: [Fase 1/2/3/4]
Objetivo: [Qué quieres hacer]

Contexto:
- Llevo aprendiendo: [cuánto tiempo]
- Sé: [qué ya dominas]
- No entiendo: [área específica]

Pregunta:
[Tu pregunta específica]

He intentado:
[Lo que ya probaste]

Necesito:
☐ Explicación del concepto
☐ Código de ejemplo
☐ Debuggear mi código
☐ Mejorar mi código
☐ Estructura de proyecto
☐ Otra: [especifica]
```

---

**¡Ahora tienes ejemplos reales para aprender!** 🎓
