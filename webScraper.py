# Importar las bibliotecas necesarias
from bs4 import BeautifulSoup
import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'connection': 'close' 
}

url = 'https://www.amazon.com.mx/s?k=pc&ref=nb_sb_noss_2'

def solicitud(url,headers):
    try:
    # Hacer una solicitud HTTP a la página de Amazon
        response = requests.get(url, headers=headers)
    #Crear un objeto BeautifulSoup para analizar el HTML
        return BeautifulSoup(response.text, 'html.parser')    
    except Exception as e:
        print(f"Error: {e}")

htmldoc = solicitud(url, headers=headers)

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
        print([price.text])
    else:
        print('no se encontro nada')
