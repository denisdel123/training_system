# Generated by Django 5.0.2 on 2024-02-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingApp', '0003_student_access_group_delete_courseaccess'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AddField(
            model_name='course',
            name='max_students',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AddField(
            model_name='course',
            name='min_students',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
