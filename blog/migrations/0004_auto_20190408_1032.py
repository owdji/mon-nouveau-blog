# Generated by Django 2.2 on 2019-04-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_related_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='related_posts',
            field=models.ManyToManyField(blank=True, related_name='_post_related_posts_+', to='blog.Post'),
        ),
    ]
