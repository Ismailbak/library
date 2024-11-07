from django.db import models

# Author Model
class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    date_of_birth = models.DateField(verbose_name="Date de naissance")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    publication_date = models.DateField(verbose_name="Date de publication")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Auteur")

    def __str__(self):
        return self.title

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
    books = models.ManyToManyField(Book, related_name="categories", verbose_name="Livres")

    def __str__(self):
        return self.name
