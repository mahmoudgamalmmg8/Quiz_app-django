# Generated by Django 3.2.9 on 2022-02-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuserstudent_custom_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuserstudent',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='customuserstudent',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuserstudent',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
