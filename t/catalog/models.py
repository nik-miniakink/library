from django.db import models
import uuid
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=40, help_text='Enter a genre')

    def __str__(self):
        return self.genre_name


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    summary = models.TextField(max_length=2000)
    genre = models.ManyToManyField(Genre)
#    imprint = models.CharField(max_length=30)
    language = models.CharField(max_length=30, null=True, blank=True)
    ISBN = models.CharField('ISBN', max_length=13, blank=True, null=True)
#    is_active = models.CharField(max_length=30)
    add = models.DateField(auto_now_add=True)
    modern = models.DateField(auto_now=True, null=True)
    image = models.ImageField(upload_to='static/', null=True, blank=True)

    @property
    def display_genre(self):
        return ', '.join([genre.genre_name for genre in self.genre.all()])

  #  display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


    def __str__(self):
        return self.book_name

    def get_1(self):
        return 'self.author'


class Author(models.Model):

    first_name = models.CharField(max_length=100)  # Имя
    last_name = models.CharField(max_length=100)  # Фамилия
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    summary_author = models.TextField(max_length=5000, null=True, blank=True) # Краткая фиография
    GENDER_CHOICES = (
        ('M', 'Mail'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, default='M', null=False)
    image = models.ImageField(upload_to='static/author/', null=True, blank=None)


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class BookInstance(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    book_name = models.ForeignKey('Book', on_delete=models.DO_NOTHING)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    add_1 = models.DateField(auto_now_add=True, null=True)
    modern_1 = models.DateField(auto_now=True, null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=10, choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s %s' % (self.book_id, self.book_name)



