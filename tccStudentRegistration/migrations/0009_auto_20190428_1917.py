# Generated by Django 2.2 on 2019-04-28 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tccStudentRegistration', '0008_auto_20190428_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='carga_horaria',
            field=models.IntegerField(blank=True, help_text='Carga horária da disciplina', null=True, verbose_name='Carga horária da disciplina'),
        ),
    ]