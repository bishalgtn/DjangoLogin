from django.db import models
from django.utils.text import slugify

# Create your models here.
SUBJECT_CHOICES = [
    ('PHYSICS', 'Physics'),
    ('CHEMISTRY', 'Chemistry'),
    ('MATHS', 'Maths'),
    ('BIOLOGY', 'Biology'),
    ('ZOOLOGY', 'Zoology'),
]

class Book(models.Model):
    ISBIN = models.IntegerField( unique=True)
    title = models.CharField(max_length=100)
    discription = models.TextField()
    catagory = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='PHYSIC',)


    def __str__(self):
        return f"{self.ISBIN} of book title {self.title}"



class Student(models.Model):
    roll_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, null=True)
    book = models.ForeignKey(Book, on_delete= models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
