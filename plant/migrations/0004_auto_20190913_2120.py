# Generated by Django 2.2.4 on 2019-09-14 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0003_auto_20190913_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='alternative_names',
            field=models.CharField(max_length=100),
        ),
    ]
