# Generated by Django 4.0 on 2022-07-12 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='variations',
        ),
    ]