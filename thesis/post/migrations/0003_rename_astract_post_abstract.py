# Generated by Django 5.0.1 on 2024-02-25 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='astract',
            new_name='abstract',
        ),
    ]
