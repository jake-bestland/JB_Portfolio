# Generated by Django 5.1.2 on 2024-10-30 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_delete_animatedimage_remove_project_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='animated_gif',
            field=models.ImageField(blank=True, null=True, upload_to='images/gifs/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/previews/'),
        ),
    ]
