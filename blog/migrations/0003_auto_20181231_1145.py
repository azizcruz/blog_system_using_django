# Generated by Django 2.2.dev20181230164339 on 2018-12-31 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181231_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='puplish_date',
            new_name='publish_date',
        ),
    ]
