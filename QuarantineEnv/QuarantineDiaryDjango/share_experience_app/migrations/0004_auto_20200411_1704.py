# Generated by Django 2.0.2 on 2020-04-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_experience_app', '0003_auto_20200411_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experienceitem',
            name='id',
        ),
        migrations.AddField(
            model_name='experienceitem',
            name='exp_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experienceitem',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
