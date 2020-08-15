from django.db import models

class Admin(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

