# Generated by Django 2.1.7 on 2019-04-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNumber', models.IntegerField(default=0)),
                ('sectionNumber', models.IntegerField(default=0)),
                ('meetingDays', models.CharField(default=' ', max_length=10)),
                ('startTime', models.CharField(default='00:00', max_length=10)),
                ('endTime', models.CharField(default='00:00', max_length=10)),
                ('RoomNumber', models.CharField(default='EMS', max_length=10)),
            ],
        ),
    ]
