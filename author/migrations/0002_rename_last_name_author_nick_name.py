# Generated by Django 5.0 on 2023-12-12 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='last_name',
            new_name='nick_name',
        ),
    ]