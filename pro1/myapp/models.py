from django.db import models

# Create your models here.
class noteapp(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    create_at=models.TimeField(auto_now_add=True)