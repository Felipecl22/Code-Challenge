# ETL (Extract, Transform, Load) en Python y BigQuery para Code Challenge Talento Digital y GLOBANT

Contenido del README:

Descripción del Proyecto

Para este proyecto se utilizó un archivo CSV llamado "Ventas Minoristas" el cual representa ventas minoristas mediante vía web del sector Europeo, se realizó un proceso de ETL mediante Python terminando con un archivo listo para su carga en BigQuery, también se utilizo SQL, consultas básicas, agrupamientos y segmentación de datos, se cargo la data en una tabla BigQuery en Google Cloud. Toda la documentación fue agregada a este repositorio GitHub el cual esta fusionado con mi máquina local, de donde se agregaron los archivos mediante la terminal, finalmente se creó una planificación en trello para una vista gráfica del proyecto, el cual esta plafinicado en sprints, mediante la metodología Agile.

Este proyecto tiene como finalidad postular a las Pasantías GLobant.

Descripción de la estructura de carpetas y archivos en el proyecto.

Dentro de la documentación se puede encontrar los siguientes archivos.

- Code Challenge, código en Python, proceso ETL.
- Ingesta de datos, código en Python y jpg, proceso ingesta de datos.
- SQLQuery_Code_Challenge, código SQL, proceso uso de SQL.
- Ventas Minoristas, archivo CSV utilizado en este proyecto.

Planificación Agile e Instrucciones:

Se planificaron 6 sprints para este proyecto, según instrucciones del Code Challenge:

Duración proyecto: 2 días.

Día 1:

Sprint 1: Utilizar Python o Java para escribir un script que simule la extracción de datos desde una fuente. Puede ser una API ficticia o un archivo CSV. Limpiar y transformar los datos: eliminar registros duplicados, completar, valores faltantes, etc.
Duración: 3 horas.
Objetivos: Realización del proceso ETL en Python.
Tareas: Configurar el entorno de desarrollo (Python ybibliotecas) y Desarrollar el script de extracción de datos desde el archivo CSV.
Entregables: CSV procesado y listo para la carga en BigQuery.

Sprint 2: Usar SQL para segmentar y agrupar la información. En esta fase, es recomendable usar SQL básico: consultas, agrupamientos, DDL, DML y filtros.
Duración: 3 horas.
Objetivos: Realización del proceso de consultas en SQL, utilizando SSMS.
Tareas: Crear base de datos en SSMS, Carga de archivo CSV creando una nueva tabla, realizar consultas.
Entregables: Archivo SQL con consultas.

Sprint 3: Utilizar la SDK de GCP para cargar los datos transformados en BigQuery.
Duración: 1 horas.
Objetivos: Crear tabla BigQuery.
Tareas: Registrarse en Google Cloud y crear tabla BigQuery con el archivo CSV procesado. 
Entregables: Tabla BigQuery lista para su utilización.

Día 2:

Sprint 4: Desarrollar un proceso simple que garantice que la ingestión de datos se realice de manera periódica (ejemplo: cada 24 horas) a través de Apache Airflow.
Duración: 5 horas.
Objetivos: Generar proceso de ingesta de datos, en este caso ingresar ventas cada 24hrs.
Tareas: Buscar documentación sobre como realizar este proceso en Python y generar el código.
Entregables: Script ingesta de datos y JPG de código.

Sprint 5: Usar GitHub para control de versiones. Debe haber evidencia de ramificación (branching) y fusión (merging) apropiados en el repositorio. Incluir un `README.md` con instrucciones sobre cómo ejecutar el proceso y entender el flujo de trabajo. Documentar los supuestos utilizados para el desarrollo del etl conrespecto a los datos.
Duración: 3 horas.
Objetivos: Usar terminal de máquina local y Python para clonar y agregar files al repositorio ya creado en GitHub.
Tareas: Acceder a GitHub, crear repositorio, enlazar máquina local con repositorio en GitHub.
Entregables: Repositorio listo para ser compartido con evidencia de ramas.

Sprint 6: Utilizar Trello para gestionar y organizar las tareas.
Duración: 1 horas.
Objetivos: Crear planificación de proyecto.
Tareas: Registrarse en en Trello y generar planificación.
Entregables: Gráfica de planificación.
