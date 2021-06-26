from django.db import models

class Maecenas(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    mail = models.CharField(max_length=200, null=True)
    message = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name
