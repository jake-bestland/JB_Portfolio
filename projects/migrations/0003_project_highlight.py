# Generated by Django 5.1.2 on 2024-10-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_project_technology_skill_project_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='highlight',
            field=models.BooleanField(default=False),
        ),
    ]
