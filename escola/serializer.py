from rest_framework import routers, serializers, viewsets 
from .models import aluno, curso , matricula

class alunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento']

class AlunoSerializerV2(serializers.ModelSerializer):  
    class Meta:
        model = aluno
        fields = ['id', 'nome', 'celular','rg', 'cpf', 'data_nascimento'] 

class cursoSerializer(serializers.ModelSerializer):
    class Meta :
        model = curso
        fields = '__all__'

class matriculaSerializer(serializers.ModelSerializer):
    class Meta :
        model = matricula
        fields = '__all__'


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    Curso = serializers.ReadOnlyField(source='Curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = matricula
        fields = ['Curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    Aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = matricula
        fields = ['Aluno_nome']


    

   
