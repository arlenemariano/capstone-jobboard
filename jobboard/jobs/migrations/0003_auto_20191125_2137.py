# Generated by Django 2.2.7 on 2019-11-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20191125_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]