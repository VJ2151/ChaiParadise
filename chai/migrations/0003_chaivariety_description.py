# Generated by Django 5.1.4 on 2025-01-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_alter_chaivariety_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
