# Generated by Django 3.0 on 2020-07-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgl', '0003_auto_20200704_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='about',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
