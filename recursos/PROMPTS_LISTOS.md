# 🎯 Prompts Recomendados: Plantillas Listas para Usar

Copia y pega estas plantillas en Claude, reemplaza lo entre `[CORCHETES]`.

---

## 📚 APRENDIZAJE

### Plantilla 1: Entender un Concepto

```
Estoy en [FASE] del curso "Aprendizaje de Programación".

No entiendo bien: [CONCEPTO]

Por favor:
1. Explicación simple (como para un principiante)
2. Analogy o comparación con algo real
3. Ejemplo en [LENGUAJE]
4. ¿Cuándo y por qué usarlo?
5. Errores comunes
6. Alternativas o conceptos relacionados

Comenta mucho el código.
```

**Ejemplo práctico:**

```
Estoy en Fase 2 del curso.

No entiendo bien: Diccionarios

Por favor:
1. Explicación simple
2. Diferencia con listas
3. Ejemplo en Python
4. ¿Cuándo usarlos?
5. Errores comunes
6. Cuándo usar diccionario vs lista

Comenta mucho el código.
```

---

### Plantilla 2: Entender Código Complicado

```
No entiendo este código. Soy [NIVEL].

\`\`\`[LENGUAJE]
[PEGA EL CÓDIGO AQUÍ]
\`\`\`

Por favor explica:
1. ¿Qué hace en términos simples?
2. Cada línea/sección importante
3. ¿Por qué se implementa así?
4. Versión más simple (sin atajos)
5. Cuándo usar este patrón
6. Potenciales problemas

Sé muy detallado.
```

**Ejemplo:**

```
No entiendo este código. Soy principiante (Fase 2).

\`\`\`python
resultado = [x**2 for x in range(10) if x % 2 == 0]
\`\`\`

Por favor explica:
1. ¿Qué hace en términos simples?
2. Cada parte (x**2, for x in, if x % 2 == 0)
3. ¿Por qué corchetes?
4. Versión con for/append normal
5. Cuándo usar cada forma
6. Otros ejemplos similares

Sé muy detallado.
```

---

## 💻 GENERACIÓN DE CÓDIGO

### Plantilla 3: Generar Función Simple

```
Soy [NIVEL]. Necesito una función en [LENGUAJE].

Requisitos:
- [Qué debe hacer]
- Entrada: [parámetros]
- Salida: [qué retorna]

Ejemplos esperados:
- Input: [ejemplo]
- Output: [resultado esperado]

Requisitos adicionales:
- [Validaciones]
- [Manejo de errores]
- [Casos especiales]

Por favor:
1. Código comentado
2. Ejemplo de uso
3. Explicación de la lógica
4. Posibles mejoras
5. Casos extremos a considerar
```

**Ejemplo:**

```
Soy principiante (Fase 2). Necesito una función en Python.

Requisitos:
- Calcula el promedio de una lista de números
- Entrada: lista de números
- Salida: promedio (número)

Ejemplos:
- [10, 20, 30] → 20
- [5] → 5
- [] → manejo especial

Requisitos adicionales:
- Validar que sean números
- No crash si lista vacía
- Resultado con 2 decimales

Por favor:
1. Código comentado
2. Ejemplo de uso
3. Explicación de la lógica
4. Posibles mejoras
5. Casos extremos
```

---

### Plantilla 4: Generar Proyecto Pequeño

```
Soy [NIVEL]. Quiero crear [PROYECTO DESCRIPCIÓN].

Objetivos principales:
1. [Objetivo 1]
2. [Objetivo 2]
3. [Objetivo 3]

Características:
- [Feature 1]
- [Feature 2]
- [Feature 3]

Restricciones:
- Lenguaje: [LENGUAJE]
- Sin librerías externas (o [LISTA])
- [Otras restricciones]

Por favor proporciona:
1. Estructura general (qué módulos/funciones)
2. Paso a paso para implementar
3. Código para la primera parte
4. Cómo las partes se conectan
5. Cómo probar/usar

Comenta el código mucho.
```

**Ejemplo:**

```
Soy intermedio (Fase 2 completado). Quiero crear un gestor de tareas simple.

Objetivos:
1. Agregar tareas
2. Ver lista de tareas
3. Marcar como completadas
4. Eliminar tareas
5. Guardar en archivo

Características:
- Interfaz por menú (línea de comandos)
- Persistencia en archivo
- Validaciones básicas
- Puede guardar en archivo al salir

Restricciones:
- Lenguaje: Python
- Sin librerías externas
- Máximo 200 líneas

Por favor:
1. Estructura general (funciones necesarias)
2. Paso a paso
3. Código inicializador
4. Cómo guardamos datos
5. Cómo testeamos
```

---

## 🐛 DEBUGGING

### Plantilla 5: Mi Código No Funciona

```
Tengo un error. Soy [NIVEL].

Error exacto:
\`\`\`
[PEGA TODO EL ERROR AQUÍ]
\`\`\`

Mi código:
\`\`\`[LENGUAJE]
[PEGA EL CÓDIGO COMPLETO/RELEVANTE]
\`\`\`

Contexto:
- Qué intentaba hacer: [DESCRIPCIÓN]
- Lo que esperaba: [RESULTADO ESPERADO]
- Lo que pasó: [RESULTADO ACTUAL]
- ¿Dónde falla?: [LÍNEA/SECCIÓN]

Por favor:
1. ¿Cuál es el problema?
2. ¿Por qué ocurre?
3. Solución paso a paso
4. Código corregido
5. Cómo prevenirlo en el futuro

Soy principiante, explica simple.
```

**Ejemplo:**

```
Tengo un error. Soy principiante (Fase 2).

Error:
\`\`\`
TypeError: can only concatenate str (not "int") to str
\`\`\`

Mi código:
\`\`\`python
edad = input("¿Tu edad?")
print("En 10 años tendrás " + (edad + 10) + " años")
\`\`\`

Contexto:
- Intento sumar 10 años a la edad del usuario
- Esperaba: "En 10 años tendrás 35 años"
- Pasó: Error de tipos
- Falla en la línea del print

Por favor explica simple qué está mal y cómo lo arreglo.
```

---

### Plantilla 6: El Código Funciona Pero Quiero Mejorarlo

```
Mi código funciona pero creo que no es óptimo. Soy [NIVEL].

Mi código actual:
\`\`\`[LENGUAJE]
[CÓDIGO]
\`\`\`

¿Problemas?
- Lentitud
- Código repetido
- Difícil de leer
- Poco eficiente
- [OTRO]

Por favor:
1. Analiza el código
2. ¿Qué está bien?
3. ¿Qué podría mejorar?
4. Versión mejorada
5. Comparación (velocidad, claridad, etc.)
6. Cuándo usar cada versión

Explica técnicas nuevas si las uso.
```

---

## 📖 INVESTIGACIÓN Y CONCEPTOS

### Plantilla 7: Comparación de Conceptos

```
Estoy confundido entre dos conceptos. Soy [NIVEL].

Concepto A: [PRIMERO]
Concepto B: [SEGUNDO]

Por favor:
1. Definición de cada uno
2. Diferencias principales
3. ¿Cuándo usar cada uno?
4. Ejemplo con cada uno (código)
5. Ventajas y desventajas
6. Casos donde se mezclan/confunden

Usa ejemplos claros.
```

**Ejemplo:**

```
Estoy confundido. Soy intermedio (Fase 2).

Concepto A: Lista (list)
Concepto B: Diccionario (dict)

Por favor:
1. Definición de cada uno
2. Diferencias principales
3. ¿Cuándo usar cada uno?
4. Ejemplo con cada uno (Python)
5. Ventajas/desventajas
6. Casos donde se mezclan

Usa ejemplos claros.
```

---

### Plantilla 8: El Mejor Enfoque

```
Tengo un problema y varias formas de resolverlo. Soy [NIVEL].

Problema:
[DESCRIPCIÓN DEL PROBLEMA]

Opción 1:
\`\`\`[LENGUAJE]
[CÓDIGO OPCIÓN 1]
\`\`\`

Opción 2:
\`\`\`[LENGUAJE]
[CÓDIGO OPCIÓN 2]
\`\`\`

Opción 3:
\`\`\`[LENGUAJE]
[CÓDIGO OPCIÓN 3]
\`\`\`

Por favor:
1. Analiza cada opción
2. Compara en: velocidad, claridad, eficiencia
3. ¿Cuál es mejor? ¿Por qué?
4. Casos de uso de cada una
5. Alternativas adicionales
6. Tu recomendación

Soy [NIVEL], explica técnicas avanzadas si las usas.
```

---

## 🎓 EXPLICACIÓN DE CONCEPTOS AVANZADOS

### Plantilla 9: Concepto Complejo Desglosado

```
Encontré [CONCEPTO] en un proyecto/tutorial pero no lo entiendo.

Soy [NIVEL].

Aquí está el concepto:
[DESCRIPCIÓN O CÓDIGO]

No entiendo:
- [Punto confuso 1]
- [Punto confuso 2]
- [Punto confuso 3]

Por favor:
1. Visión general del concepto
2. Desglosa en partes simples
3. Por qué es importante
4. Ejemplo simple vs complicado
5. Cuándo usarlo en proyectos reales
6. Próximos pasos para dominarlo

Sé muy paciente y claro.
```

---

## 📋 CHECKLISTS Y VALIDACIÓN

### Plantilla 10: Validar mi Código

```
Terminé una función/programa. Soy [NIVEL].

Código:
\`\`\`[LENGUAJE]
[CÓDIGO]
\`\`\`

Por favor revisa:
1. ¿Hay bugs potenciales?
2. ¿Sigue buenas prácticas?
3. ¿Es eficiente?
4. ¿Hay validaciones suficientes?
5. ¿Los nombres de variables son claros?
6. ¿Falta documentación?
7. ¿Hay casos extremos no cubiertos?
8. Sugerencias de mejora
9. Score de calidad (1-10) con explicación

Soy [NIVEL], se amable con las críticas.
```

---

## 🚀 MIS PROMPTS FAVORITOS

### Favorito 1: Aprender con Proyecto

```
Quiero aprender [CONCEPTO] haciendo un pequeño proyecto.

Soy [NIVEL].

Proyecto idea: [IDEA SIMPLE]

Este proyecto me ayudaría a:
- Entender [CONCEPTO]
- Practicar [OTRA COSA]
- Ver uso en mundo real

¿Cómo estructura esto? Dame:
1. Qué partes del proyecto necesito
2. Orden para implementar (más fácil a difícil)
3. Código para PASO 1
4. Consejos para cada paso
5. Cómo probar cada parte
```

---

### Favorito 2: Explicación Multinivel

```
Explícame [CONCEPTO] en 3 niveles.

Soy [NIVEL].

Nivel 1: Como a un niño de 5 años (analogía simple)
Nivel 2: Como explicación técnica concisa
Nivel 3: Profundidad completa con código

Incluye ejemplos para cada nivel.
```

---

### Favorito 3: Hoja de Ruta Personalizada

```
Quiero aprender [TEMA] pero no sé por dónde empezar.

Mi nivel actual: [NIVEL]
Mi objetivo: [OBJETIVO ESPECÍFICO]
Tiempo disponible: [TIEMPO]
Mi estilo de aprendizaje: [VIDEO/LECTURA/PRÁCTICA]

Por favor dame:
1. Pre-requisitos (qué debo saber ya)
2. Ruta de aprendizaje (pasos en orden)
3. Recursos recomendados
4. Proyectos para practicar (fácil a difícil)
5. Señales de que lo domino
6. Tiempo estimado total

Luego podemos profundizar en cada paso.
```

---

## ✨ PRO TIPS

### Tip 1: Usa Contexto

```
"Como estoy en Fase 2 de Python y acabo de aprender
listas, esto es lo que intento..."
```

### Tip 2: Se Iterativo

```
TÚ: "Explica herencia"
CLAUDE: "[Explicación]"
TÚ: "¿Y si..."
CLAUDE: "[Más detalle]"
TÚ: "Cómo eso se aplica a..."
```

### Tip 3: Pide Ejemplos

```
"Proporciona 5 ejemplos progresivos
(fácil → difícil)"
```

### Tip 4: Valida Siempre

```
"Ejecuté tu código en mi computadora.
Funcionó pero quiero entender por qué X parte..."
```

---

**¡Copia, pega y customiza!** 🚀
