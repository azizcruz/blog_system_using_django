# Generated by Django 2.2.dev20181230164339 on 2019-01-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181231_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_images/default.png', upload_to='post_image'),
        ),
    ]
