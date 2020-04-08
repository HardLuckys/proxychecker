from django.db import models

class Proxy(models.Model):
    ipadress = models.CharField(max_length=100, unique=True, verbose_name="Ip Adress")

    def __str__(self):
        return self.ipadress
