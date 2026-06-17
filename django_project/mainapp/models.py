from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)

