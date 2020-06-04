from django.db import models

class FinalOrder(models.Model):
    date = models.DateTimeField(auto_now=True)
    