# Generated by Django 3.2.9 on 2022-01-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20220112_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]