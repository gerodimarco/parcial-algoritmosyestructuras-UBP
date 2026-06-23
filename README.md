# Evaluación Integradora - Algoritmos y Estructuras de Datos

## Alumno
Gerónimo Dimarco Unzaga

# Plataforma de Análisis de Incidentes y Rutas

## Descripción

El sistema simula una plataforma de análisis de incidentes que permite almacenar eventos, realizar búsquedas eficientes, priorizar incidentes, analizar rutas mediante grafos, detectar patrones en textos y demostrar conceptos básicos de criptografía utilizando RSA.

La solución integra los contenidos de los módulos 1 a 6 de la materia, incluyendo Programación Orientada a Objetos, estructuras lineales, árboles, grafos, algoritmos de búsqueda, análisis de complejidad y algoritmos avanzados.

---

## Tecnologías utilizadas

* Python 3.10+
* collections.deque
* heapq
* timeit

No se requieren dependencias externas.

---

## Estructura del proyecto

```text
Parcial/
│
├── main.py
│
├── models/
│   └── event.py
│
├── storage/
│   ├── event_store.py
│   └── index.py
│
├── structures/
│   ├── queue_manager.py
│   └── priority_queue.py
│
├── algorithms/
│   ├── searching.py
│   ├── sorting.py
│   └── benchmark.py
│
├── analysis/
│   └── text_analyzer.py
│
├── routing/
│   └── router.py
│
├── advanced_structures/
│   ├── avl_node.py
│   └── avl_tree.py
│
├── graphs/
│   └── graph.py
│
├── advanced_algorithms/
│   ├── pattern_matching.py
│   └── rsa_demo.py
│
├── benchmarks/
│   └── advanced_benchmark.py
│
└── examples/
    ├── avl_demo.py
    ├── graph_demo.py
    ├── pattern_demo.py
    └── rsa_demo_runner.py
```

---

## Arquitectura

### Event

Representa un incidente dentro del sistema.

Atributos principales:

* id
* timestamp
* category
* priority
* text
* origin
* destination

### EventStore

Gestiona el almacenamiento de eventos.

Operaciones principales:

* add_event()
* get_all_events()

### Index

Implementa indexación utilizando diccionarios de Python para acceder rápidamente a eventos mediante su identificador.

Complejidad promedio:

* Inserción: O(1)
* Búsqueda: O(1)

### QueueManager

Implementa una cola FIFO utilizando collections.deque.

Operaciones:

* enqueue()
* dequeue()
* peek()

### PriorityQueue

Implementa una cola de prioridad utilizando heapq.

Permite atender primero los incidentes más críticos.

---

## Módulo 4 - Árbol AVL

Se implementó un Árbol AVL para indexar incidentes manteniendo el árbol balanceado.

Características:

* Inserción
* Búsqueda
* Rotación izquierda
* Rotación derecha
* Balanceo automático

Complejidad:

* Inserción: O(log n)
* Búsqueda: O(log n)

---

## Módulo 5 - Grafos

La red de rutas se modeló mediante listas de adyacencia.

Algoritmos implementados:

* BFS
* DFS
* Dijkstra
* Kruskal

Aplicaciones:

* Exploración de rutas
* Alcance de nodos
* Camino mínimo
* Árbol de expansión mínima

---

## Módulo 6 - Algoritmos Avanzados

### Búsqueda de patrones

Implementaciones:

* Fuerza Bruta
* Knuth-Morris-Pratt (KMP)

Permiten detectar palabras clave dentro de las descripciones de incidentes.

### RSA demostrativo

Implementación educativa de:

* Generación de claves
* Cifrado
* Descifrado

Utiliza números primos pequeños con fines académicos.

---

## Ejecución del proyecto

### Ejecución principal

Desde la raíz del proyecto:

```bash
python3 main.py
```

---

## Ejemplos individuales

### AVL

```bash
python3 -m examples.avl_demo
```

### Grafos

```bash
python3 -m examples.graph_demo
```

### Búsqueda de patrones

```bash
python3 -m examples.pattern_demo
```

### RSA

```bash
python3 -m examples.rsa_demo_runner
```

---

## Benchmarks

Para ejecutar las mediciones de rendimiento:

```bash
python3 -m benchmarks.advanced_benchmark
```

Las pruebas comparan:

* Fuerza Bruta vs KMP
* Búsqueda en Árbol AVL

---

## Resultados obtenidos

Última ejecución realizada:

### Pattern Matching

Fuerza Bruta: 0.000624 segundos

KMP: 0.001005 segundos

### AVL

Búsqueda AVL: 0.003149 segundos

Los tiempos pueden variar según el hardware utilizado.

---
