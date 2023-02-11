import requests, jsonpath


avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")

#resultados = jsonpath.jsonpath(avaliacoes.json(), "results")
#print(resultados)

# Buscando o primeiro
#primeira = jsonpath.jsonpath(avaliacoes.json(), "results[0]")
#print(primeira)

# Buscando nome do primeiro resultado
#nome = jsonpath.jsonpath(avaliacoes.json(), "results[0].nome")
#print(nome)

# Buscando avaliacao(nota) do primeiro resultado
#nota = jsonpath.jsonpath(avaliacoes.json(), "results[0].avaliacao")
#print(nota)

# Todos os nomes das pessoas que avaliaram o curso
#nomes = jsonpath.jsonpath(avaliacoes.json(), "results[*].nome")
#print(nomes)
