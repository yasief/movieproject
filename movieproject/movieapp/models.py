from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=50)
    year=models.CharField(max_length=4)
    duration=models.CharField(max_length=50)
    genre=models.CharField(max_length=250)
    desc=models.TextField()
    starring=models.TextField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
