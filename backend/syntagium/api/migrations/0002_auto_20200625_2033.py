# Generated by Django 3.0.7 on 2020-06-25 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='syntagi',
            old_name='owner',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='syntagi',
            name='image',
        ),
        migrations.RemoveField(
            model_name='syntagi',
            name='star_rating',
        ),
    ]
