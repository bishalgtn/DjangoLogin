# Generated by Django 5.1.5 on 2025-01-29 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_rename_isbin_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 29, 8, 28, 25, 383894, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
