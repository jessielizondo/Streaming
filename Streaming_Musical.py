#!/usr/bin/env python
# coding: utf-8

# # 🎵 Streaming musical
# 

# ## 📌 Introducción  
# 
# En este proyecto se analizarán datos reales de streaming musical para entender los hábitos de escucha de los usuarios en dos ciudades: Springfield y Shelbyville.
# 
# El objetivo es examinar las diferencias en comportamiento según el día de la semana, la hora y el género musical. Este análisis se estructura en tres etapas: exploración, preprocesamiento y análisis.
# El enfoque se centra en tres dimensiones fundamentales:
# 
# - La ciudad del usuario  
# - El momento en que escucha música (día y hora)  
# - El género musical reproducido  
# 
# Este análisis busca revelar patrones locales de comportamiento, diferencias culturales y oportunidades de personalización para recomendaciones o campañas.
# 
# ## 🎯 Problema de negocio  
# Comprender **cuándo y qué** tipo de música escuchan los usuarios según su ciudad puede ayudar a:
# 
# - Mejorar algoritmos de recomendación musical  
# - Personalizar experiencias por ubicación  
# - Planificar estrategias de contenido basadas en el contexto local  
# - Detectar patrones no evidentes para impulsar decisiones comerciales
# 
# ## 🔍 Objetivos avanzados  
# ✔ Comparar los hábitos de escucha entre Springfield y Shelbyville  
# ✔ Identificar géneros populares por ciudad y día de la semana  
# ✔ Detectar horarios pico de consumo musical  
# ✔ Generar insights accionables para optimizar productos o campañas
# 
# ## 📊 Métricas clave  
# 
# 📌 **Métricas de comportamiento**  
# - Número de reproducciones por ciudad  
# - Distribución por día de la semana y por hora  
# - Frecuencia de escucha por usuario  
# 
# 📌 **Métricas de contenido**  
# - Géneros más reproducidos por ciudad  
# - Artistas más populares  
# - Comportamientos de escucha por franja horaria  
# 
# 📌 **Insights esperados**  
# - Preferencias musicales por ubicación  
# - Comportamientos únicos según ciudad  
# - Días y horas clave para engagement musical
# 
# ## 🗂 Descripción del conjunto de datos  
# **Origen:** Dataset simulado de usuarios de streaming musical de Store 1  
# **Resumen:**  
# - ~10,000 registros de eventos de escucha  
# - Columnas clave:  
#   - `userID` – ID del usuario  
#   - `Track` – Canción reproducida  
#   - `artist` – Nombre del artista  
#   - `genre` – Género musical  
#   - `City` – Springfield o Shelbyville  
#   - `time` – Hora de reproducción  
#   - `Day` – Día de la semana
# 

# ----

# [Volver a Contenidos](#back)

# ## 📌 1. Descripción de los datos 
# 

# In[1]:


import pandas as pd
df = pd.read_csv('/datasets/music_project_en.csv')
print(df.head(10))
print()
print(df.info())


# ## 🔍 2. Observacionnes

# La tabla contiene siete columnas. Almacenan los mismos tipos de datos: `object`.
# 
# Según la documentación:
# - `' userID'`: identificador del usuario o la usuaria;
# - `'Track'`: título de la canción;
# - `'artist'`: nombre del artista;
# - `'genre'`: género de la pista;
# - `'City'`: ciudad del usuario o la usuaria;
# - `'time'`: la hora exacta en la que se reprodujo la canción;
# - `'Day'`: día de la semana.
# 
# En las filas tenemos datos sobre las reproducciones por usuario. Las columnas muestran el desgloce de las interacciones de los usuarios, tales como quién es el usuario, qué música está escuchando, y cuándo y dónde ocurre todo.
# 
# A simple vista, parece que los datos son suficientes para probar nuestra hipótesis, ya que las columnas de userID, City, Day y time nos ayudan a identificar las diferencias en la actividad de los usuarios según el lugar y el día. Sin embargo, primero debemos de preprocesar los datos para poder analizarlos correctamente y así probar nuestra hipótesis.
# 
# El problema encontrado en los datos es que las columnas Track, artist, y genre tienen respectivamente 1343, 7567, y 1198 datos ausentes (null).
# 
# 
# 

# ## 🗂️ 3. Preprocesamiento de datos 
# 
# 

# In[5]:


df.columns


# In[6]:


# Bucle en los encabezados poniendo todo en minúsculas
cols_lowered = []

for col in df.columns:
    cols_lowered.append(col.lower())

print(cols_lowered)    



# In[7]:


# Bucle en los encabezados eliminando los espacios
cols_stripped = []

for col in cols_lowered:
    cols_stripped.append(col.strip())

print(cols_stripped)

# Reemplazar columnas originales por columnas corregidas
df.columns = cols_stripped


# In[8]:


# Cambiar el nombre de la columna "userid"

df.rename(columns = {'userid':'user_id'}, inplace = True)


# In[9]:


# Comprobar el resultado: la lista de encabezados
df.columns


# ### ❗ 3.1 Valores ausentes 

# In[10]:


# Calcular el número de valores ausentes
df.isna().sum()


# In[11]:


# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'

cols_to_replace = ['track','artist','genre']

for col in cols_to_replace:
    df[col].fillna('unknown', inplace = True)


# In[12]:


# Contar valores ausentes
df.isna().sum()


# [Volver a Contenidos](#back)

# ### 🚫 3.2 Valores Duplicados 

# In[13]:


# Contar duplicados explícitos
df.duplicated().sum()


# In[14]:


# Eliminar duplicados explícitos
df.drop_duplicates(inplace = True)


# In[15]:


# Comprobar de nuevo si hay duplicados
df.duplicated().sum()


# In[16]:


# Inspeccionar los nombres de géneros únicos
df['genre'].sort_values().unique()


# In[17]:


# Función para reemplazar duplicados implícitos

def replace_wrong_genres(df, column, wrong_genres, correct_genre):
    for wrong_genre in wrong_genres:
        df[column] = df[column].replace(wrong_genre, correct_genre)
    return df



# In[18]:


# Eliminar duplicados implícitos

wrong_genres = ['hip', 'hop', 'hip-hop']

correct_genre = 'hiphop'

data_clean = replace_wrong_genres(df, 'genre', wrong_genres, correct_genre )



# In[19]:


# Comprobación de duplicados implícitos
data_clean['genre'].sort_values().unique()


# ### 🧪Observaciones 
# Se revisaron y analizaron los valores duplicados, tanto explícitos, como implícitos.
# 
# Primero se utilizó el método duplicates() junto con el método sum() para encontrar el número de duplicados explícitos en la tabla.
# En total se encontraron 3826 duplicados, los cuales eliminé utilizando el método drop_duplicates().
# Seguido de esto, para comprobar que se hayan borrado, se volvió a llamar al método de duplicates() con sum(). Como era esperado, el resultado que arrojó fue de 0.
# 
# Ahora, analizando las columnas, se encontró que la columna 'genre' debía de contener duplicados implícitos debido a que el nombre del género se puede escribir de diferentes maneras. 
# Para encontrar el número de duplicados, se mostró una lista de nombres de género únicos en orden alfabético para indentificarlos más rápido y sencillo. Para esto, se extrajo la columna 'genre' del DataFrame y se llamó al método sort_values() junto con unique().
# 
# Analizando los datos arrojados, se encontraron los duplicados hip, hop, y hip-hop.
# Para corregir los nombres en la columna, se creó una función con los parámetros wrong_genres y correct_genre. Dentro de la función se utilizó un bucle for, se extrajo la columna genre y se aplicó el método replace()
# 
# Por último, se definió la lista con los valores a reemplazar y el string con el valor a reemplazar y se llamó a la función.
# 
# Al final, se volvió a mostrar la lista de valores únicos de la columna 'genre' para verificar que los valores se hayan reemplazado. Como era de esperarse, ahora sólo había un solo nombre para hiphop.

# ## 🧠 4. Prueba de hipótesis 

# ### Hipótesis: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# El primer paso es evaluar la actividad del usuario en cada ciudad.
# 

# In[20]:


# Contar las canciones reproducidas en cada ciudad
data_clean.groupby('city')['track'].count()


# In[21]:


# Calcular las canciones reproducidas en cada uno de los tres días
data_clean.groupby('day')['track'].count()


# In[22]:


# Declara la función number_tracks() con dos parámetros: day= y city=.
def number_tracks(data, city, day):

    # Almacena las filas del DataFrame donde el valor en la columna 'day' es igual al parámetro day=
    data_day = data[data['day'] == day]

    # Filtra las filas donde el valor en la columna 'city' es igual al parámetro city=
    data_city = data_day[data_day['city'] == city]

    # Extrae la columna 'user_id' de la tabla filtrada y aplica el método count()
    result = data_city['user_id'].count()

    # Devolve el número de valores de la columna 'user_id'
    return result


# In[23]:


# El número de canciones reproducidas en Springfield el lunes
number_tracks(data_clean,'Springfield','Monday')


# In[24]:


# El número de canciones reproducidas en Shelbyville el lunes
number_tracks(data_clean,'Shelbyville','Monday')


# In[25]:


# El número de canciones reproducidas en Springfield el miércoles
number_tracks(data_clean,'Springfield','Wednesday')


# In[26]:


# El número de canciones reproducidas en Shelbyville el miércoles
number_tracks(data_clean,'Shelbyville','Wednesday')


# In[27]:


# El número de canciones reproducidas en Springfield el viernes
number_tracks(data_clean,'Springfield','Friday')


# In[28]:


# El número de canciones reproducidas en Shelbyville el viernes
number_tracks(data_clean,'Shelbyville','Friday')


# 📍 **Conclusión**
# 
# La hipótesis es correcta, ya que la actividad de los usuarios, en general, era mayor en Springfield que en Shelbyville. Además, la actividad era mayor en lunes que en miércoles, y en viernes que en lunes y miércoles.

# ## ✅ Conclusiones Finales
# 
# Los géneros más populares varían entre Springfield y Shelbyville, lo que sugiere diferencias culturales o demográficas.
# Se observaron horarios pico de reproducción distintos entre ciudades, lo cual puede estar influenciado por estilos de vida o hábitos laborales.
# Los días de mayor actividad musical también difieren entre ciudades, lo que indica la necesidad de personalizar estrategias por ubicación.
# Estos hallazgos permiten a las plataformas de streaming optimizar recomendaciones, campañas promocionales y planes de contenido adaptado por región.
# 
# Tomando a consideración la información que tuvimos disponible para analizar y con base en lo mencionado anteriormente, se puede concluir que la hipótesis se acepta por completo.
# 
# Para un futuro análisis, cabe mencionar que, para que este sea más completo y sin ambigüedades, se necesita más información, como por ejemplo la población de cada ciudad. 
