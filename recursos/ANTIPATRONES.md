# 🚫 Anti-Patrones: Lo Que NO Hacer con IA

> **Errores comunes cuando usas IA para programar y cómo evitarlos.**

---

## ❌ Error 1: Copiar-Pegar Sin Entender

### ❌ MAL

```
TÚ: "Dame código para leer un archivo"
CLAUDE: "[Proporciona código]"
TÚ: "Gracias" → Copias y pegas sin leer
```

### 🚀 BIEN

```
TÚ: "Dame código para leer un archivo"
CLAUDE: "[Proporciona código]"
TÚ: "¿Por qué usas 'with'?", "¿Qué pasa si no existe?"
CLAUDE: "[Explicación]"
```

**Impacto:** Si no entiende, cuando algo falla no sabrá qué hacer.

---

## ❌ Error 2: Preguntas Demasiado Vagas

### ❌ MAL

```
"¿Cómo programo?"
"¿Qué es Python?"
"Necesito ayuda con código"
```

Claude responderá genéricamente. No es útil.

### 🚀 BIEN

```
"Soy Fase 2. Quiero crear una función que valide
emails en Python. Debe revisar @ y .com"

"No entiendo por qué mi función retorna None"

"¿Es más eficiente list comprehension o for?"
```

**Impacto:** Respuestas precisas y prácticas.

---

## ❌ Error 3: Usar IA para Tareas Sin Pensar

### ❌ MAL

```
TÚ: "Haz mi tarea de programación"
CLAUDE: "Lo siento, no puedo hacer tareas"
TÚ: "Bueno, dame el código..."
```

No aprendes nada. Y no es honesto.

### 🚀 BIEN

```
"Estoy trabado en [PUNTO ESPECÍFICO].
Ya hice [ESTO], pero necesito ayuda con [ESTO]"
```

**Impacto:** Aprendes real, honestidad académica, dominas el tema.

---

## ❌ Error 4: No Proporcionar Contexto

### ❌ MAL

```
"Mi código no funciona"
"Error en la función"
"Ayuda con diccionarios"
```

Claude no sabe:

- Qué código
- Qué error
- Qué intenta hacer

### 🚀 BIEN

```
Error:
TypeError: 'str' object is not subscriptable

Mi código:
def obtener_primero(texto):
    return texto[0]

resultado = obtener_primero(123)

Contexto: Intento obtener el primer carácter
```

**Impacto:** Diagnóstico correcto y rápido.

---

## ❌ Error 5: Esperar Perfección

### ❌ MAL

```
"Claude, dame código perfecto y listo para producción"
CLAUDE: [Proporciona código]
TÚ: "¿Y si falla aquí?" "¿Y aquí?"
```

AI no es perfecta. Todo necesita revisión.

### 🚀 BIEN

```
"Dame una función básica para comenzar.
Luego iteramos y mejoramos"

Primero: funcionalidad
Luego: eficiencia
Finalmente: validaciones
```

**Impacto:** Proceso iterativo, mejor aprendizaje.

---

## ❌ Error 6: No Validar el Código

### ❌ MAL

```
CLAUDE: [Proporciona 20 líneas de código]
TÚ: Copias directamente a tu proyecto
RESULTADO: Falla en producción
```

### 🚀 BIEN

```
CLAUDE: [Proporciona código]
TÚ: 1. Lo copias en un archivo de prueba
    2. Lo ejecutas
    3. Lo modificas
    4. Verifica que funcione
    5. Lo integras
```

**Impacto:** Código confiable, sin sorpresas.

---

## ❌ Error 7: Conversación Desconectada

### ❌ MAL

```
MENSAJE 1: "Hola, explica variables"
MENSAJE 2: "Dame código para leer archivos"
MENSAJE 3: "¿Cómo debuggeo?"

Sin conexión entre preguntas
```

Claude se reinicia mentalmente cada vez.

### 🚀 BIEN

```
MENSAJE 1: "Estoy en Fase 2. Quiero un gestor de notas"
MENSAJE 2: "¿Cómo guardo las notas en un archivo?"
MENSAJE 3: "¿Cómo cargo las notas al abrir?"
MENSAJE 4: "¿Cómo busco notas?"

Conversación conectada = contexto retenido
```

**Impacto:** Mejor comprensión del proyecto global.

---

## ❌ Error 8: Ignorar Explicaciones

### ❌ MAL

```
CLAUDE: "Aquí está el código. La lógica es:
1. Validar entrada
2. Procesar datos
3. Retornar resultado"

TÚ: "OK gracias" → Copias sin leer la explicación
```

### 🚀 BIEN

```
CLAUDE: [Explicación + Código]
TÚ: 1. Leo la explicación
    2. Entiendo la lógica
    3. Leo el código
    4. Ejecuto
    5. Modifico para experimentar
    6. Pregunto más
```

**Impacto:** Entendimiento profundo, no superficial.

---

## ❌ Error 9: Usar Claude Para Cosas Prohibidas

### ❌ MAL

```
"Cómo hago un hack/exploit/malware"
"Cómo robo datos de..."
"Cómo bypass seguridad de..."
```

Claude rechazará y es correcto.

### 🚀 BIEN

```
"¿Cómo funcionan los ataques de seguridad?
Para aprender a defenderme"

"Quiero aprender criptografía"

"¿Cómo funciona autenticación y por qué es importante?"
```

**Impacto:** Conocimiento ético, skills reales.

---

## ❌ Error 10: No Seguir el Aprendizaje

### ❌ MAL

```
Semana 1: Aprendo variables con Claude
Semana 2: Dejo de practicar
Semana 3: He olvidado todo

Claude fue solo para trucar, no aprender
```

### 🚀 BIEN

```
Semana 1: Aprendo variables
         Hago 3 ejercicios
         Creo pequeño proyecto

Semana 2: Aprendo listas
         Hago 3 ejercicios
         Integro en proyecto

Semana 3: Puedo hacer cosas nuevas
```

**Impacto:** Conocimiento acumulativo y duradero.

---

## ❌ Error 11: Asumir Que Claude Siempre Es Correcto

### ❌ MAL

```
CLAUDE: [Proporciona código]
TÚ: "Si Claude lo dice, debe estar bien"
RESULTADO: Código con bugs

Claude es muy bueno pero no es perfecto.
```

### 🚀 BIEN

```
CLAUDE: [Proporciona código]
TÚ: 1. Lo pruebo
    2. Lo valido
    3. Lo verifico
    4. Pregunto si tiene dudas
    5. Lo mejoro si es necesario
```

**Impacto:** Pensamiento crítico, código confiable.

---

## ❌ Error 12: Preguntar Sin Investigar Primero

### ❌ MAL

```
TÚ: "¿Cómo se instala Python?"
Pregunta que podría responder Googling

TÚ: "¿Qué significa __name__?"
Pregunta que podría buscar en docs
```

### 🚀 BIEN

```
Antes de preguntar a Claude:
1. Busca en Google
2. Lee la documentación
3. Pregunta en Stack Overflow

Si aún no entiendes:
"He visto esto... pero no entiendo por qué..."
```

**Impacto:** Información verificada, mejor aprendizaje.

---

## ✅ CHECKLIST: ¿Estoy Usando IA Bien?

- [ ] Entiendo el código que recibo
- [ ] Valido todo lo que me proporciona
- [ ] Proporciono contexto en mis preguntas
- [ ] Hago preguntas específicas
- [ ] Iteramos en conversaciones conectadas
- [ ] Practico lo que aprendo
- [ ] Cuestiono resultados dudosos
- [ ] Uso Claude para aprender, no para evitar
- [ ] Leo explicaciones, no solo código
- [ ] He experimentado con el código modificándolo
- [ ] Entiendo el "por qué", no solo el "qué"
- [ ] Contribuyo lo que aprendí en la comunidad

Si respondiste "no" a alguno, es oportunidad de mejora.

---

## 🎯 La Regla de Oro

### ✨ REGLA: AI Es Tutor, No Homework Robot

```
Claude DEBE:
✓ Explicar conceptos
✓ Mostrar ejemplos
✓ Ayudarte a debuggear
✓ Sugerir mejores enfoques
✓ Responder preguntas de seguimiento

Claude NO DEBE:
✗ Hacer tu trabajo por ti
✗ Proporcionar respuestas sin contexto
✗ Ser fuente única de verdad
✗ Reemplazar tu pensamiento
✗ Usarse para plagiar
```

---

## 📊 Comparación: Bien vs Mal

| Aspecto       | ❌ Mal              | ✅ Bien           |
| ------------- | ------------------- | ----------------- |
| Entendimiento | Superficial         | Profundo          |
| Retención     | Olvidas en días     | Retienes semanas  |
| Habilidad     | No adquieres        | Desarrollas       |
| Confianza     | Inseguridad         | Seguridad         |
| Velocidad     | Rápido inicialmente | Sostenible        |
| Éxito futuro  | Fallos frecuentes   | Éxito consistente |

---

## 🔗 Recursos Adicionales

- [Guía Oficial Claude](GUIA_CLAUDE_IA.md)
- [Prompts Listos](PROMPTS_LISTOS.md)
- [Ética en IA](../recursos/ETICA_IA.md)

---

**Recuerda:** El mejor código no es el que genera IA.

El mejor código es el que **tú entiendes, escribes y mejorar juntos.**

🚀 ¡Úsalo sabiamente!
