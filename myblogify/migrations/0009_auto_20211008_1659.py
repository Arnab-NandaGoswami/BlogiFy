# Generated by Django 3.2.7 on 2021-10-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogify', '0008_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the link above to read the blog post...', max_length=255),
        ),
    ]