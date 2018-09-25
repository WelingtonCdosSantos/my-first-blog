from django.contrib import admin
from .models import Post #Importando a classe Post do arquivo models

admin.site.register(Post) #É preciso registrar a classe Post
