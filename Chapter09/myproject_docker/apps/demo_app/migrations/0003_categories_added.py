# Generated by Django 2.1.1 on 2018-09-11 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0002_add_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='ideas', to='demo_app.Category', verbose_name='Category'),
        ),
    ]
