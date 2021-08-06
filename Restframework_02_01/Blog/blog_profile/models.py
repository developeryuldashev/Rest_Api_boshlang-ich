from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    level=models.CharField(max_length=100, null=True)
    faculty= models.CharField(max_length=200, null=True)
    cafedra= models.CharField(max_length=200, null=True)
    image=models.ImageField(default='')
    reg_time=models.DateTimeField(auto_now_add=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
    @property
    def full_name(self):
        return self.user.first_name +' ' + self.user.last_name
    def __str__(self):
        return self.full_name

class Article(models.Model):
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    name=models.CharField(max_length=300 )
    text=models.TextField()
    tags=models.CharField(max_length=300)
    published_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class LinkedFiles(models.Model) :
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    file= models.FileField()
    describtion= models.CharField(max_length=200)
    @property
    def fileURL(self):
        try:
            return self.file.url
        except:
            return ''







