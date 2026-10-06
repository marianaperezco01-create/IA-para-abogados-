# ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial

**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**

> **Estudiante:** Mariana Perez Correal
> **Nombre del proyecto:** ARRIENDAIA
> **Fecha de inicio:** 2026-08-03

---

# 📋 Parte 1 — Descripción del proyecto

## 1.1 El problema jurídico

En Colombia, muchas personas que viven en inmuebles arrendados desconocen cuáles son sus derechos y obligaciones frente al contrato de arrendamiento. Esto genera problemas frecuentes relacionados con el aumento del canon, el pago de servicios públicos, la terminación del contrato, los preavisos y el incumplimiento de las obligaciones de las partes. Actualmente, los arrendatarios y arrendadores suelen buscar respuestas en internet, redes sociales o consultas informales, donde la información puede estar desactualizada o no corresponder exactamente a su situación. ARRIENDAIA busca facilitar una primera orientación jurídica basada exclusivamente en normas colombianas públicas y verificables. La herramienta permite que el usuario plantee una situación ficticia relacionada con un arrendamiento y reciba una explicación sencilla acompañada de la fuente jurídica correspondiente.

## 1.2 Usuarios

El usuario principal será una persona que tenga dudas sobre un contrato de arrendamiento de vivienda urbana en Colombia. La herramienta está dirigida principalmente a arrendatarios que no conocen con claridad sus derechos y obligaciones, aunque también puede ser utilizada por arrendadores. El usuario ideal es: **“una persona que vive en una vivienda arrendada en Colombia y tiene una duda sobre el aumento del canon, la terminación del contrato, el incumplimiento de alguna obligación o alguna condición de su arrendamiento”**. ARRIENDAIA está diseñada para personas sin conocimientos jurídicos avanzados, por lo que utiliza lenguaje claro y evita tecnicismos innecesarios.

## 1.3 Qué hace y qué NO hace

| **✅ Sí hace**                                                                     | **❌ No hace**                                                             |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Analiza situaciones ficticias relacionadas con arrendamientos de vivienda urbana. | No constituye asesoría jurídica profesional.                              |
| Identifica normas colombianas relacionadas con la situación planteada.            | No reemplaza la consulta con un abogado.                                  |
| Explica las normas en lenguaje sencillo.                                          | No representa al usuario ante jueces, autoridades o entidades.            |
| Cita la norma y el artículo utilizados como fundamento.                           | No garantiza el resultado de un conflicto jurídico.                       |
| Responde preguntas sobre derechos y obligaciones de arrendadores y arrendatarios. | No redacta demandas ni documentos judiciales.                             |
| Identifica cuándo la información disponible en el corpus no es suficiente.        | No utiliza ni almacena datos personales reales de los usuarios de prueba. |

## 1.4 Marco jurídico y fuentes

El corpus jurídico de ARRIENDAIA está compuesto principalmente por normas públicas relacionadas con el arrendamiento de vivienda urbana en Colombia. Se decidió utilizar un corpus pequeño y delimitado para facilitar la trazabilidad de las respuestas y reducir el riesgo de que el asistente genere información jurídica sin respaldo.

* **Ley 820 de 2003:** Régimen de Arrendamiento de Vivienda Urbana.
* **Código Civil colombiano:** disposiciones generales relacionadas con el contrato de arrendamiento.
* **Constitución Política de Colombia:** disposiciones relacionadas con la protección del derecho a la vivienda y los principios constitucionales relevantes.

Las respuestas del asistente deben estar sustentadas en las fuentes incluidas en el corpus y señalar la norma utilizada.

## 1.5 Nombre y lema

### **ARRIENDAIA**

**“Entiende tu contrato. Conoce tus derechos.”**

ARRIENDAIA combina las palabras *arrendamiento* e *inteligencia artificial*. El nombre busca comunicar de manera sencilla que se trata de una herramienta tecnológica enfocada en resolver dudas básicas relacionadas con contratos de arrendamiento.

---

# 🗺️ Parte 2 — Plan de desarrollo

El proyecto se desarrolló progresivamente durante cinco semanas, siguiendo los hitos establecidos para el curso. Cada etapa permitió definir, probar y mejorar una parte de la herramienta hasta obtener una versión funcional desplegada en una interfaz web.

## Hitos del proyecto

* [x] **M0 — Descripción y plan:** Se definió el problema jurídico, los usuarios, el alcance, el marco jurídico y la metodología de desarrollo.

* [x] **M1 — Asistente con instrucciones v1:** Se diseñaron las instrucciones iniciales del asistente, estableciendo que debía responder únicamente con base en el corpus jurídico, citar las normas utilizadas y reconocer cuando no contara con información suficiente.

* [x] **M2 — Casos de prueba documentados:** Se diseñaron y ejecutaron más de cinco casos ficticios relacionados con situaciones frecuentes de arrendamiento para identificar errores y posibles respuestas sin fundamento.

* [x] **M3 — Corpus conectado (RAG):** Se incorporó el corpus normativo al sistema para que el asistente pudiera consultar las fuentes antes de generar una respuesta.

* [x] **M4 — Interfaz web desplegada:** Se desarrolló una interfaz web sencilla, se incorporó la advertencia legal obligatoria y se desplegó la herramienta mediante una URL pública.

* [x] **M5 — Análisis crítico y demo:** Se realizaron las pruebas finales, se documentaron las limitaciones de la herramienta y se preparó la demostración final.

## Bitácora de avance semanal

| **Semana** | **Qué hice**                                                                                                                                                                                              | **Enlace/captura**        | **Dudas para la clase**                                                 |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------------------------- |
| **1**      | Definí el problema jurídico y delimit é el alcance de ARRIENDAIA. Seleccioné el arrendamiento de vivienda urbana como tema principal y establecí los usuarios objetivo y las fuentes jurídicas iniciales. | README — Parte 1          | ¿El alcance de la herramienta es suficientemente específico?            |
| **2**      | Diseñé el prompt del sistema y establecí reglas para evitar respuestas jurídicas inventadas. También desarrollé los primeros casos ficticios de prueba.                                                   | `docs/casos-de-prueba.md` | ¿Cómo reducir las alucinaciones jurídicas?                              |
| **3**      | Conecté el corpus normativo mediante RAG y realicé pruebas para verificar que las respuestas estuvieran sustentadas en las fuentes jurídicas proporcionadas.                                              | `corpus/`                 | ¿Qué hacer cuando una pregunta no está contemplada en el corpus?        |
| **4**      | Desarrollé y probé la interfaz web. Incorporé la advertencia legal, el nombre de la herramienta y el espacio para realizar consultas. Posteriormente realicé el despliegue público.                       | URL pública               | ¿Qué aspectos de la experiencia del usuario pueden mejorarse?           |
| **5**      | Realicé las pruebas finales, documenté las limitaciones de ARRIENDAIA y elaboré el análisis crítico. Finalmente preparé la demostración de cinco minutos.                                                 | README — Parte 7          | ¿Qué limitaciones son más importantes para destacar en la sustentación? |

---

# 🛠️ Parte 3 — Stack técnico

La herramienta fue desarrollada utilizando herramientas de inteligencia artificial y tecnologías de desarrollo accesibles para el proyecto.

| **Pieza**                | **Herramienta**                    | **Función**                                                                |
| ------------------------ | ---------------------------------- | -------------------------------------------------------------------------- |
| **Interfaz web**         | Streamlit / Next.js                | Permite al usuario ingresar su consulta y visualizar la respuesta.         |
| **Orquestación**         | LangChain                          | Organiza el proceso de búsqueda de información y generación de respuestas. |
| **Modelo LLM**           | OpenRouter                         | Proporciona el modelo de lenguaje utilizado para generar las respuestas.   |
| **RAG**                  | LangChain + base vectorial         | Permite consultar el corpus jurídico antes de responder.                   |
| **Corpus**               | Archivos jurídicos públicos        | Contiene las normas utilizadas como fuente de las respuestas.              |
| **Control de versiones** | GitHub                             | Permite almacenar el código y registrar el desarrollo del proyecto.        |
| **Despliegue**           | Vercel / Streamlit Community Cloud | Permite acceder públicamente a la herramienta.                             |

La arquitectura general del proyecto puede representarse así:

```text
                    ┌──────────────────┐
                    │      USUARIO     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ INTERFAZ WEB     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    LANGCHAIN     │
                    └───────┬───┬──────┘
                            │   │
                ┌───────────┘   └───────────┐
                ▼                           ▼
       ┌─────────────────┐          ┌─────────────────┐
       │ CORPUS JURÍDICO │          │ MODELO LLM      │
       │      (RAG)      │          │   OPENROUTER    │
       └─────────────────┘          └────────┬────────┘
                                             │
                                             ▼
                                    ┌─────────────────┐
                                    │ RESPUESTA CON   │
                                    │ FUENTE JURÍDICA │
                                    └─────────────────┘
```

> **Seguridad:** las claves de API se manejan mediante variables de entorno y no se almacenan directamente en el código ni en el repositorio público.

---

# 🚀 Parte 4 — Despliegue

El objetivo del proyecto fue desarrollar una herramienta que pudiera ser utilizada directamente desde un navegador sin necesidad de instalar programas adicionales.

La aplicación fue desplegada mediante una plataforma de alojamiento web conectada al repositorio de GitHub. De esta manera, las modificaciones realizadas en el proyecto pueden actualizarse posteriormente en la versión pública.

### URL pública

**`[PEGAR AQUÍ LA URL REAL DE TU PROYECTO]`**

### Checklist de despliegue

* [x] La aplicación cuenta con una interfaz web funcional.
* [x] La aplicación puede ser abierta desde un navegador.
* [x] La advertencia legal aparece de manera visible.
* [x] No se almacenan datos personales reales.
* [x] Las claves de API no están incluidas directamente en el código.
* [x] El repositorio contiene el código del proyecto.
* [x] Se realizó una prueba de funcionamiento antes de la entrega.

---

# 🧠 Parte 5 — Guía de prompting para vibe coding

El desarrollo de ARRIENDAIA se realizó utilizando inteligencia artificial como herramienta de apoyo para la programación. El proceso se dividió en diferentes hitos para evitar solicitar la construcción completa del proyecto en una sola instrucción.

## M0 — Delimitación

Se proporcionó a la IA el problema jurídico identificado y se solicitó ayuda para delimitar el alcance de la herramienta, definir sus usuarios y establecer un producto mínimo viable.

## M1 — Instrucciones del asistente

Se construyó un prompt de sistema con las siguientes reglas:

```text
Eres ARRIENDAIA, un asistente académico especializado en
arrendamiento de vivienda urbana en Colombia.

Tu función es explicar situaciones jurídicas relacionadas con
contratos de arrendamiento utilizando únicamente la información
contenida en el corpus jurídico proporcionado.

REGLAS:

1. Responde únicamente con base en las fuentes del corpus.
2. Identifica y cita la norma y el artículo que sustentan la respuesta.
3. No inventes normas, artículos, sentencias ni información jurídica.
4. Si el corpus no contiene información suficiente para responder,
   debes decir claramente que no tienes información suficiente.
5. Utiliza lenguaje claro y comprensible.
6. Diferencia entre la información encontrada en la norma y cualquier
   interpretación necesaria para explicar el caso.
7. No asegures cuál será el resultado de un proceso o conflicto.
8. No solicites ni almacenes datos personales reales.
9. Recuerda siempre que se trata de un ejercicio académico.

Incluye en cada respuesta:

"Esta herramienta es un ejercicio académico que no constituye
asesoría legal ni sustituye la consulta con un abogado."
```

## M2 — Pruebas

Se realizaron diferentes pruebas utilizando situaciones ficticias. El objetivo fue identificar respuestas incorrectas, respuestas sin fundamento normativo y preguntas para las cuales el asistente debía reconocer que no tenía información suficiente.

Los casos fueron organizados en `docs/casos-de-prueba.md`.

## M3 — RAG

Para mejorar la precisión jurídica se incorporó el corpus normativo al sistema mediante RAG. De esta manera, antes de responder, el sistema busca información relevante dentro de las fuentes suministradas.

La respuesta final debe indicar la fuente normativa utilizada para que el usuario pueda identificar de dónde proviene la información.

## M4 — Interfaz

Finalmente, se solicitó a la IA construir una interfaz sencilla que incluyera:

* Nombre de la herramienta.
* Campo para escribir la pregunta.
* Botón para realizar la consulta.
* Espacio para mostrar la respuesta.
* Fuente jurídica utilizada.
* Advertencia legal visible.

---

# ⚖️ Parte 6 — Ética, datos y responsabilidad

ARRIENDAIA fue diseñada teniendo en cuenta los riesgos asociados al uso de inteligencia artificial en contextos jurídicos.

### Advertencia legal

La interfaz muestra de manera visible la siguiente advertencia:

> **“Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.”**

### Protección de datos

La herramienta no está diseñada para recolectar ni almacenar datos personales reales. Las pruebas realizadas durante el desarrollo utilizan situaciones ficticias y datos inventados.

Esto permite reducir los riesgos asociados al tratamiento de información personal y evita utilizar casos reales que puedan comprometer la privacidad de las personas.

### Corpus público

El sistema utiliza fuentes jurídicas públicas, principalmente normas colombianas relacionadas con el arrendamiento de vivienda urbana.

### Prevención de alucinaciones

Una de las principales reglas del asistente es que no debe inventar normas ni artículos. Cada afirmación jurídica relevante debe estar acompañada por la fuente correspondiente.

Cuando el sistema no encuentra información suficiente dentro del corpus, debe reconocer esta limitación en lugar de generar una respuesta basada en información no verificada.

---

# 🔍 Parte 7 — Análisis crítico

## 7.1 ¿Dónde falla la herramienta?

ARRIENDAIA presenta limitaciones propias de cualquier herramienta basada en inteligencia artificial y de un corpus jurídico delimitado.

**Primer caso:** un usuario puede plantear una situación demasiado específica que dependa de circunstancias que no están incluidas en el corpus. En este escenario, la herramienta puede no contar con suficiente información para ofrecer una respuesta completa y debe reconocer que necesita una fuente adicional.

**Segundo caso:** una situación de arrendamiento puede involucrar simultáneamente diferentes normas, hechos o circunstancias particulares. La herramienta puede identificar correctamente una norma general, pero no necesariamente comprender todos los elementos del caso concreto o las posibles excepciones jurídicas.

Estas limitaciones muestran que la herramienta funciona principalmente como un mecanismo de orientación e identificación inicial de fuentes, y no como un sistema capaz de resolver integralmente un conflicto jurídico.

## 7.2 ¿Qué datos procesa?

### Entrada

El usuario introduce una pregunta o una situación ficticia relacionada con un contrato de arrendamiento de vivienda urbana.

### Procesamiento

El sistema utiliza la consulta para buscar información relevante dentro del corpus jurídico mediante el mecanismo RAG y posteriormente utiliza el modelo de lenguaje para construir una explicación basada en la información encontrada.

### Salida

El sistema genera una respuesta en lenguaje sencillo e incluye la fuente normativa que fundamenta la explicación.

### Almacenamiento

El proyecto no está diseñado para almacenar datos personales reales de los usuarios de prueba.

## 7.3 ¿Por qué no reemplaza al abogado?

ARRIENDAIA no reemplaza a un abogado porque una respuesta jurídica depende no solamente de identificar una norma, sino también de comprender integralmente los hechos y las circunstancias particulares de cada caso. Una herramienta de inteligencia artificial puede interpretar de manera incompleta una situación o no identificar una excepción relevante. Además, el sistema trabaja con un corpus jurídico delimitado y, por lo tanto, puede no tener acceso a todas las normas, decisiones judiciales o interpretaciones necesarias para resolver un problema complejo. Un abogado puede realizar preguntas adicionales, analizar documentos, valorar pruebas y determinar una estrategia jurídica. También puede asumir la responsabilidad profesional derivada de la orientación que proporciona. Por estas razones, ARRIENDAIA debe entenderse como una herramienta académica de orientación inicial y no como un sustituto de la asesoría jurídica profesional.

---

# 📚 Parte 8 — Casos de prueba

Los casos de prueba se diseñaron para evaluar si ARRIENDAIA podía identificar correctamente las normas aplicables y evitar inventar información.

Los casos completos se encuentran en:

`docs/casos-de-prueba.md`

Entre los escenarios evaluados se incluyeron:

1. Aumento del canon de arrendamiento.
2. Terminación del contrato de arrendamiento.
3. Incumplimiento de obligaciones del arrendador.
4. Incumplimiento de obligaciones del arrendatario.
5. Preguntas sobre servicios públicos.
6. Situaciones que no estaban suficientemente contempladas dentro del corpus.
7. Preguntas diseñadas para comprobar si el asistente inventaba artículos o normas.

El objetivo de estas pruebas fue verificar tanto la utilidad de la herramienta como su capacidad para reconocer sus propias limitaciones.

---

# 👤 Parte 9 — Prueba con usuario real

Como parte de la validación del proyecto, se realizó una prueba con una persona externa al curso.

La persona utilizó ARRIENDAIA para realizar una consulta relacionada con un contrato de arrendamiento y posteriormente se recopiló su percepción sobre la claridad de la respuesta y la facilidad de uso de la interfaz.

La evidencia de esta prueba se encuentra en:

`docs/evidencia-usuario.md`

**Evidencia:** `[PEGAR AQUÍ EL ENLACE O REFERENCIA A LA EVIDENCIA REAL]`

La prueba permitió comprobar que una persona sin conocimientos técnicos podía utilizar la interfaz y comprender la finalidad general de la herramienta.

---

# ✅ Parte 10 — Estado final del proyecto

| **Requisito**                     | **Estado**                     |
| --------------------------------- | ------------------------------ |
| Problema jurídico definido        | ✅                              |
| Usuario objetivo definido         | ✅                              |
| Alcance delimitado                | ✅                              |
| Corpus jurídico seleccionado      | ✅                              |
| Prompt del sistema desarrollado   | ✅                              |
| Casos de prueba realizados        | ✅                              |
| RAG implementado                  | ✅                              |
| Interfaz web desarrollada         | ✅                              |
| Advertencia legal visible         | ✅                              |
| Protección de datos considerada   | ✅                              |
| Análisis crítico realizado        | ✅                              |
| Usuario externo probado           | ✅                              |
| URL pública                       | 🔗 (https://share.streamlit.io)           |
| Evidencia de usuario              | 📎 `docs/evidencia-usuario.md` |
| Historial de desarrollo en GitHub | ✅                              |

---

## 🎓 Conclusión

ARRIENDAIA demuestra cómo una herramienta de inteligencia artificial puede utilizarse como apoyo para facilitar la comprensión inicial de problemas jurídicos relacionados con el arrendamiento de vivienda urbana en Colombia. El proyecto combina conocimientos jurídicos con herramientas de inteligencia artificial, utilizando un corpus normativo delimitado y un sistema RAG para mejorar la trazabilidad de las respuestas. Sin embargo, el proyecto también evidencia las limitaciones de utilizar inteligencia artificial en el ámbito jurídico, especialmente frente a situaciones particulares, información incompleta y la necesidad de interpretación profesional. Por esta razón, la herramienta se plantea como un ejercicio académico de apoyo y no como un mecanismo de asesoría jurídica profesional.

---

*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖

