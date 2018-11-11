# Práctica 1: Web Scraping

## Asignatura: Tipología y ciclo de vida de los datos

## Descripción de la práctica

Aquí se encuentran los ficheros correspendientes a la resolución de la PRACTICA 1 de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC).
En esta práctica se han empleado diversas técnicas de web scraping, utilizando para ello un script escrito en Python, que será el encargado de extraer los datos de una web dedicada a la venta de maquetas de la serie de anime "Gundam", _(https://www.1999.co.jp/eng/gundam/)_ y con dichos datos, generar un dataset en formato .csv 

## Miembros del equipo

La práctica ha sido elaborada individualmente por **Luis Manuel Martín Guerra**

## Bibliotecas necesarias para la ejecución del script

Para el correcto funcionamiento del script, es necesario tener insalada la biblioteca **BeautifulSoup4**

Se puede instalar mediante el comando _pip install beautifulsoup4_

## Modo de empleo

El script se debe ejecutar de la siguiente manera:

python gunpla_main.py

## Ficheros de la práctica

Los ficheros se organizan en tres directorios diferentes:

* **scr**/ Contiene los ficheros del **_código fuente de los scripts_** empleados en el web scraping y creación del .csv:
  
     **scr/gunpla_main.py**: es el archivo principal, y el que arranca el proceso de web scraping. Se emplea como punto de acceso a la ejecución del proceso y nos permitirá en un futuro ampliar las funcionalidades del script.
     
     **scr/gunpla_scraper.py**: es el fichero que contiene la implementación de la clase _GunplaScraper_, que contiene los métodos que se emplean para las diferenes fases del data scraping de la web [HobbySearch](https://www.1999.co.jp/eng/gundam/): _Captura de categorías, Captura de enlaces a productos, Extracción de datos de productos y generación del fichero de datos_. 
     
* **csv**/ Contiene el fichero _gunpla.csv_ obtenido como resultado del web scraping realizado por el script _gunpla_scraper.py_.

* **pdf**/ Contiene el documento _practica1_luimargu.pdf_, que contiene las respuestas a las características del dataset solicitadas en el enunciado de la práctica. 

## Recursos

1. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2018). _Web Scraping with Python: Collecting Data from the Modern Web (2nd Edition)_. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
3. Subirats, L., Calvo, M. (2018). _Web Scraping_. Apuntes de la asignatura Tipología y ciclo de vida de los datos. Universitat Oberta de Catalunya,
4. Lutz, M. (2016). _Learning Python (5th Edition)_. O'Reilly Media, Inc.
