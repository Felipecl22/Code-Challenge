# CODE CHALLENGE

'''
Desarrollar un pequeño proceso de ETL que recoja datos desde una fuente, los transforme y luego los cargue en BigQuery. Durante este proceso, es necesario aplicar metodologías Agile y
utilizar herramientas de control de versiones.

Pasos: 

1# Utilizar Python o Java para escribir un script que simule la extracción de datos desde una fuente. Puede ser una API ficticia o un archivo CSV.
2# Limpiar y transformar los datos: eliminar registros duplicados, completar valores faltantes, etc.
3# Usar SQL para segmentar y agrupar la información.
4# En esta fase, es recomendable usar SQL básico: consultas, agrupamientos, DDL, DML y filtros.
5# Utilizar la SDK de GCP para cargar los datos transformados en BigQuery.
6# El candidato o candidata debe garantizar que la estructura de la tabla en BigQuery sea adecuada para los datos.
7# Desarrollar un proceso simple que garantice que la ingestión de datos se realice de manera periódica (ejemplo: cada 24 horas). Esto se puede hacer a través de
herramientas como Apache Airflow o mediante cron jobs.
8# Usar Git para control de versiones.
9# Debe haber evidencia de ramificación (branching) y fusión (merging) apropiados en el repositorio.
10# Incluir un `README.md` con instrucciones sobre cómo ejecutar el proceso y entender
el flujo de trabajo. Documentar los supuestos utilizados para el desarrollo del etl con respecto a los datos.
11# Organizar el desarrollo del proyecto en sprints. Documentar brevemente las tareas realizadas en cada sprint y los obstáculos encontrados.
12# Utilizar herramientas como Trello o Jira para gestionar y organizar las tareas.
'''


# Para este desafío vamos a utilizar un archivo CSV llamado Online Retail, el cual contiene ventas minoristas en línea en el sector Europeo, entre 2010 al 2011, esta data contiene 592 entradas.

############################################
# Paso 1: Configurar y definir el directorio para acceder al archivo CSV.

import os # Importar os para conocer nuestro directorio.

# creando un variable llamada mi_directorio:
mi_directorio = os.getcwd() 

# Definiendo nuevo directorio:
nuevo_directorio = "C:\\Users\\Felipe\\Desktop\\Python\\Files"
os.chdir(nuevo_directorio) # Change directory.

# Cargando el archivo CSV utilizando pandas:
import pandas as pd
df = pd.read_csv('Ventas Minoristas.csv', sep=';') # Notar que nuestro archivo esta separado por ; (punto y coma) y se debe especificar que es de este modo sino pandas leera el archivo con , (coma).

############################################
# Paso 2: Exploración inicial de los datos, limpieza y transformación.

# Vista rápida de nuestra dataframe:
df.head(5)  
df.tail(5)

# Obtener una descripción de nuestra dataframe, número total de columnas con conteo de not null, tipo de datos y memoria utilizada. 
df.info() 
df.shape 
# Notar que las columnas "Non-Null Count" muestren 599 para cada columna significa que todas las filas (entradas) en la DataFrame tienen valores no nulos en esas columnas.
# Sin embargo, la primera fila, que generalmente contiene los nombres de las columnas (encabezados), no se cuenta como una entrada de datos, por esta razón cuenta 591 entradas. 
# La dataframe contiene 591 filas y 8 columnas (shape).

# Hemos visto que la dataframe no contiene non-null data, pero vamos a asegurarnos que sea justamente de este modo:

missing_values = df.isnull().sum() # Nuestra dataframe no contiene NA values.
missing_values
sum(df.isnull().sum()) # Suma total de NA's.  
(missing_values / len(df)) * 100  # Porcentaje total de NA's.
# Como podemos ver ninguna columna presenta NA's.

# Antes de realizar cualquier cambio en la data crearemos una copia para evitar perder nuestra información.
df1 = df.copy()

# Buscando valores duplicados, esto es un poco tricky porque tenemos las columnas Invoice_No, Stock_Code e Invoice_Date, todas esta columnas pueden presentar valores repetidos, dado que un producto puede presentar,
# la misma factura para diferentes productos vendidos y viceversa pero no tener la misma Invoice_Date, por ello vamos a filtrar la data en base a estas 3 columnas para cerciorse que no tengamos valores duplicados.

verificar_duplicados = df1[df1.duplicated(subset=['Invoice_No', 'Stock_Code', 'Invoice_Date'], keep=False)]
verificar_duplicados

# Como podemos ver existen valores duplicados que tienen las 3 condiciones iguales, por ello es necesario quitar estos valores duplicados.
df1.drop_duplicates(subset=['Invoice_No', 'Stock_Code', 'Invoice_Date'], keep='first', inplace=True) 

# Utilizo subset para especificar que columnas considerar para la identificación de valores duplicados
# Utilizo Keep= 'first' para identificar la primera ocurrencia de valor duplicado.
# Utilizo inplace=True para realizar los cambios de forma inmediata en la dataframe evitando tener que crear una nueva variable.

df1.duplicated().sum() # Podemos verificar que la data ya no contiene valores duplicados. 
df1.shape              # Ahora la dataframe contiene 584 filas no 591 filas.

# Antes de continuar vamos a cambiar los nombres de las columnas para un mejor entendimiento:
df1.columns # Como podemos ver, las columnas tienen _ y otras no por ello vamos a estandarizar los nombre para tener nombres en español y sin otros caracteres más que palabras.

# Rename column names
df1.rename(columns={'Invoice_No': 'Factura', 
                    'Stock_Code': 'NumeroStock',
                    'Description': 'Descripcion',
                    'Quantity': 'Cantidad',
                    'Invoice_Date': 'Fecha',
                    'UnitPrice': 'PrecioUnitario',
                    'Customer_ID': 'IDcliente',
                    'Country': 'Pais',
                    }, inplace=True) # First the name of the actual column second the name you want to give to the column.
df1.columns # Verificamos los cambios realizados.
df1.head(5) # Damos un vistazo a la dataframe. 

# Ahora vamos a verificar por valores únicos en cada columna excepto en Factura, NumeroStock, cantidad, Fecha y Precio Unitario.

df1['Descripcion'].unique()  # Verificamos cada uno de los productos vendidos de la columna Descripcion.
df1['Descripcion'].nunique() # Tenemos 65 tipos de productos.

df1['IDcliente'].unique()  # Verificamos cada uno de los clientes de la columna IDcliente.
df1['IDcliente'].nunique() # Tenemos 264 tipos de clientes.

df1['Pais'].unique()  # Verificamos cada uno de los clientes de la columna IDcliente.
# Podemos darnos cuenta que existen Nombre de países que fueron ingresados incorrectamente estos son: Fracne, United Kindomg y German. Es necesario entonces corregir estas entradas.

# Primero encontramos para cada Pais los valores mal ingresados y luego los reemplazamos por los correctos.
df1.loc[df1['Pais'].str.startswith('F'),:]
# Corregimos.
df1['Pais'] = df1['Pais'].replace('Fracne', 'France')
# Verificamos
df1['Pais'].unique() # Como podemos ver solo existe France.

# Analogamente realizamos el mismo procedimiento para los otros errores encontrados en los nombres de los países.

df1.loc[df1['Pais'].str.startswith('G'),:]
# Corregimos.
df1['Pais'] = df1['Pais'].replace('German', 'Germany')
# Verificamos
df1['Pais'].unique() # Como podemos ver solo existe France.

df1.loc[df1['Pais'].str.startswith('G'),:]
# Corregimos.
df1['Pais'] = df1['Pais'].replace('United Kindomg', 'United Kingdom')
# Verificamos
df1['Pais'].unique() # Como podemos ver solo existe France.

# Verificamos los datatypes de cada columna y transformamos en los datatypes correctos que nos permitan realizar cálculos de forma correcta en el futuro.

df1.dtypes 

# Podemos ver que algunas columnas estan en formato object e int, necesitamos cambiar las siguientes: 
# Descripcion como str, Fecha a datetime con formato %d-%m-%Y, PrecioUnitario como float aqui necesitamos primero cambiar la coma por puntos y luego a float y por último Pais a str.

# Cambiar las columnas a los tipos de datos adecuados

df1['Descripcion'] = df1['Descripcion'].astype(str)
df1['Fecha'] = pd.to_datetime(df1['Fecha'], format='%d-%m-%Y')
df1['PrecioUnitario'] = df1['PrecioUnitario'].str.replace(',', '.').astype(float)  # Cambiar comas a puntos y convertir a float
df1['Pais'] = df1['Pais'].astype(str)

# Verificar los tipos de datos resultantes
print(df1.dtypes)
df1.head(5) # Vista rápida de la dataframe corregida.

#########################################################################################################################################################################################
# Ya hemos realizado el proceso de carga, limpieza y transformación necesaria a la data que posteriormente será cargada en SSMS como base de datos para realizar consultas en SQL Server.
#########################################################################################################################################################################################

# El último paso es exportar el archivo en un CSV para su uso posterior.

df1.to_csv('Ventas Minoristas.csv', index=False)

# FIN CÓDIGO.
