# Generated by Django 3.2.9 on 2022-02-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserstudent',
            name='custom_student_id',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
