# Generated by Django 5.0.2 on 2024-03-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
