# Generated by Django 4.0.4 on 2022-05-24 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]