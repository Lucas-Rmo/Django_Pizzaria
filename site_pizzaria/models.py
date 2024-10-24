from django.db import models

# Create your models here.
class Sabor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Borda(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pizza(models.Model):
    nome = models.CharField(max_length=50)
    ingredientes = models.TextField()
    sabor = models.ForeignKey(Sabor,on_delete=models.CASCADE, related_name='pizza_sabor1')
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='media/',null=True)
    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    borda = models.ForeignKey(Borda,on_delete=models.CASCADE)
    #para permitir o django a usar duas chaves estrangeiras no mesmo model,
    #é necessário usar o related_name
    pizza1 = models.ForeignKey(Pizza,on_delete=models.CASCADE, related_name='pizza_sabor1')
    pizza2 = models.ForeignKey(Pizza,on_delete=models.CASCADE, related_name='pizza_sabor2',blank=True,null=True)

    