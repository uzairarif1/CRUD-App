from django.db import models

# Create your models here.

class Record(models.Model):
    first_name= models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    email= models.EmailField(max_length=25)
    phone= models.IntegerField()
    address= models.TextField(max_length=100)
    joined_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name





