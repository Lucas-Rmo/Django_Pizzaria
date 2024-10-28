from django.db import models

# Create your models here.

class Borda(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pizza(models.Model):
    nome = models.CharField(max_length=50)
    ingredientes = models.TextField()
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='static/media',null=True,blank=True)
    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('Em andamento', 'Em Andamento'),
        ('Pedido entregue' , 'Pedido Entregue')
    ]

    nome_cliente = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    borda = models.ForeignKey(Borda,on_delete=models.CASCADE)
    #para permitir o django a usar duas chaves estrangeiras no mesmo model,
    #é necessário usar o related_name
    pizza1 = models.ForeignKey(Pizza,on_delete=models.CASCADE, related_name='pizza_sabor1')
    pizza2 = models.ForeignKey(Pizza,on_delete=models.CASCADE, related_name='pizza_sabor2',blank=True,null=True)
    preco = models.FloatField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=50,default='Em andamento')
    def calcular_preco(self):
        if self.pizza1 and not self.pizza2:
            return self.pizza1.preco
        elif self.pizza1 and self.pizza2:
            return (self.pizza1.preco + self.pizza2.preco) / 2
    
    def __str__(self):
        return f"Pedido {self.id} de {self.nome_cliente}"