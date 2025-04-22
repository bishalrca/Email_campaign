from django.db import models

# Create your models here.

from django.db import models

class EmailList(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    email_list = models.ForeignKey(EmailList, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class Campaign(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    email_list = models.ForeignKey(EmailList, null=True, blank=True, on_delete=models.SET_NULL)
    sent_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject
    

