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

    def get_tag_list(self):
        if not self.tags:
            return []

        raw_tags = self.tags.replace(';', ',').replace('|', ',')
        return [tag.strip() for tag in raw_tags.split(',') if tag.strip()]


class Skill(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='skill_logos/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class ChronologyEntry(models.Model):
    SIDE_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]

    title = models.CharField(max_length=200)
    date_label = models.DateTimeField("date published")
    description = models.TextField()
    image = models.ImageField(upload_to='chronology_images/', blank=True)
    video_url = models.URLField(blank=True)
    link = models.URLField(blank=True)
    side = models.CharField(max_length=10, choices=SIDE_CHOICES, default='right')

    class Meta:
        ordering = ['date_label']

    def __str__(self):
        return f"{self.title} ({self.date_label})"
