from django.contrib import admin

# Register your models here.
from.models import Alternativa, Pergunta
# Importa os modelos Alternativa e Pergunta

# Registrar os modelos para que fiquem visíveis na página de admin
admin.site.register(Pergunta)
admin.site.register(Alternativa)