# Generated by Django 2.2.19 on 2022-06-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220625_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='descprition',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]