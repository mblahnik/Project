# Generated by Django 2.1.7 on 2019-04-02 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='RoomNumber',
        ),
    ]