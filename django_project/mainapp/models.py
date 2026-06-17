import datetime

from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
