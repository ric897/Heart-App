# Generated by Django 3.2.7 on 2022-10-16 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20221016_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='resources',
        ),
        migrations.AddField(
            model_name='course',
            name='resources',
            field=models.ManyToManyField(to='main.Resource'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='trainings',
        ),
        migrations.AddField(
            model_name='course',
            name='trainings',
            field=models.ManyToManyField(to='main.Training'),
        ),
    ]