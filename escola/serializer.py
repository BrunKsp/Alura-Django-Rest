from rest_framework import serializers
from .models import aluno, curso

class alunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento']

    

class cursoSerializer(serializers.ModelSerializer):
    class Meta :
        model = curso
        fields = '__all__'

