from django.db import models

# Create your models here.
class BDAdata(models.Model):
    userid = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=16)
    dateofJoining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userid