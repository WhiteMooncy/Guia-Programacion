# 🟠 Fase 3: Programación Orientada a Objetos (POO)

**Duración:** 3-4 semanas  
**Nivel:** Intermedio  
**Requisito:** Completar Fase 2 (Python Fundamentals)  
**Objetivo:** Dominar conceptos de OOP para escribir código profesional y escalable

---

## 📚 Tabla de Contenidos

1. [Introducción a POO](#introducción-a-poo)
2. [Conceptos Fundamentales](#conceptos-fundamentales)
3. [Clases y Objetos](#clases-y-objetos)
4. [Herencia](#herencia)
5. [Encapsulación](#encapsulación)
6. [Polimorfismo](#polimorfismo)
7. [Ejemplos Prácticos](#ejemplos-prácticos)
8. [Ejercicios](#ejercicios)
9. [Proyectos](#proyectos)

---

## 🎯 Introducción a POO

### ¿Qué es Programación Orientada a Objetos?

POO es un **paradigma de programación** que organiza el código alrededor de **objetos** en lugar de funciones.

**Analogía del mundo real:**

- **Función:** Es como escribir una lista de pasos ("Hacer un café")
- **Objeto:** Es como tener una máquina de café completa con sus propiedades y acciones

### Ventajas de POO

✅ **Código más organizado** - Los datos y funciones están juntos  
✅ **Reutilizable** - Herencia y composición evitan repetir código  
✅ **Mantenible** - Fácil entender y modificar código  
✅ **Escalable** - Facilita proyectos grandes  
✅ **Profesional** - Estándar en desarrollo moderno

### Cuándo usar POO

**Usa POO cuando:**

- Tu proyecto tiene muchos datos relacionados
- Necesitas reutilizar código
- Trabajas en equipo
- El proyecto es mediano/grande

**No necesitas POO para:**

- Scripts simples
- Automatizaciones cortas
- Prototipos rápidos

---

## 📖 Conceptos Fundamentales

### 1. Clases y Objetos

Una **clase** es el plano/molde. Un **objeto** es la instancia.

**Analogía:**

- **Clase:** Plano de una casa
- **Objeto:** La casa construida

```python
# Definir una clase
class Persona:
    pass  # Por ahora vacía

# Crear objetos (instancias)
juan = Persona()
maria = Persona()

print(type(juan))  # <class '__main__.Persona'>
```

### 2. Atributos

Son las **propiedades** del objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo

juan = Persona("Juan", 25)
print(juan.nombre)  # Juan
print(juan.edad)    # 25
```

### 3. Métodos

Son las **acciones** que el objeto puede hacer.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):  # Método
        print(f"Hola, soy {self.nombre}")

    def cumpleaños(self):  # Método
        self.edad += 1
        print(f"¡Ahora tengo {self.edad}!")

juan = Persona("Juan", 25)
juan.saludar()      # Hola, soy Juan
juan.cumpleaños()   # ¡Ahora tengo 26!
```

### 4. Constructor (**init**)

El **constructor** es un método especial que se ejecuta cuando creas un objeto.

```python
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        print(f"✓ Coche {marca} {modelo} creado")

mi_coche = Coche("Toyota", "Corolla", 2023)
# Imprime: ✓ Coche Toyota Corolla creado
```

---

## 🏗️ Clases y Objetos (Profundo)

### Ejemplo Completo: Sistema Bancario

```python
class CuentaBancaria:
    """Representa una cuenta bancaria"""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historial = []

    def depositar(self, cantidad):
        """Deposita dinero en la cuenta"""
        if cantidad <= 0:
            print("❌ La cantidad debe ser positiva")
            return False

        self.saldo += cantidad
        self.historial.append(f"Depósito: +{cantidad}")
        print(f"✓ Depositado: {cantidad}. Nuevo saldo: {self.saldo}")
        return True

    def retirar(self, cantidad):
        """Retira dinero de la cuenta"""
        if cantidad > self.saldo:
            print("❌ Saldo insuficiente")
            return False

        self.saldo -= cantidad
        self.historial.append(f"Retiro: -{cantidad}")
        print(f"✓ Retirado: {cantidad}. Nuevo saldo: {self.saldo}")
        return True

    def obtener_saldo(self):
        """Retorna el saldo actual"""
        return self.saldo

    def ver_historial(self):
        """Muestra el historial de transacciones"""
        print(f"\n📜 Historial de {self.titular}:")
        for i, transaccion in enumerate(self.historial, 1):
            print(f"  {i}. {transaccion}")

    def __str__(self):
        """Representación en string"""
        return f"Cuenta de {self.titular}: ${self.saldo}"

# Uso
cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.ver_historial()
print(cuenta)
```

---

## 👨‍👩‍👧 Herencia

Permite que una clase **herede** propiedades y métodos de otra.

### Concepto

```python
class Animal:
    """Clase base (padre)"""
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    """Clase derivada (hijo) - hereda de Animal"""
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    """Otra clase derivada"""
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Uso
perro = Perro("Rex")
gato = Gato("Michi")

perro.hacer_sonido()  # Rex dice: ¡Guau!
gato.hacer_sonido()   # Michi dice: ¡Miau!
```

### Ejemplo Avanzado: Sistema de Empleados

```python
class Empleado:
    """Clase base de empleados"""
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_detalles(self):
        return f"{self.nombre}: ${self.salario}"

class Desarrollador(Empleado):
    """Empleado desarrollador"""
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)  # Llama constructor de padre
        self.lenguaje = lenguaje

    def obtener_detalles(self):
        return super().obtener_detalles() + f" (Desarrolla en {self.lenguaje})"

class Gerente(Empleado):
    """Empleado gerente"""
    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario)
        self.equipo = equipo

    def obtener_detalles(self):
        return super().obtener_detalles() + f" (Gerencia equipo de {self.equipo})"

# Uso
dev = Desarrollador("Juan", 3000, "Python")
gerente = Gerente("María", 5000, 5)

print(dev.obtener_detalles())
# Juan: $3000 (Desarrolla en Python)

print(gerente.obtener_detalles())
# María: $5000 (Gerencia equipo de 5)
```

---

## 🔐 Encapsulación

Control de acceso a atributos usando `public`, `protected` y `private`.

```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular           # Public
        self._numero_cuenta = "123456"   # Protected (por convención)
        self.__saldo = saldo             # Private (doble guion bajo)

    def depositar(self, cantidad):
        """Solo se puede acceder a __saldo a través de métodos"""
        if cantidad > 0:
            self.__saldo += cantidad

    def obtener_saldo(self):
        """Método público para acceder a saldo privado"""
        return self.__saldo

cuenta = CuentaBancaria("Juan", 1000)

# Acceso permitido
print(cuenta.titular)        # Juan
print(cuenta.obtener_saldo())  # 1000

# Esto fallará (Python lo protege)
# print(cuenta.__saldo)  # AttributeError
```

---

## 🎭 Polimorfismo

Un método con el mismo nombre se comporta diferente según la clase.

```python
class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio ** 2)

# Polimorfismo: mismo método, diferente implementación
figuras = [Cuadrado(5), Circulo(3)]

for figura in figuras:
    print(f"Área: {figura.area()}")
    # Cuadrado: 25
    # Círculo: 28.26
```

---

## 💡 Ejemplos Prácticos

### Ejemplo 1: Sistema de Biblioteca

```python
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_disponibles(self):
        return [l for l in self.libros if l.disponible]

    def prestar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro.prestar()
        return False

# Uso
biblioteca = Biblioteca()
libro1 = Libro("1984", "George Orwell", "123")
biblioteca.agregar_libro(libro1)

print(len(biblioteca.listar_disponibles()))  # 1
biblioteca.prestar_libro("123")
print(len(biblioteca.listar_disponibles()))  # 0
```

---

## 🎯 Ejercicios

### Nivel 1: Principiante

1. **Clase Persona** - Crear clase con nombre, edad, métodos saludar()
2. **Clase Producto** - Tienda con precio, descuento, calcular_precio_final()
3. **Clase Temperatura** - Convertir y almacenar temperaturas

### Nivel 2: Intermedio

4. **Sistema Escolar** - Clases: Estudiante, Profesor, Materia
5. **Red Social** - Usuario, Publicación, seguir/dejar de seguir
6. **Videojuego** - Personaje, Arma, inventario

### Nivel 3: Avanzado

7. **E-commerce** - Producto, Carrito, Pedido, Pago
8. **Sistema de Empleados** - Empleado, Desarrollador, Diseñador, Gerente
9. **Juego de Cartas** - Baraja, Mano, Juego

---

## 🚀 Proyectos

### Proyecto 1: Sistema de Gestión Escolar (2 semanas)

**Requisitos:**

- Clase `Estudiante` con atributos de persona, calificaciones
- Clase `Profesor` con especialidad
- Clase `Materia` con estudiantes matriculados
- Clase `Escuela` que gestiona todo

**Funcionalidades:**

- Agregar/remover estudiantes
- Asignar calificaciones
- Calcular promedio
- Generar reportes

### Proyecto 2: Juego de Rol Simple (3 semanas)

**Requisitos:**

- Clase `Personaje` con estadísticas (vida, ataque, defensa)
- Clase `Enemigo` que hereda de Personaje
- Clase `Juego` que controla el flujo
- Sistema de combate con turnos

**Funcionalidades:**

- Crear personajes
- Sistema de combate
- Inventario de objetos
- Niveles y experiencia

---

## 📊 Progresión Recomendada

```
Semana 1: Clases, objetos, atributos, métodos
Semana 2: Herencia, super(), polimorfismo
Semana 3: Encapsulación, métodos especiales (__str__, __repr__)
Semana 4: Proyectos integrados
```

---

## 🔗 Recursos Adicionales

- **Documentación oficial:** https://docs.python.org/3/tutorial/classes.html
- **Tutorial interactivo:** https://www.w3schools.com/python/python_oop.asp
- **Videos:** "Python OOP Tutorial" en YouTube

---

## ✅ Checklist de Progreso

- [ ] Entiendo qué es una clase y un objeto
- [ ] Puedo crear clases con atributos y métodos
- [ ] Comprendo y uso herencia correctamente
- [ ] Implemento encapsulación en mis clases
- [ ] Aplico polimorfismo en proyectos
- [ ] Puedo diseñar una arquitectura de clases
- [ ] Completé al menos 1 proyecto POO

---

**¡Felicidades! Dominar POO es un paso importante hacia programación profesional.** 🎉

Cuando termines esta fase, estarás listo para **Fase 4: Especialización**.
