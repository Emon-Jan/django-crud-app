# Generated by Django 2.0.6 on 2018-06-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]