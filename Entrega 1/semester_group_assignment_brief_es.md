# Resumen del Trabajo Grupal del Semestre

## Título

Proyecto Semestral: Descubrimiento de Dominios, Recomendación e Inteligencia de Grafos

## Propósito

Esta tarea está diseñada para desarrollarse a lo largo del ciclo completo de 14 semanas del curso.
No es un proyecto de un solo modelo.
Es un proyecto técnico acumulativo que obliga a los estudiantes a practicar:

- adquisición de datos
- diseño de esquemas
- ingeniería de características
- reducción de dimensionalidad
- agrupamiento (clustering)
- recomendación o clasificación (ranking)
- analítica de grafos
- flujos de trabajo (pipelines) reproducibles
- informes técnicos y defensa final

El proyecto debe ser técnico ante todo.
El informe escrito es importante, pero las entregas más sólidas se juzgarán por la calidad del flujo de datos, el rigor de los experimentos y la reproducibilidad de los artefactos.

## Estructura Principal del Proyecto

Cada equipo debe construir un proyecto con las siguientes capas:

1. `capa de catálogo` (catalog layer)
- la tabla de entidades principal
- ejemplos: publicaciones, perfiles, recetas, productos, canciones, negocios, artículos, eventos, cursos

2. `capa de características` (feature layer)
- características numéricas, categóricas, de texto, temporales o derivadas de grafos

3. `capa de interacción o co-ocurrencia` (interaction or co-occurrence layer)
- ejemplos: clics, calificaciones, guardados, cestas, reseñas, etiquetas compartidas, menciones conjuntas, seguimientos, listas, sesiones, listas de reproducción

4. `capa de grafos` (graph layer)
- ejemplos: ítem-ítem, hashtag-hashtag, habilidad-habilidad, negocio-negocio, artículo-artículo, proyección usuario-ítem, grafo de transición de carrera

5. `capa de tubería` (pipeline layer)
- una ruta de construcción reproducible desde los datos brutos hasta los datos procesados y los artefactos de análisis

Los proyectos que se detengan en el aprendizaje supervisado básico se considerarán incompletos para este curso.

## Pistas de Proyecto Permitidas

Los equipos pueden elegir una de las siguientes:

### Pista A: Proyecto con Conjunto de Datos Públicos

Utilizar uno o más conjuntos de datos públicos de Kaggle, portales de datos gubernamentales/abiertos, publicaciones oficiales de investigación o exportaciones sancionadas por plataformas.

Ejemplos:

- recomendación de noticias
- analítica de negocios locales
- recomendación de recetas
- recomendación de comercio electrónico de nicho
- inteligencia de artículos académicos
- descubrimiento de eventos
- recomendación de libros o juegos

### Pista B: Construye Tu Propio Conjunto de Datos

Crear un conjunto de datos a partir de sitios web públicos o APIs, sujeto a la legalidad y las reglas de la plataforma.
Se recomienda encarecidamente esta pista cuando el equipo desea un dominio más original.

Ejemplos:

- herramientas para startups
- eventos culturales locales
- catálogos de podcasts
- juegos indie
- catálogos de cursos abiertos
- bibliotecas de software científico
- comunidades de juegos de mesa

### Pista C: Inteligencia de Contenido de Instagram

Utilizar datos de Instagram solo a través de medios aprobados:

- exportaciones de datos de participantes con consentimiento
- analítica de cuentas de negocios o creadores
- acceso a la API aprobado por la plataforma

Planteamiento sugerido del problema:

- agrupar estilos de contenido
- analizar patrones de compromiso (engagement)
- recomendar hashtags, temas de contenido o estrategias de publicación
- construir grafos de hashtags o menciones

### Pista D: Inteligencia de Carreras y Habilidades de LinkedIn

Utilizar datos de LinkedIn solo a través de medios aprobados:

- exportaciones de datos de participantes con consentimiento
- analítica de administradores de páginas si el equipo tiene acceso válido
- acceso a la API aprobado donde esté disponible

Planteamiento sugerido del problema:

- normalizar y agrupar trayectorias profesionales
- construir grafos de habilidades
- clasificar habilidades, roles o transiciones de carrera
- recomendar direcciones de desarrollo de habilidades o familias de roles

### Pista E: Proyecto Multiplataforma

Combinar múltiples fuentes cuando el equipo pueda justificar la coincidencia.

Ejemplos:

- analítica de marca personal en Instagram más LinkedIn
- reseñas de negocios locales más contenido de redes sociales
- metadatos de publicaciones más grafo de citas más habilidades de autores

Esta pista es más difícil y solo debe ser aprobada si el equipo puede explicar claramente la alineación de los datos.

## Tipos de Proyectos Recomendados

El mejor ajuste para este curso es un `sistema de descubrimiento y recomendación`.

Eso significa que el resultado final debe responder preguntas como:

- ¿Qué ítems son similares?
- ¿Qué ítems pertenecen al mismo segmento latente?
- ¿Qué ítems deberían recomendarse a continuación?
- ¿Qué entidades son centrales en el grafo?
- ¿Qué cambios en el contenido o comportamiento se asocian con mejores resultados?

## Opciones de Proyecto Prohibidas o Débiles

Lo siguiente no es aceptable:

- Titanic
- Iris
- Pingüinos
- MNIST utilizado como un ejercicio de enseñanza estándar
- cualquier conjunto de datos escolar pequeño sin un desafío de ingeniería significativo
- cualquier proyecto con solo un CSV plano y sin flujo de trabajo (pipeline)
- cualquier proyecto con solo capturas de pantalla y sin código reproducible

Lo siguiente es técnicamente posible pero débil para este curso a menos que se extienda sustancialmente:

- predicción simple de salarios con una sola tabla
- regresión simple de precios de casas con una sola tabla
- cualquier proyecto sin una capa de interacción o una capa de grafos

## Tamaño del Equipo

Tamaño de equipo recomendado:

- `3 a 5` estudiantes por equipo

Cada equipo debe asignar al menos estos roles, incluso si un estudiante cubre más de uno:

- líder de ingeniería de datos
- líder de modelado y evaluación
- líder de informes y presentación

## Reglas del Conjunto de Datos

Cada equipo debe cumplir con todo lo siguiente:

1. Utilizar un conjunto de datos que no sea trivial en tamaño, estructura o dificultad de preprocesamiento.
2. Proporcionar un diccionario de datos.
3. Documentar todas las URLs de origen y la procedencia.
4. Explicar por qué el conjunto de datos elegido respalda la segunda mitad del curso, no solo la primera.
5. Evitar conjuntos de datos de referencia (benchmarks) triviales.
6. Si el conjunto de datos es demasiado grande, definir un subconjunto de trabajo justificado.
7. Si se combinan múltiples fuentes, documentar la lógica de emparejamiento.

## Ética y Reglas de la Plataforma

Estas reglas son obligatorias.

### General

- No realizar extracción (scraping) no autorizada de datos privados o de acceso controlado.
- No utilizar datos personales sin el consentimiento claro de los participantes.
- No redistribuir datos personales brutos recopilados de los participantes.
- Los identificadores sensibles deben ser anonimizados o cifrados (hashed) en los artefactos procesados, a menos que se documente un permiso explícito.

### Instagram

Los proyectos basados en Instagram están permitidos solo cuando los datos provienen de:

- exportaciones de participantes con consentimiento
- analítica de cuentas de negocios o creadores con consentimiento
- acceso a la API aprobado por la plataforma

Los equipos no deben extraer perfiles privados ni eludir las restricciones de la plataforma.

### LinkedIn

Los proyectos basados en LinkedIn están permitidos solo cuando los datos provienen de:

- exportaciones de participantes con consentimiento
- datos de administración de páginas con acceso válido
- acceso a la API aprobado por la plataforma

Los equipos no deben extraer perfiles personales sin permiso.

### Nota de Ética Requerida

Cada hito debe incluir una sección corta titulada `Nota de Ética y Acceso` que indique:

- de dónde provinieron los datos
- por qué el equipo tiene permitido usarlos
- qué riesgos existen respecto a los datos personales
- cómo se redujeron esos riesgos

## Estructura de Repositorio Requerida

El repositorio de cada equipo debe incluir una estructura equivalente a esta:

```text
proyecto/
  data/
    raw/
    interim/
    processed/
  notebooks/
  src/
  reports/
  artifacts/
  README.md
  requirements.txt o pyproject.toml
```

Los nombres exactos pueden variar, pero la separación entre datos brutos, procesados, código e informes debe ser explícita.

## Artefactos Técnicos Requeridos

Cada equipo debe producir:

1. un script o flujo de trabajo (pipeline) de ingestión
2. un directorio de conjunto de datos procesado
3. un diccionario de datos
4. un script o cuaderno de construcción de características
5. un script de evaluación
6. un script de construcción de grafos
7. un manual de instrucciones (runbook) que explique cómo reproducir los resultados
8. un artefacto de demostración final
- esto puede ser un cuaderno, CLI, un pequeño tablero (dashboard) o una pequeña API

Los proyectos que solo consistan en cuadernos (notebooks) no son suficientes.
Al menos parte del flujo de trabajo debe ser ejecutable desde scripts o comandos.

## Hitos Obligatorios

El proyecto tiene entregables parciales en las semanas 3, 5, 7, 10, 12 y 14.

### Semana 3: Carta del Conjunto de Datos y Conjunto de Datos Procesado V1

Objetivo:

- demostrar que el equipo tiene un dominio válido, una fuente de datos válida y una primera construcción de conjunto de datos reproducible

Entregables requeridos:

1. una propuesta de proyecto
- dominio
- declaración del problema
- pregunta esperada sobre el producto
- por qué el conjunto de datos es adecuado para el curso

2. un inventario de fuentes
- URLs de origen
- licencias o condiciones de acceso
- formatos de archivos brutos
- tamaño estimado

3. un borrador de esquema
- tablas de entidades
- claves
- uniones (joins) esperadas

4. un conjunto de datos procesado V1
- al menos una tabla limpia guardada en el disco

5. un borrador del diccionario de datos

6. un análisis de escala
- filas
- columnas
- datos faltantes
- estimación de dispersión o memoria

7. una nota de ética y acceso

Expectativa técnica:

- la ingestión debe ejecutarse desde un comando documentado

### Semana 5: Informe de Representación y Dimensionalidad

Objetivo:

- pasar de tablas brutas a representaciones significativas

Entregables requeridos:

1. una matriz o matrices de características
- numéricas
- texto
- codificación categórica
- características temporales si son relevantes

2. un informe de reducción de dimensionalidad
- PCA y/o SVD
- t-SNE opcional para visualización

3. una tabla comparativa
- varianza explicada o energía retenida
- error de reconstrucción cuando sea apropiado

4. un conjunto de visualizaciones
- al menos dos gráficos significativos

5. una breve interpretación técnica
- qué se aprendió sobre la dimensionalidad, redundancia o calidad de las características

Expectativa técnica:

- el flujo de trabajo de construcción de características debe ser reproducible

### Semana 7: Informe de Agrupamiento (Clustering) y Validación

Objetivo:

- segmentar el dominio y validar si la segmentación es significativa

Entregables requeridos:

1. un experimento de agrupamiento con K-means
2. un experimento de agrupamiento con DBSCAN u otro método de densidad justificado
3. una tabla de validación
- silueta (silhouette)
- inercia o métricas relacionadas con la densidad
- límites de interpretación

4. un análisis de perfil de clúster
- qué caracteriza a los clústeres

5. un análisis de fallas
- qué no se agrupó bien y por qué

Expectativa técnica:

- el equipo debe mostrar barridos de parámetros, no solo un resultado seleccionado a mano

### Semana 10: Motor de Recomendación, Clasificación o Decisión Predictiva

Objetivo:

- conectar el trabajo técnico a una tarea de decisión o clasificación

Entregables requeridos:

1. un sistema base (baseline)
- basado en contenido, basado en popularidad u otro sistema base simple

2. un sistema más sólido
- filtrado colaborativo
- factorización de matrices
- clasificación híbrida
- clasificación predictiva
- u otro modelo avanzado justificado

3. un informe de evaluación fuera de línea (offline)
- métricas
- definición del grupo de candidatos
- comparación con los sistemas base

4. un análisis de errores
- casos exitosos
- casos fallidos

5. una explicación de si el proyecto es de:
- recomendación
- clasificación (ranking)
- predicción
- segmentación que alimenta a la clasificación

Expectativa técnica:

- los equipos deben explicar su protocolo de evaluación claramente
- si afirman tener un sistema híbrido, deben documentar la alineación de los datos

### Semana 12: Informe de Analítica de Grafos y Centralidad

Objetivo:

- formalizar el grafo inducido por el dominio y utilizarlo para el análisis estructural

Entregables requeridos:

1. una definición del grafo
- nodos
- aristas
- pesos
- direccionalidad

2. un script de construcción de grafos

3. un informe de grafos
- componentes conectados
- grado o grado ponderado
- centralidad o PageRank

4. una sección comparativa
- clasificación por grafos frente a clasificación basada en popularidad o modelos

5. una nota de interpretación
- qué significa la estructura del grafo en el dominio

Expectativa técnica:

- las elecciones de definición del grafo deben estar justificadas

### Semana 14: Entrega Integrada Final y Defensa

Objetivo:

- entregar el sistema completo y defender su coherencia

Entregables requeridos:

1. un informe técnico final
2. un repositorio reproducible
3. un manual de instrucciones (runbook)
4. una presentación final
5. un artefacto de demostración final
6. un plan de monitoreo u operacionalización
7. una sección de limitaciones y trabajo futuro

Expectativa técnica:

- el proyecto debe ejecutarse desde pasos documentados
- el equipo debe mostrar artefactos y resultados procesados finales, no solo diapositivas

## Estructura del Informe Final

El informe final debe contener:

1. declaración del problema
2. contexto del dominio
3. fuentes del conjunto de datos y condiciones de acceso
4. esquema y diccionario de datos
5. preprocesamiento e ingeniería de características
6. análisis de dimensionalidad y representación
7. análisis de agrupamiento (clustering)
8. sistema de recomendación o clasificación
9. analítica de grafos
10. protocolo de evaluación
11. flujo de trabajo y reproducibilidad
12. ética y limitaciones
13. conclusiones finales


## Criterios de Evaluación Detallados

### Ingeniería de Datos

El equipo será evaluado por:

- corrección de la ingestión
- claridad del esquema
- calidad de los datos procesados
- calidad del diccionario de datos
- manejo de valores faltantes, duplicados y uniones

### Modelado y Análisis

El equipo será evaluado por:

- calidad de la representación
- justificación de los parámetros
- comparaciones con sistemas base
- rigor métrico
- calidad de la interpretación

### Capa de Grafos y Capa Avanzada

El equipo será evaluado por:

- validez de la construcción del grafo
- corrección del análisis de centralidad o PageRank
- conexión entre los resultados del grafo y la pregunta del producto

### Ingeniería y Reproducibilidad

El equipo será evaluado por:

- estructura del repositorio
- comandos claros
- artefactos guardados
- flujo de trabajo re-ejecutable
- evidencia de que el proyecto no depende de estados ocultos de cuadernos (notebooks)

### Defensa Final

El equipo será evaluado por:

- coherencia entre objetivo, datos, modelo y evaluación
- claridad de las decisiones técnicas
- honestidad sobre las limitaciones
- calidad de la defensa oral y respuestas técnicas

## Propuestas de Temas Sugeridas

Estos son ejemplos sólidos, no una lista exhaustiva.

### Propuesta 1: Recomendación de Noticias y Grafo de Temas

Construir un sistema que:

- represente artículos usando características de texto
- modele el comportamiento de clics o de lectura
- recomiende artículos
- construya un grafo de entidades o temas

### Propuesta 2: Motor de Descubrimiento de Negocios Locales

Construir un sistema que:

- modele negocios, reseñas, categorías y vecindarios
- agrupe negocios
- recomiende negocios
- construya grafos de negocio-negocio o de categorías

### Propuesta 3: Recomendación de Recetas y Grafo de Ingredientes

Construir un sistema que:

- represente recetas a partir de ingredientes e instrucciones
- agrupe estilos de recetas
- recomiende recetas
- construya un grafo de ingredientes

### Propuesta 4: Inteligencia de Contenido de Instagram

Construir un sistema que:

- represente publicaciones y subtítulos (captions)
- prediga o clasifique el potencial de compromiso (engagement)
- agrupe estrategias de contenido
- construya grafos de hashtags o menciones

### Propuesta 5: Inteligencia de Carreras y Habilidades de LinkedIn

Construir un sistema que:

- normalice roles y habilidades
- agrupe perfiles profesionales o familias de roles
- clasifique habilidades importantes
- construya grafos de habilidades o transiciones de carrera

### Propuesta 6: Recomendador de Comercio Electrónico de Nicho

Construir un sistema que:

- modele productos, metadatos, reseñas e interacciones
- agrupe productos
- recomiende productos
- construya grafos de co-ocurrencia o co-compra de productos

### Propuesta 7: Sistema de Descubrimiento de Artículos Académicos

Construir un sistema que:

- represente artículos usando títulos, resúmenes, temas y citas
- agrupe temas de investigación
- recomiende artículos
- clasifique artículos, autores o sedes (venues) mediante métodos de grafos

## Regla de Aprobación de Proyectos

Ningún proyecto es aprobado hasta que el instructor confirme que:

1. el conjunto de datos no es trivial
2. la fuente de datos está permitida
3. los temas de la segunda mitad del curso son factibles con los datos elegidos
4. el equipo tiene un plan de construcción creíble

Los equipos cuyo tema sea demasiado débil en la Semana 3 pueden verse obligados a pivotar.

## Estándar Técnico Mínimo para Aprobar

Para aprobar el proyecto, un equipo debe mostrar todo lo siguiente:

- un conjunto de datos procesado real
- al menos una representación de características rigurosa
- al menos un experimento de agrupamiento
- al menos un experimento de clasificación o recomendación
- al menos un análisis de grafos
- una ruta de construcción reproducible

Si falta alguna de estas capas, el proyecto puede ser calificado como incompleto.

## Nota Final para los Estudiantes

No elijan un proyecto porque parece fácil.
Elijan un proyecto cuya estructura de datos pueda sobrevivir todo el semestre.

La pregunta correcta no es:

> ¿Podemos entrenar un modelo con estos datos?

La pregunta correcta es:

> ¿Podemos construir un producto de datos coherente desde la ingestión hasta la clasificación, el análisis de grafos y la defensa final?
