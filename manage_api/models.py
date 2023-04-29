from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    summary = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title