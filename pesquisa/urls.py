from django.urls import path
from . import views
#Aqui, estamos importando do Django a função url e todas as nossas views do aplicativo blog

urlpatterns = [
    path('', views.index, name="index"),
    # atribui a view chamada index para a URL raiz
    # name="index" é o nome da URL que será usado para identificar a view
    path('responder/<int:num_pergunta>', views.responder, name="responder"),
    # responder/ é a URL. <int:num_pergunta> quer dizer que o Django espera um objeto do tipo inteiro e que vai transferí-lo para a view como uma variável chamada num_pergunta
    path('votar', views.votar, name="votar"),
    path('resultados/<int:num_pergunta>', views.resultados, name="resultados")
]