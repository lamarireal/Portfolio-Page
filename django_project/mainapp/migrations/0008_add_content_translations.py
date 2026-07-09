from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_remove_skill_category_remove_skill_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chronologyentry',
            name='description_es',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='chronologyentry',
            name='description_uk',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='chronologyentry',
            name='title_es',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='chronologyentry',
            name='title_uk',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='description_es',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_uk',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tags_es',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='tags_uk',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='title_es',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='title_uk',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
