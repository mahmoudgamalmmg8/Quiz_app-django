# Generated by Django 3.2.9 on 2022-02-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='total',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
    ]
