# 🎧 Análisis de Escucha Musical por Ciudad  
Exploración de hábitos de escucha en Springfield y Shelbyville usando Python

## 📌 Introducción  
Store 1 amplía su análisis de datos explorando un nuevo dominio: los **hábitos de escucha musical** de los usuarios. En esta tercera fase del proyecto, se estudian los patrones de consumo de música en **Springfield** y **Shelbyville** para descubrir diferencias clave que puedan informar futuras decisiones de producto y marketing.

El enfoque se centra en tres dimensiones fundamentales:

- La ciudad del usuario  
- El momento en que escucha música (día y hora)  
- El género musical reproducido  

Este análisis busca revelar patrones locales de comportamiento, diferencias culturales y oportunidades de personalización para recomendaciones o campañas.

## 🎯 Problema de negocio  
Comprender **cuándo y qué** tipo de música escuchan los usuarios según su ciudad puede ayudar a:

- Mejorar algoritmos de recomendación musical  
- Personalizar experiencias por ubicación  
- Planificar estrategias de contenido basadas en el contexto local  
- Detectar patrones no evidentes para impulsar decisiones comerciales

## 🔍 Objetivos avanzados  
✔ Comparar los hábitos de escucha entre Springfield y Shelbyville  
✔ Identificar géneros populares por ciudad y día de la semana  
✔ Detectar horarios pico de consumo musical  
✔ Generar insights accionables para optimizar productos o campañas

## 📊 Métricas clave  

📌 **Métricas de comportamiento**  
- Número de reproducciones por ciudad  
- Distribución por día de la semana y por hora  
- Frecuencia de escucha por usuario  

📌 **Métricas de contenido**  
- Géneros más reproducidos por ciudad  
- Artistas más populares  
- Comportamientos de escucha por franja horaria  

📌 **Insights esperados**  
- Preferencias musicales por ubicación  
- Comportamientos únicos según ciudad  
- Días y horas clave para engagement musical

## 🗂 Descripción del conjunto de datos  
**Origen:** Dataset simulado de usuarios de streaming musical de Store 1  
**Resumen:**  
- ~10,000 registros de eventos de escucha  
- Columnas clave:  
  - `userID` – ID del usuario  
  - `Track` – Canción reproducida  
  - `artist` – Nombre del artista  
  - `genre` – Género musical  
  - `City` – Springfield o Shelbyville  
  - `time` – Hora de reproducción  
  - `Day` – Día de la semana


## ⚙️ Proceso de análisis  
Realizado en Python con Pandas, NumPy y visualización con Matplotlib.

### Paso 1: Revisión de datos  
✔ Cargar y explorar el dataset  
✔ Validar estructura de columnas y tipos de datos  

### Paso 2: Limpieza  
✔ Eliminar duplicados  
✔ Corregir nombres y formatos  
✔ Manejo de valores nulos  

### Paso 3: Análisis comparativo  
✔ Comparar escucha por ciudad, día y género  
✔ Detectar diferencias de comportamiento  

### Paso 4: Conclusiones  
✔ Resumir hallazgos clave  
✔ Formular recomendaciones  

## 📁 Estructura del repositorio  
📂 data  
   └── music_project_en.csv - Dataset de escucha musical  

📂 notebooks  
   └── Proyecto_Sprint3.ipynb - Notebook principal  

📂 visuals  
   └── charts/ - Gráficos del análisis  

📂 insights  
   └── summary.md - Conclusiones y observaciones  

## 📬 Contacto  
📧 Correo: jessica.elizondo.t@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/jessica-elizondo-t
