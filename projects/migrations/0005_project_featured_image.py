# Generated by Django 4.1.7 on 2023-03-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_tag_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
