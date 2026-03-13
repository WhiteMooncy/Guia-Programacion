# 📇 Referencia Rápida: Claude Cheat Sheet

> **Guía rápida que siempre tener a mano.**

---

## 🔗 Acceso

- **Gratis:** https://claude.ai
- **API:** https://api.anthropic.com
- **Documentación:** https://docs.anthropic.com

---

## 📋 Estructura de Prompt Perfecta

```
CONTEXTO:
"Soy [NIVEL]. Estoy en Fase [X].
He aprendido: [QUÉ]"

PROBLEMA/OBJETIVO:
"Necesito: [QUÉ QUIERO]"

ESPECÍFICOS:
- [Requisito 1]
- [Requisito 2]
- [Requisito 3]

FORMATO DESEADO:
"Por favor proporciona:
1. [Tipo de respuesta 1]
2. [Tipo de respuesta 2]"

NIVEL:
"Explica como si fuera [principiante/intermedio]"
```

---

## 🎯 Prompts Fórmula por Tipo

### 📚 APRENDER CONCEPTO

```
No entiendo [CONCEPTO].

¿Puede:
1. Explicar simple
2. Dar analogía/ejemplo real
3. Código ejemplo
4. ¿Cuándo se usa?
5. Errores comunes

Soy [NIVEL].
```

### 💻 GENERAR CÓDIGO

```
Necesito función Python que:
- [Qué hace]
- Input: [parámetros]
- Output: [resultado]

Requisitos:
- [Validación]
- [Manejo errores]

Proporciona:
1. Código comentado
2. Ejemplo de uso
3. Explicación
```

### 🐛 DEBUGGEAR

```
Error: [ERROR EXACTO]

Mi código:
\`\`\`python
[CÓDIGO]
\`\`\`

¿Qué está mal?
¿Por qué?
¿Solución?
```

### 📈 MEJORAR CÓDIGO

```
¿Cómo mejoro?

\`\`\`python
[CÓDIGO]
\`\`\`

Considera:
- Eficiencia
- Legibilidad
- Mejores prácticas
```

---

## ✅ Checklist: Buen Prompt

- [ ] Incluye contexto (qué fase, nivel)
- [ ] Es específico (no vago)
- [ ] Proporciona código/error si es relevante
- [ ] Pide formato de respuesta
- [ ] Es claro y fácil de leer

---

## ❌ Lo Que NO Hacer

| ❌ MAL               | ✅ BIEN                          |
| -------------------- | -------------------------------- |
| "Cómo programo?"     | "¿Cómo valido emails en Python?" |
| "Mi código falla"    | "Error: [ERROR]. Código: [...]"  |
| Copiar sin entender  | Entender primero                 |
| Confiar ciegamente   | Validar todo                     |
| Una pregunta aislada | Conversación conectada           |

---

## 🔄 Flujo de Conversación

```
1. TÚ: Pregunta inicial (específica)
   ↓
2. CLAUDE: Respuesta + Explicación
   ↓
3. TÚ: Pregunta de seguimiento ("¿Y si...")
   ↓
4. CLAUDE: Profundiza
   ↓
5. Repite hasta dominar
```

---

## 💡 Frases Clave Útiles

### Para pedir explicación

- "Explica como si fuera principiante"
- "Dame una analogía"
- "Paso a paso por favor"
- "¿Por qué usas X en lugar de Y?"

### Para pedir código

- "Código comentado por favor"
- "Muestra ejemplo de uso"
- "¿Hay forma más eficiente?"
- "¿Hay alternativas?"

### Para debugging

- "¿Qué significa este error?"
- "¿Cuál es el problema exacto?"
- "¿Cómo prevenirlo?"
- "¿Hay solución mejor?"

### Para profundizar

- "¿Y si agrego..."
- "¿Cuál es la diferencia con..."
- "¿Cuándo usaría esto vs..."
- "¿Cómo escala esto para..."

---

## 📊 Tipos de Respuestas a Pedir

| Tipo      | Cómo pedir       | Ejemplo                     |
| --------- | ---------------- | --------------------------- |
| Concepto  | "Explica [X]"    | "Explica herencia"          |
| Código    | "Función que..." | "Función que valide emails" |
| Debugging | "Error: [...]"   | "Error: TypeError: ..."     |
| Mejora    | "¿Cómo mejoro?"  | "¿Cómo hago más rápido?"    |
| Pasos     | "Paso a paso"    | "Cómo hacer un servidor"    |
| Analogía  | "Dale analogía"  | "Explica callbacks como..." |

---

## 🚀 Fast Path (Rápido)

```
1. Abre https://claude.ai (2 min)
2. Crea cuenta gratis (2 min)
3. Escribe:
   "Hola, soy principiante. ¿Me ayudas?"
4. ¡Listo! Ya puedes preguntar (1 min)
```

---

## 📱 Usalo en

- 💻 Computadora (mejor)
- 📱 Celular (también funciona)
- ⌨️ VSCode (con extensión)
- 🌐 Cualquier navegador

---

## 🎓 Integración con Curso

| Necesidad         | Archivo a Leer             |
| ----------------- | -------------------------- |
| Empieza ya        | QUICK_START_CLAUDE.md      |
| Prompts listos    | PROMPTS_LISTOS.md          |
| Todo sobre Claude | GUIA_CLAUDE_IA.md          |
| Errores evitar    | ANTIPATRONES.md            |
| Ejemplos reales   | EJEMPLOS_CONVERSACIONES.md |

---

## ⚡ Speed Prompts (Lista)

### Concepto

```
"No entiendo [X]. Explica simple con ejemplo. Soy principiante."
```

### Código

```
"Función Python que [HACE QUÉ]. Código comentado + ejemplo."
```

### Bug

```
"Error: [ERROR]. Código: [CÓDIGO]. ¿Qué está mal?"
```

### Mejora

```
"¿Cómo mejoro esto? [CÓDIGO]. Eficiencia y claridad."
```

### Proyecto

```
"Quiero hacer [PROYECTO]. Fase [X]. Estructura y pasos?"
```

---

## 🎯 Antes de Preguntar

✅ **Sí, pregunta a Claude:**

- Conceptos que no entiendas
- Cómo escribir código
- Debuggear errores
- Mejorar soluciones
- Entender código ajeno

❌ **No, Google primero:**

- Cómo instalar [software]
- Documentación oficial
- Preguntas muy genéricas
- Cosas que ya buscaste

---

## 📈 Evolución Recomendada

```
Semana 1: Aprendes a usar Claude
Semana 2-4: Usas para cada concepto
Mes 2: Usas para proyectos
Mes 3: Usas para debugging avanzado
Mes 4+: Lo dominas, ayudas a otros
```

---

## 🎁 Pro Tips

1. **Guarda conversaciones buenas** - Reutilízalas
2. **Itera preguntas** - No hagas preguntas aisladas
3. **Valida código** - Siempre ejecuta
4. **Modifica ejemplos** - Experimenta
5. **Lee explicaciones** - No solo código
6. **Haz proyectos** - Aplica lo aprendido
7. **Enseña a otros** - Consolida conocimiento

---

## 🔗 Recurso Links

| Recurso   | URL                        |
| --------- | -------------------------- |
| Claude IA | https://claude.ai          |
| API Docs  | https://docs.anthropic.com |
| Guías     | Ver carpeta `recursos/`    |
| Curso     | Aprendizaje-Programacion/  |

---

## ✨ La Regla

```
CLAUDE = Asistente
No = Hacedor de tareas

Úsalo para APRENDER
No para EVITAR pensar
```

---

**Imprime o guarda esta página para consulta rápida.** 🎯

_Última actualización: Marzo 2026_
