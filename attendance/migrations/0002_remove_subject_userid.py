# Generated by Django 3.0.4 on 2020-04-02 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='userid',
        ),
    ]
