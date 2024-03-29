# Generated by Django 3.2.9 on 2021-11-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20211116_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/Countries'),
        ),
        migrations.AddField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/Genre'),
        ),
    ]
