# Generated by Django 2.0.2 on 2020-04-11 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share_experience_app', '0002_auto_20200411_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experienceitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='experienceitem',
            name='created_on',
        ),
    ]
