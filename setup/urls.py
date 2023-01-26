

from django.contrib import admin
from django.urls import path , include
from escola.views import AlunoViewsets , CursoViewsets
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('alunos', AlunoViewsets, basename = 'Alunos')
router.register('cursos', CursoViewsets, basename = 'Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) )
]
