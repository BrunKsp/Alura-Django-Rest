
from rest_framework.test import APITestCase
from django.http import response 
from django.urls import reverse 
from escola.models import Curso
from rest_framework import status 

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso teste 1', nivel='B'
        )

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para criar um curso"""
        data = {
            'codigo_curso':'PY1',
            'descricao':'Curso pYTHON 3',
            'nivel':'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    
    def test_requisicao_delete_para_deletar_curso(self):
        ## Para funcionar precisa adicionar http_method_names = ['get', 'post', 'put', 'path' , 'delete'] nos cursos viewset 
        """Teste para verificar a requisição DELETE não permitida para deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar a requisição PUT para atualizar um curso"""
        data = {
            'codigo_curso':'PHP1',
            'descricao':'Curso PHP atualizado',
            'nivel':'I'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)