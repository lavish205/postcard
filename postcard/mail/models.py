from django.db import models

# Create your models here.
class Mail(models.Model):
    subject = models.CharField(max_length=127)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
        