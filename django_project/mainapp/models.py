import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import get_language


TRANSLATED_LANGUAGE_SUFFIXES = {
    'es': 'es',
    'ua': 'ua',
}


def localized_field(instance, field_name):
    language_code = (get_language() or 'en').split('-')[0]
    suffix = TRANSLATED_LANGUAGE_SUFFIXES.get(language_code)
    if suffix:
        translated_value = getattr(instance, f'{field_name}_{suffix}', '')
        if translated_value:
            return translated_value
    return getattr(instance, field_name)


class Project(models.Model):
    title = models.CharField(max_length=100)
    title_es = models.CharField(max_length=100, blank=True)
    title_ua = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    description_es = models.TextField(blank=True)
    description_ua = models.TextField(blank=True)
    tags = models.CharField(max_length=100)
    tags_es = models.CharField(max_length=100, blank=True)
    tags_ua = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def localized_title(self):
        return localized_field(self, 'title')

    def localized_description(self):
        return localized_field(self, 'description')

    def get_tag_list(self):
        tags = localized_field(self, 'tags')
        if not tags:
            return []

        raw_tags = tags.replace(';', ',').replace('|', ',')
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
    title_es = models.CharField(max_length=200, blank=True)
    title_ua = models.CharField(max_length=200, blank=True)
    date_label = models.DateTimeField("date published")
    description = models.TextField()
    description_es = models.TextField(blank=True)
    description_ua = models.TextField(blank=True)
    image = models.ImageField(upload_to='chronology_images/', blank=True)
    video_url = models.URLField(blank=True)
    link = models.URLField(blank=True)
    side = models.CharField(max_length=10, choices=SIDE_CHOICES, default='right')

    class Meta:
        ordering = ['date_label']

    def __str__(self):
        return f"{self.title} ({self.date_label})"

    def localized_title(self):
        return localized_field(self, 'title')

    def localized_description(self):
        return localized_field(self, 'description')
