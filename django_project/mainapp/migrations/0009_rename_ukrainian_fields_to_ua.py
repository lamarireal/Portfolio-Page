from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_add_content_translations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chronologyentry',
            old_name='description_uk',
            new_name='description_ua',
        ),
        migrations.RenameField(
            model_name='chronologyentry',
            old_name='title_uk',
            new_name='title_ua',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='description_uk',
            new_name='description_ua',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='tags_uk',
            new_name='tags_ua',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title_uk',
            new_name='title_ua',
        ),
    ]
