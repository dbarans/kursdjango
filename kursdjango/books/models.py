from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.TextField()
    publication_year = models.SmallIntegerField()
    author = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.author})"