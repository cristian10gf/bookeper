# crea una clase que tenga un nombre de libro, un texto
class Resumen:
    def __init__(self, nombre_libro, texto):
        self.nombre_libro = nombre_libro
        self.texto = texto

    def __str__(self):
        return f"{self.nombre_libro} - {self.texto}"
    
# crea una funcion para almacenar un resumen en un archivo de texto
def almacenar_resumen(self):
    with open('resumenes.txt', 'a') as archivo:
        archivo.write(f'{self.nombre_libro},{self.texto}')

# crea un archivo de texto para almacenar los resumenes
with open('resumenes.txt', 'w') as archivo:
    archivo.write('nombre_libro,texto')

# crea una funcion para leer los datos de un archivo de texto y guardarlos en un diccionario
def leer_archivo():
    with open('resumenes.txt', 'r') as archivo:
        for linea in archivo:
            resumenes = {}
            linea = linea.strip()
            nombre_libro, texto = linea.split(',')
            resumenes[nombre_libro] = Resumen(nombre_libro, texto)
    return resumenes

# importa requests
import requests

""" url = 'https://www.goodreads.com/book/review_counts.json'
# haz una peticion de un libro a la api de goodreads
def peticion_libro(isbn, nombre_libro):
    # crea un diccionario con los parametros de la peticion
    peticion = {'key': 'API_KEY', 'isbns': isbn}
    # haz la peticion
    respuesta = requests.get(url, params=peticion)
    # convierte la respuesta en un diccionario
    diccionario = respuesta.json()
    # crea un diccionario con los datos del libro
    libro = {}
    libro['nombre_libro'] = nombre_libro
    libro['isbn'] = isbn
    libro['puntuacion'] = diccionario['books'][0]['average_rating']
    libro['numero_votos'] = diccionario['books'][0]['work_ratings_count']
    return libro """

