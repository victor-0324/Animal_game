from os import write
import re 
import requests  
from bs4 import BeautifulSoup  
from datetime import datetime

# now = datetime.now().strftime("%d/%m/%Y ")
# print(f"Current time: {now}") 

# def Tabela():
# 1. Pegar conteudo HTML a partir da URL
url = "https://www.resultadofacil.com.br/resultado-do-jogo-do-bicho/PB" 
html = requests.get(url)  

if html.status_code != 200: 
    print(">> Falha na requisição! <<")
else:
# content passa o conteúdo da página
    html_content = html.content
    # Parsear o conteúdo HTML buscado, para poder ficar mais estruturado de acordo com as tags HTML
    soup = BeautifulSoup(html_content, 'html.parser')

# cabecario = soup.select('b')[0 : 5]
# bichos = soup.find_all('tbody', id=True)
# data = soup.find_all('h3', class_='g')

    tabela = soup.find_all('div', {"class":"col-sm-12 col-md-6 col-lg-4"})  
    novo = soup.find_all( 'p')
    h3 = list(novo)
    
    print(h3[0])