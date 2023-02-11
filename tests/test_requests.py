import requests


# GET avaliacoes
#avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")

# Acessando o código de status HTTP
#print(avaliacoes.status_code)

# Acessando os dados da resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json()))

# Acessando a quntidade de registros
#print(avaliacoes.json()["count"])

# Acessando a próxima página de resultados
#print(avaliacoes.json()["next"])

# Acessando os resultados desta página
#print(avaliacoes.json()["results"])
#print(type(avaliacoes.json()["results"]))


# GET Avaliacao
# avaliacao id = 2
#avaliacao = requests.get("http://localhost:8000/api/v2/avaliacoes/2")

#print(avaliacao.json())

# GET curso

# Credenciais de autenticação
headers = {"Authorization": "Token d31245a8aaab46dff2f67de0f3cad19d38e9a77b"}

cursos = requests.get(url="http://localhost:8000/api/v2/cursos", 
                                                            headers=headers)

print(cursos.json())
print("Status code:", cursos.status_code)
