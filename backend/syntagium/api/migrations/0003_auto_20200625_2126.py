# Generated by Django 3.0.7 on 2020-06-26 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200625_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syntagi',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]