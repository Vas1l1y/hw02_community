# Generated by Django 2.2.19 on 2022-06-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220625_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='descprition',
            field=models.TextField(),
        ),
    ]
