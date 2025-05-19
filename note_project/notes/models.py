from django.db import models

# Create your models here.
class note(models.Model):
    title = models.CharField()
    text = models.TextField()

    def __str__(self):
        return self.title