from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')


class Tag(models.Model):
    title = models.CharField(max_length=20, null=False)

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200, default='no title', null=False) 

    contents = models.CharField(max_length = 5000)
    hits = models.PositiveSmallIntegerField(default = 0, null=True)
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
