from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings

class Estado(models.Model):

    nome = models.CharField('Nome do Estado', max_length = 200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(models.Model):

    nome = models.CharField('Nome da cidade', max_length = 200)
    estado = models.ManyToManyField(Estado)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class Filtro(models.Model):

    nome = models.CharField('Nome do filtro', max_length = 200)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Filtro'
        verbose_name_plural = 'Filtros'

class User(AbstractUser):
    username = models.CharField('username', max_length=150, unique=True)
    nome = models.CharField(
        'Nome Completo',
        max_length=200,
        unique=False,
        null=True
    )
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    pais = models.ManyToManyField(Cidade)
    email =  models.EmailField('E-mail', max_length = 200)
    telefone =  models.CharField('Telefone', max_length = 20)
    biografia = models.TextField('Biografia')

    def __str__(self):
        return str(self.username)

class Foto(models.Model):

    imagem = models.ImageField('Foto', upload_to='media/foto')
    legenda = models.CharField('Legenda', max_length = 2200)
    filtro = models.ManyToManyField(Filtro)

    def __str__(self):
        return self.legenda

    def get_absolute_url(self):
        return reverse('foto_edit', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

class Like(models.Model):

    usuario = models.ManyToManyField(User)
    foto = models.ManyToManyField(Foto)

