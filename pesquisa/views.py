from django.shortcuts import render
# Incluir os modelos/classes (definidos em models.py) no arquivo views.py:
from .models import Alternativa, Pergunta
# O ponto antes de models significa diretório/aplicativo atual.
# Create your views here.

def index(request):
    todas = Pergunta.objects.all()
    return render(request, 'index.html', {
        "perguntas": todas
    })
    # criada a função def chamada index que recebe um request, executa a função render que irá renderizar(montar) o modelo de acordo com o template index.html e retorna (return) o resultado
def responder(request, num_pergunta):
    pergunta = Pergunta.objects.get(pk=num_pergunta)
    # metodo get para selecionar uma pergunta com o campo pk (primary key) igual a nu_pergunta
    # pergunta é a variável definida para o QuerySet
    return render(request, 'responder.html', {
        # a função render tem o parâmetro request um arquivo de template responder.html e o parâmetro, que é uma string "pergunta"
        "pergunta": pergunta
    })

def votar(request):
    voto = request.POST['escolha']
    escolhida = Alternativa.objects.get(pk=voto)
    escolhida.votos += 1
    escolhida.save()

    return resultados(request, escolhida.pergunta_id)

def resultados(request, num_pergunta):
    pergunta = Pergunta.objects.get(pk=num_pergunta)
    return render(request, 'resultados.html', {
        "pergunta": pergunta
    })