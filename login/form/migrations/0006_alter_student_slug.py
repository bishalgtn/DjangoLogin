# Generated by Django 5.1.5 on 2025-01-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_alter_book_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
