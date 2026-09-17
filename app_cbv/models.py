from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,

    )
    summary = models.TextField(max_length=600,null=True)
    isbn = models.CharField(max_length=30,unique=True)
    genre = models.ManyToManyField(Genre)
    languages = models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_details', kwargs = {"pk":self.pk})

class Language(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name


    #genre = models.ManyToManyField(Genre)
class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True,blank=True)

    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        return reverse('author_details', kwargs = {"pk":self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name
#unique book (copy)
import uuid
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=150)
    due_back = models.DateField(null=True,blank=True)
    borrower= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)#user obj table

    LOAN_STATUS = (
    ('m',"Maintenance"),
        ('o', "On loan"),
        ('r', "Reserved"),
    ('a','Available'),
    )
    status = models.CharField(max_length=1,choices=LOAN_STATUS,default='m',blank=True)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f"{self.id} '  {self.book.title}"

