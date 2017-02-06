from django.db import models

class Pessoa(models.Model):
    nome = models.CharField("Nome do Participante", max_length=150)
    dataNascimento = models.DateField("Data de Nascimento")
    telefone = models.CharField("Telefone", max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.nome
class Participante(Pessoa):
    pass

class Palestrante(Pessoa):
    minicurriculo = models.TextField("Minicurriculo")

class Endereco(models.Model):
    logradouro = models.CharField("Logradouro", max_length=255)
    numero = models.CharField("Número", max_length=10)
    bairro = models.CharField("Bairro", max_length=150)
    bairro = models.CharField("Bairro", max_length=150)
    cidade = models.CharField("Cidade", max_length=55)
    estado = models.CharField("Estado", max_length=50)

class Evento(models.Model):
    titulo = models.CharField("Titulo do Evento", max_length=250)
    dataInicio = models.DateField("Data de Inicio do evento")
    dataTermino = models.DateField("Data do Termino do evento")
    endereco = models.OneToOneField(Endereco)

    def __str__(self):
        return self.titulo

class Atividade(models.Model):
    titulo = models.CharField("Titulo da Atividade", max_length=150)
    duracao = models.CharField("Tempo de duração", max_length=50)
    tipo = models.CharField("Tipo da atividade", max_length=50)
    participante = models.ManyToManyField(Participante)
    palestrante = models.ManyToManyField(Palestrante)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
