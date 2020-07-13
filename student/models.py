from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=25,unique=True,default='')
    phone = models.IntegerField(unique=True)
    course = models.CharField(max_length=20)
    fee = models.IntegerField()
    dateofJoining = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,upload_to='studentpics')

    def __str__(self):
        return self.name



