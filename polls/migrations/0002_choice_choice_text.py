# Generated by Django 2.2.2 on 2019-07-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='Not much', max_length=200),
            preserve_default=False,
        ),
    ]
