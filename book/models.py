from django.db import models
# Create your models here.
from author.models import Author
class Book(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateField()
    genre = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')