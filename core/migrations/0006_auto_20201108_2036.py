# Generated by Django 3.1.3 on 2020-11-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201108_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='updated_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(),
        ),
    ]
