# Generated by Django 4.2.1 on 2023-05-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babies', '0005_alter_baby_logged_milestones'),
        ('milestones', '0002_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='logged_by_babies',
            field=models.ManyToManyField(blank=True, related_name='milestones', to='babies.baby'),
        ),
    ]
