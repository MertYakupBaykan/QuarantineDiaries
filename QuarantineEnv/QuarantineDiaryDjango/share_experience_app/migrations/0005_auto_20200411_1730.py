# Generated by Django 2.0.2 on 2020-04-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_experience_app', '0004_auto_20200411_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experienceitem',
            name='exp_id',
        ),
        migrations.AddField(
            model_name='experienceitem',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
