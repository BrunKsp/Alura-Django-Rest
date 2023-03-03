from django.contrib import admin
from .models import Matricula, Aluno, Curso

admin.site.register(Matricula)
admin.site.register(Curso)
admin.site.register(Aluno)
