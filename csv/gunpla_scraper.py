import csv
import time
from math import ceil
from urllib.request import urlopen
from bs4 import BeautifulSoup


class GunplaScraper:

    def __init__(self):
        self.url = urlopen('https://www.1999.co.jp/eng/gundam/')
        self.data = []
        self.categories = []
        self.product = []
        self.category_links = []

    @staticmethod
    def __get_categories_links(url):
        bs = BeautifulSoup(url, 'html.parser')
        # Obtenemos los enlaces de los productos relacionados con Gunplas
        print("Procesando enlaces referentes a Gunplas\n")
        gunpla_links = bs.body.find_all('a', {'class': {'LListTyp3'}})
        number = 0
        category = 0
        categories_links = []
        for link in gunpla_links:
            if 'href' in link.attrs:
                if category != 6:
                    category += 1

                else:
                    categories_links.append('https://www.1999.co.jp'+link.attrs["href"])
                    number += 1
        # Eliminamos los enlaces que no corresponden a gunplas, empezando por el final de la lista.
        while number != 12:
            categories_links.pop(number - 1)
            number -= 1
        print("Categorías analizadas:", number)
        return categories_links

    @staticmethod
    def __get_category_products(urls):
        gunpla_list = []
        count = len(urls)
        print("Procesando categorías obtenidas\n")
        for url in urls:
            print("Procesando categoría:", count)
            # Cargamos el enlace que se nos pasa
            html = urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')

            # Obtenemos el número de productos en por categoría

            items = soup.body.find('div', {'class': {'list_kensu02'}})
            item = items.text
            numero_productos = ''
            for letter in item:
                if letter != ' ':
                    numero_productos = numero_productos + letter
                else:
                    break

            numero_productos = int(numero_productos)
            paginas = ceil((numero_productos / 40))
            print("Hay:", numero_productos, "productos en esta categoría", ",repartidos en", paginas,
                  "páginas de búsqueda")

            # Formateamos el enlace de la categoría, para poder ir avanzando por cada página de búsqueda

            master_link = url.split('list')[0]
            category_link = url.split('list')[1].split('/')[1]

            # Obtenemos los enlaces de los productos, para cada página de búsqueda que hemos encontrado

            while paginas > 0:
                final_link = (master_link + 'list/' + category_link + '/0/' + str(paginas))
                html = urlopen(final_link)
                soup = BeautifulSoup(html, 'html.parser')
                divs = soup.body.find_all('div', {'class': {'ListItemName'}})
                counter = 0
                print("Procesando página:", paginas)
                for div in divs:
                    a = div.next_element.next_element
                    if a.name == 'a':
                        href = a['href']
                        href = 'https://www.1999.co.jp' + href
                        counter += 1
                        gunpla_list.append(href)
                print("Se han añadido:", counter, "enlaces a productos")
                paginas -= 1
            print("Productos procesados: ", len(gunpla_list))
            count -= 1
        return gunpla_list

    @staticmethod
    def __get_products(product_list):
        print("Procesando el listado de productos...\n")
        kit_list = []
        header_list = ["Nombre", "Fabricante", "Escala", "Serie", "Original", "Fecha de lanzamiento",
                       "Precio venta", "Precio especial", "Código JAN", "Embalaje", "Peso"]
        total = len(product_list)
        kit_list.append(header_list)
        print(kit_list)
        count = 1
        for item in product_list:
            html = urlopen(item)
            soup = BeautifulSoup(html, 'html.parser')
            contents = []
            name = soup.body.find('h2', {'class': {'h2_itemDetail'}})
            kit_name = (name.text.split('(')[0])
            table = soup.body.find_all('td', {'class': {'tdItemDetail'}})
            print("Procesando", count, "/", total)
            for data in table:
                contents.append(data.text)

            # Obtener las cabeceras
            try:
                fabricante = contents[1]
            except IndexError:
                print("Error con el fabricante")
                fabricante = 'null'
            try:
                scala = contents[3]
            except IndexError:
                print("Error con la escala")
                scala = 'null'
            try:
                serie = contents[5]
            except IndexError:
                print("Error con el fabricante")
                serie = 'null'
            try:
                original = contents[7]
            except IndexError:
                print("Error con el fabricante")
                original = 'null'

            try:
                fecha_lanzamiento = contents[9]
            except IndexError:
                print("Error con el fabricante")
                fecha_lanzamiento = 'null'

            try:
                precio_pvp = contents[11].split('t')[1]
            except IndexError:
                print("Error con el fabricante")
                precio_pvp = 'null'

            try:
                precio_especial = contents[13].split('t')[1].split('\n')[0]
            except IndexError:
                print("Error con el fabricante")
                precio_especial = 'null'

            try:
                codigo_jan = contents[17]
            except IndexError:
                print("Hay algún valor fuera de rango")
                codigo_jan = 'null'

            # Ahora vamos a por los detalles del kit

            details = []
            details_table = soup.body.find_all('div', {'class': {'bikou marginTop10'}})

            # Separa los elementos de la tabla de detalles
            for data in details_table:
                details = data.text.split("\n")
            try:
                medidas = details[3].split(':')[1].split('/')[0]
            except IndexError:
                print("medidas fuera de rango")
                medidas = 'null'
            try:
                peso = details[3].split(':')[1].split('/')[1]
            except IndexError:
                print("peso fuera de rango")
                peso = 'null'

            data_list = [kit_name, fabricante, scala, serie, original, fecha_lanzamiento, precio_pvp, precio_especial,
                         codigo_jan, medidas, peso]
            print(data_list)
            kit_list.append(data_list)
            print("Datos procesados correctamente\n")
            count += 1
        print("Gunplas procesados", len(kit_list))
        return kit_list

    @staticmethod
    def write_data(data_list):
        print("Guardando datos en el csv:\n")
        with open('gunpla.csv', 'w+', newline='')as csvFile:
            writer = csv.writer(csvFile)
            for detail_element in data_list:
                writer.writerow(detail_element)
                print("#Registro guardado")

    def start_scrape(self):
        start_time = time.time()
        print("Iniciando scraping", start_time)
        self.categories = self.__get_categories_links(self.url)
        self.product = self.__get_category_products(self.categories)
        self.data = self.__get_products(self.product)
        self.write_data(self.data)
        end_time = time.time()
        print("\nScraping finalizado, se han obtenido:", len(self.data), "registros")
        print("El proceso ha durado", str(round(((end_time - start_time) / 60), 2)) + " minutos")
