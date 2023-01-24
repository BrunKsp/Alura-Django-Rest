from django.urls import path
from . import views 



urlpatterns = [
    path('alunos/', views.alunos, name='alunos'),
    
]