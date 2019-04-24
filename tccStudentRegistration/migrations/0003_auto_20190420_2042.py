# Generated by Django 2.2 on 2019-04-20 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tccStudentRegistration', '0002_auto_20190420_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='alunos',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='disciplinas',
        ),
        migrations.AddField(
            model_name='matricula',
            name='aluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tccStudentRegistration.Aluno'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='disciplina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tccStudentRegistration.Disciplina'),
        ),
    ]