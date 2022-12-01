import requests
from bs4 import BeautifulSoup   

def Texto(novo) -> list:
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
        novo = soup.find_all('td')
       
        return novo 

j = []
resu = Texto(j)

# vetor = input("Digite sua milhar: ")

for v in resu:
    # if v == vetor:
    #     print(f'Essa milhar saio: {vetor}')
        
    # else:
    #     print(f'\nEssa milhar nao saio: {vetor} ')
    #     print(v[1::10])
    #     break
    
    print(type(v))
        
            

    



