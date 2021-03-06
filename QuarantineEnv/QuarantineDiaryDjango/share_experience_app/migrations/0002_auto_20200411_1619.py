# Generated by Django 2.0.2 on 2020-04-11 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('share_experience_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experienceitem',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='experienceitem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experienceitem',
            name='likes',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
