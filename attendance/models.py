from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    name=models.CharField(max_length=25)
    attended=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    attendance=models.FloatField(default=0)
    userid=models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

