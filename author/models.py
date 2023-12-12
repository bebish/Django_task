from django.db import models

# Create your models here.

class Author(models.Model): #create table item
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=100)
    birth=models.DateField()

    def __str__(self) -> str:       # вид в админке каждого продукта
        return f"{self.name} {self.last_name}"