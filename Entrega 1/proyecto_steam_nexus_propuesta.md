# Propuesta de Proyecto: Steam Nexus

## 1. Declaración del Proyecto

**Dominio:** Entretenimiento Digital y Videojuegos (Ecosistema Steam).

**Problema:** Con más de 100,000 juegos en Steam, los usuarios sufren de "parálisis por análisis". Los sistemas de recomendación actuales suelen basarse en popularidad masiva, ignorando nichos emergentes y la evolución técnica de los géneros.

**Pregunta del Producto:** ¿Podemos descubrir segmentos latentes de juegos y predecir el éxito de nuevas combinaciones de géneros utilizando inteligencia de grafos y procesamiento de lenguaje natural?

**Idoneidad para el curso:** El dataset de Steam es masivo y complejo. Permite aplicar todas las capas requeridas:
- Ingestión de metadatos y reseñas.
- Ingeniería de características con NLP (descripciones) y Audio (trailers - opcional).
- Agrupamiento de géneros híbridos.
- Recomendación basada en grafos de tags y co-ocurrencia.

## 2. Inventario de Fuentes

- **Nombre:** Steam Dataset 2025: Multi-Modal Gaming Analytics Platform.
- **Origen:** [Kaggle](https://www.kaggle.com/datasets/steam-dataset-2025).
- **Licencia:** CC BY-NC-SA 4.0.
- **Formato:** CSV y PostgreSQL Dump.
- **Tamaño Estimado:** ~239,664 aplicaciones y >1,000,000 reseñas (~2GB+).

## 3. Borrador de Esquema

### Tablas Principales:
1. **Games (Apps):** `app_id`, `name`, `release_date`, `price`, `description`, `developer`, `publisher`.
2. **Genres/Tags:** `tag_id`, `tag_name`.
3. **Game_Tags (Join):** `app_id`, `tag_id`.
4. **Reviews:** `review_id`, `app_id`, `user_id`, `review_text`, `score`, `playtime_at_review`.

### Uniones Esperadas:
- `Games` <-> `Game_Tags` <-> `Genres` para análisis de grafos de tags.
- `Games` <-> `Reviews` para sistemas de recomendación colaborativos.

## 4. Análisis de Escala (Estimación)
- **Filas:** ~240k juegos, ~1M reseñas.
- **Columnas:** ~20-30 por tabla.
- **Memoria:** Estimada en 1.5GB - 3GB en RAM (se usará procesamiento por chunks o subconjuntos si es necesario).
- **Datos Faltantes:** Se espera un 10-15% en descripciones y precios de juegos antiguos.

## 5. Nota de Ética y Acceso
- **Origen:** Datos públicos recolectados mediante la API oficial de Steam (Steam Web API).
- **Permiso:** El uso es para fines académicos y de investigación. Se respeta la licencia CC de la fuente.
- **Riesgos de Datos Personales:** El dataset utiliza IDs de usuario anónimos de Steam. No se procesarán nombres reales, correos ni datos de pago.
- **Reducción de Riesgos:** Se eliminarán cualquier mención de información sensible en las reseñas mediante limpieza de texto.

---

## Anexo: Borrador de Diccionario de Datos (Games Table)

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `app_id` | Integer | ID único del juego en Steam. |
| `name` | String | Título del videojuego. |
| `release_date` | Date | Fecha de lanzamiento oficial. |
| `price` | Float | Precio actual en USD. |
| `genres` | List[String] | Lista de géneros asociados. |
| `description` | Text | Descripción detallada (para NLP). |
| `positive_reviews`| Integer | Conteo de reseñas positivas. |
| `negative_reviews`| Integer | Conteo de reseñas negativas. |
