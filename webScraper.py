# Importar las bibliotecas necesarias
from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com.mx/s?k=pc&ref=nb_sb_noss_2'

def solicitud(url):
    try:
    # Hacer una solicitud HTTP a la página de Amazon
        response = requests.get(url)
    #Crear un objeto BeautifulSoup para analizar el HTML
        return BeautifulSoup(response.text, 'html.parser')    
    except Exception as e:
        print(f"Error: {e}")

htmldoc = solicitud(url)

#   Encontramos el elemento 'div' en el HTML
item_html = htmldoc.find_all('div', class_='a-section a-spacing-base')

# Iterar sobre cada elemento 'div' encontrado
for spans in item_html:
    # Encontrar el elemento con la clase específica 'a-size-mini a-spacing-none a-color-base s-line-clamp-4'
    #clasname = spans.find('td',class_='a-color-secondary')

    # Encontrar el elemento 'a-price-whole' que generalmente contiene el precio
    price = spans.find('span',class_='a-price-whole')

    # Imprimir una lista con el precio
    if price:
        print([price])
    else:
        print('no se encontro nada')