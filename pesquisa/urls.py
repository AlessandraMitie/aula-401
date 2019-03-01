from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('responder/<int:num_pergunta>', views.responder, name="responder"),
    path('votar', views.votar, name="votar"),
    path('resultados/<int:num_pergunta>', views.resultados, name="resultados")
]