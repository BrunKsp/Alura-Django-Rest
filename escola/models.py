from django.db import models

class aluno (models.Model):
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)


    def __str__(self) :
        return self.nome


class curso (models.Model):
    
    NIVEL = (
            ('B', 'Básico'),
            ('I','Intermediário'),
            ('A','Avançado'),
            
            )
    
    codigo_curso = models.CharField(max_length=10)
    descricao = models.TextField(max_length=100)
    nivel = models.CharField(max_length=1,choices=NIVEL, blank=False, null=False ,default='B')
