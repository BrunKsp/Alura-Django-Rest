from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import routers, serializers, viewsets
from .models import aluno , curso 
from .serializer import alunoSerializer , cursoSerializer



class AlunoViewsets(viewsets.ModelViewSet):
    ##Exibe todos os alunos do banco!!
    queryset = aluno.objects.all()
    serializer_class = alunoSerializer


class CursoViewsets(viewsets.ModelViewSet):
    queryset = curso.objects.all()
    serializer_class = cursoSerializer


def alunos (request):

    if request.method == 'GET':
        aluno = {'id':'1' , 'nome':'Teste' }
        return JsonResponse(aluno)
