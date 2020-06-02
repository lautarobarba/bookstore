from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta():
        ordering = ['last_name']

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)