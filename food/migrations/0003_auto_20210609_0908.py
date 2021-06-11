# Generated by Django 3.1.6 on 2021-06-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(default='data:image/jpeg;base64,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', max_length=9500),
        ),
    ]
