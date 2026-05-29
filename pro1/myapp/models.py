from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
      
        return self.name


class noteapp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    create_at=models.TimeField(auto_now_add=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title