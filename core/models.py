from django.db import models

class Apps(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
