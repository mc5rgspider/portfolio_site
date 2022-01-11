from django.db import models

# Create your models here.

class Blog(models.Model):
    #title of the blog
    title = models.CharField(max_length=150)
    
    #description for the blog
    description = models.TextField()
    date = models.DateField()
    
    
    def __str__(self):
        return self.title