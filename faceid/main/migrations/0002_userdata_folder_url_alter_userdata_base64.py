# Generated by Django 5.2 on 2025-05-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='folder_url',
            field=models.CharField(max_length=20),
        ),
        # migrations.AlterField(
        #     model_name='userdata',
        #     name='base64',
        #     field=models.CharField(max_length=255),
        # ),
    ]
