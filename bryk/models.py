from django.db import models

# Create your models here.
class Jobs_Listings(models.Model):
    username = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_link = models.CharField(max_length=1000)
    deadline = models.CharField(max_length=100)

    def __str__(self):
        return self.username

