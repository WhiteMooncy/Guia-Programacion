# ⚡ Quick Start: Usa Claude en 5 Minutos

> **Comienza a usar Claude ya mismo. La guía más rápida posible.**

---

## 🚀 Paso 1: Abre Claude (2 minutos)

1. Ve a: **https://claude.ai**
2. Haz click en **"Create Account"**
3. Usa tu email
4. Verifica tu email
5. ¡Listo! Ya puedes usar

**Costo:** Gratis (con límites generosos)

---

## 📝 Paso 2: Tu Primer Mensaje (1 minuto)

Copia y pega esto en el chat:

```
Hola Claude, soy estudiante de programación (principiante).

¿Puedes ayudarme a entender conceptos y escribir código?

Si digo algo que no entiendas, avísame.
```

Claude responderá que claro.

---

## 💻 Paso 3: Pide Tu Primer Código (2 minutos)

Copia y pega esto:

```
Necesito una función en Python que:
1. Pida un número al usuario
2. Diga si es par o impar
3. Mostrar un mensaje claro

Soy principiante, comenta el código.
```

Claude te dará código listo para usar.

---

## ✅ Paso 4: Prueba El Código

**En tu computadora:**

1. Abre un editor (VSCode)
2. Crea archivo: `prueba.py`
3. Copia el código de Claude
4. Guarda
5. Ejecuta: `python prueba.py`

---

## 🎯 Paso 5: Pide Explicación

Pregunta en Claude:

```
¿Por qué usas % en el código?

¿Hay otra forma?
```

Claude explicará línea por línea.

---

## 🔥 Tips Inmediatos

### Tip 1: Sé Específico

❌ "Cómo hago código"  
✅ "Función en Python que ordene lista de números"

### Tip 2: Proporciona Contexto

```
Soy Fase 2 (Python básico).
Mi código da error: [ERRO]
```

### Tip 3: Itera Preguntas

```
TÚ: "Explica variables"
CLAUDE: "[Explicación]"
TÚ: "¿Y si quiero..."
CLAUDE: "[Más detalle]"
```

### Tip 4: Valida Todo

```
1. Copia código de Claude
2. Ejecutalo
3. Entiendelo
4. Modifícalo
```

### Tip 5: Usa Plantillas

Copia de [PROMPTS_LISTOS.md](PROMPTS_LISTOS.md)

---

## 🚫 Lo Que NO Hacer

- ❌ Copiar sin entender
- ❌ Preguntas vagas
- ❌ Esperar perfección
- ❌ Ignorar la validación
- ❌ No iterar preguntas

**Leer:** [ANTIPATRONES.md](../recursos/ANTIPATRONES.md)

---

## 📚 Que Leer Después

1. **[GUIA_CLAUDE_IA.md](GUIA_CLAUDE_IA.md)** - Guía completa
2. **[PROMPTS_LISTOS.md](PROMPTS_LISTOS.md)** - Plantillas
3. **[EJEMPLOS_CONVERSACIONES.md](EJEMPLOS_CONVERSACIONES.md)** - Reales

---

## 🎓 Conversación Ejemplo

### PASO 1: Hola

**TÚ:**

```
Hola, soy principiante en Python.
Estoy aprendiendo variables.
¿Puedes darme un ejemplo?
```

**CLAUDE:**

```
¡Claro!

Una variable es un "contenedor" para datos:

nombre = "Juan"
edad = 25
altura = 1.75

nombre almacena texto
edad almacena número
altura almacena número decimal
```

### PASO 2: Profundiza

**TÚ:**

```
¿Y si quiero guardar varios nombres?
```

**CLAUDE:**

```
Usa una lista:

nombres = ["Juan", "María", "Carlos"]
print(nombres[0])  # "Juan"
```

### PASO 3: Experimenta

**TÚ:**

```
¿Cómo acceso el segundo nombre?
```

**CLAUDE:**

```
índice 1 (empieza en 0):

print(nombres[1])  # "María"
```

---

## 🎯 Tu Primer Proyecto

### Idea: Conversor de Temperatura

**PROMPT PARA CLAUDE:**

```
Soy principiante.
Quiero un programa Python que:
1. Pida temperatura en Celsius
2. Convierta a Fahrenheit
3. Muestre resultado

Por favor: código comentado + explicación

Fórmula: F = (C × 9/5) + 32
```

Claude te dará:

```python
# Pedir temperatura
celsius = input("¿Temperatura en C? ")

# Convertir a número
celsius = float(celsius)

# Fórmula
fahrenheit = (celsius * 9/5) + 32

# Mostrar
print(f"{celsius}C = {fahrenheit}F")
```

---

## 💡 Regla de Oro

```
CLAUDE NO reemplaza aprendizaje.
CLAUDE acelera aprendizaje.

Si no entiendes código, NO lo uses.
Pide explicación hasta entenderlo.

Así aprendes real.
```

---

## 🔗 Enlaces

- **Claude:** https://claude.ai
- **Documentación:** https://docs.anthropic.com
- **Guías Completas:** Ver carpeta `recursos/`

---

**¿Listo? ¡Abre Claude ahora!** 🚀

No esperes más. Aprenderás haciendo.
