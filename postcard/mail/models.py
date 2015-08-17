from django.db import models

class Mail(models.Model):
    subject = models.CharField(max_length=127)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

class Thread(models.Model):
    # TODO : Sequencing of thread
    mail = models.ForeignKey('Mail')
    message = models.TextField(blank=False)
    user = models.ManyToManyField('user_auth.User', through='UserThreadMap')
    created_on = models.DateTimeField(auto_now_add=True)

class UserThreadMap(models.Model):
    DELIVERY_CHOICES = (
        ('CC', 'CC'),
        ('BCC', 'BCC'),
        ('TO', 'TO'),
        ('FROM', 'FROM'),
    )
    user = models.ForeignKey('user_auth.User')
    thread = models.ForeignKey('Thread')
    delivery_status = models.CharField(max_length=4, choices=DELIVERY_CHOICES)