# Generated by Django 4.2 on 2023-04-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(),
        ),
    ]
