# Generated by Django 3.2.7 on 2022-10-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
