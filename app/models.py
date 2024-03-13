from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="app/static/imagens", blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.categoria} {self.nome}"


class Imovel(models.Model):
    nome = models.CharField(max_length=100)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Imoveis"

    def __str__(self):
        return self.nome


class ContratoLocacao(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True)
    nome = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "Contratos de Locação"

    def save(self, *args, **kwargs):
        # Set the 'valor_aluguel' attribute of the instance
        # based on the related 'imovel' object's 'valor_aluguel'
        self.valor_aluguel = self.imovel.valor_aluguel

        # Set the 'nome' attribute of the instance
        # based on the related 'imovel' object's 'nome'
        self.nome = self.imovel.nome

        # Call the save method of the parent class to save the instance
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.imovel.nome}"


@receiver(post_save, sender=Imovel)
def update_contratolocacao(sender, instance, **kwargs):
    ContratoLocacao.objects.filter(imovel=instance).update(valor_aluguel=instance.valor_aluguel)
    ContratoLocacao.objects.filter(imovel=instance).update(nome=instance.nome)


