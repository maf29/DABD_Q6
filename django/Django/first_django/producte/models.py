from django.db import models

# Create your models here.

class ProductTemplate(models.Model):
    name = models.CharField(max_length=200)
    list_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    salable = models.BooleanField()

    def __str__(self):
        return self.name


class ProductProduct(models.Model):
    template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)

    def __str__(self):
        return '[' + self.code + '] ' + self.template.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    
    #protect : el objeto al que se hace referencia no se puede eliminar mientras existan objetos que hagan referencia a él. Los objetos de referencia deben eliminarse manualmente antes de eliminar el objeto de referencia. 
    parent = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, blank=True, null=True)
    
    
    #Relación muchos a muchos entre Productos y categorías 
    template = models.ManyToManyField(ProductTemplate, blank=True) # en el ManyToManyField no le importa el NULL

    def __str__(self):
        return self.name