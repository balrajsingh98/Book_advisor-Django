# Generated by Django 2.2.10 on 2021-05-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdvisorName', models.CharField(max_length=80)),
                ('AdvisorPhotoURL', models.CharField(max_length=80)),
            ],
        ),
    ]