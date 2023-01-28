

from django.contrib import admin
from django.urls import path , include
from escola.views import AlunoViewsets , CursoViewsets , MatriculaViewsets , ListaMatriculaAluno
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('alunos', AlunoViewsets, basename = 'Alunos')
router.register('cursos', CursoViewsets, basename = 'Cursos')
router.register('matriculas', MatriculaViewsets, basename = 'Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('aluno/<int:pk>/matriculas/',ListaMatriculaAluno.as_view()),
]
