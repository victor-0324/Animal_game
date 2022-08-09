from flask import Blueprint, request, render_template, url_for, redirect
import re 
import requests  
from bs4 import BeautifulSoup  
from datetime import datetime

# now = datetime.now().strftime("%d/%m/%Y ")
# print(f"Current time: {now}") 

def Tabela():
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

        tabela = soup.find_all('div', class_="col-sm-12 col-md-6 col-lg-4")  
        novo = soup.find_all('table')
       
        return novo

def Horario():
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

        tabela = soup.find_all('div', class_="col-sm-12 col-md-6 col-lg-4")  
        novo = soup.find_all('h3')
       
        return novo

initial_app = Blueprint("initial_app", __name__, url_prefix="/", template_folder='templates',static_folder='static')

# Tela Iniciarl
@initial_app.route("/", methods=["GET", "POST"])
def mostrar():
    tabela = Tabela()
    hrs_0 = tabela
    data = Horario()
    return render_template("pages/initial/index.html",hrs_0=hrs_0, data=data)