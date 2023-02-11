import pytest
import requests


class TestCurso:
    headers = {"Authorization": "Token d31245a8aaab46dff2f67de0f3cad19d38e9a77b"}
    url_base_cursos = "http://localhost:8000/api/v2/cursos/"

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}2/', 
                                                        headers=self.headers)

        assert curso.status_code == 200
    
    def test_post_curso(self):
        novo = {
            "titulo": "Curso de programacao de python",
            "url": "http://www.cursopython.com.br",
        }
        resposta = requests.post(url=self.url_base_cursos, 
                                            headers=self.headers, data=novo)

        assert resposta.status_code == 201
        #assert resposta.json()["titulo"] == novo["titulo"]

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Python",
            "url": "http://www.novocursopython.com.br",
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', 
                                        headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Python 2",
            "url": "http://www.novocursopython.com.br",
        }
        resposta = requests.put(url=f'{self.url_base_cursos}2/', 
                                        headers=self.headers, data=atualizado)

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}2/', 
                                                        headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
