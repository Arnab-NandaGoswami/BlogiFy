# Generated by Django 3.2.7 on 2021-10-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogify', '0004_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
