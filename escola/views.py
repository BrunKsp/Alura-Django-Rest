from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import routers, serializers, viewsets , generics
from .models import aluno , curso , matricula
from .serializer import alunoSerializer , cursoSerializer , matriculaSerializer , ListaMatriculasAlunoSerializer , ListaAlunosMatriculadosSerializer , AlunoSerializerV2
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated , DjangoModelPermissions




class AlunoViewsets(viewsets.ModelViewSet):
    ##Exibe todos os alunos do banco!!
    queryset = aluno.objects.all()
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return alunoSerializer


class CursoViewsets(viewsets.ModelViewSet):
    queryset = curso.objects.all()
    serializer_class = cursoSerializer



class MatriculaViewsets(viewsets.ModelViewSet):
    queryset = matricula.objects.all()
    serializer_class = matriculaSerializer


class ListaMatriculaAluno(generics.ListAPIView):
    ##Lista as matricula de um determinado aluno
    def get_queryset(self):
        queryset = matricula.objects.filter(Aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    ## Autenticação de usuarios 
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated , DjangoModelPermissions]

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated , DjangoModelPermissions]