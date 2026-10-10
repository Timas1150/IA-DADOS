import requests as rq

cep = input("Digite seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = rq.get(url).json()

print(f" você mora na {dados["logradouro"]} no bairro {dados["bairro"]} e na cidade de {dados["localidade"]}")