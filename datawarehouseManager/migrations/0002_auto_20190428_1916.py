# Generated by Django 2.2 on 2019-04-28 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datawarehouseManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grr_aluno', models.CharField(help_text='GRR do aluno', max_length=45, verbose_name='GRR do aluno')),
                ('nome_aluno', models.CharField(blank=True, help_text='Nome do aluno', max_length=255, null=True, verbose_name='Nome do aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_curso', models.CharField(help_text='Carga de identificação do curso', max_length=45, verbose_name='Código do curso')),
                ('descricao_curso', models.CharField(blank=True, help_text='Nome do curso', max_length=255, null=True, verbose_name='Descrição do curso')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_disciplina', models.CharField(help_text='Código de identificação da disciplina', max_length=45, verbose_name='Código da disciplina')),
                ('descricao_disciplina', models.CharField(blank=True, help_text='Nome da disciplina', max_length=255, null=True, verbose_name='Descrição da disciplina')),
                ('carga_horaria', models.IntegerField(blank=True, help_text='Carga horária da disciplina', null=True, verbose_name='Carga horária da disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='FatoEvasao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidadeRetencoes', models.IntegerField(blank=True, help_text='Quantidade de retencoes', null=True, verbose_name='Quantidade retencoes')),
                ('ira', models.FloatField(blank=True, help_text='Indice de rendimento academico', null=True, verbose_name='IRA')),
                ('coeficienteEvasao', models.FloatField(blank=True, help_text='Porcentagem de evasao', null=True, verbose_name='Porcentagem de evasao')),
                ('alunoEvasao', models.ForeignKey(blank=True, help_text='Aluno que evadiu', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.Aluno', verbose_name='Aluno')),
                ('cursoEvasao', models.ForeignKey(blank=True, help_text='Curso em que evadiu', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.Curso', verbose_name='Curso evasao')),
            ],
        ),
        migrations.CreateModel(
            name='FatoMatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faltasMatricula', models.IntegerField(blank=True, help_text='Quantidade de faltas da matricula', null=True, verbose_name='Faltas matricula')),
                ('mediaMatricula', models.FloatField(blank=True, help_text='Media final da matricula', null=True, verbose_name='Media matricula')),
                ('coeficienteRetencao', models.FloatField(blank=True, help_text='Porcentagem de retencao', null=True, verbose_name='Porcentagem de retencao')),
                ('alunoMatricula', models.ForeignKey(blank=True, help_text='Aluno que fez a matricula', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.Aluno', verbose_name='Aluno matricula')),
                ('cursoMatricula', models.ForeignKey(blank=True, help_text='Curso em que a matricula foi feita', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.Curso', verbose_name='Curso matricula')),
                ('disciplinaMatricula', models.ForeignKey(blank=True, help_text='Disciplina em que a matricula foi feita', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.Disciplina', verbose_name='Disciplina matricula')),
            ],
        ),
        migrations.CreateModel(
            name='FormaIngresso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_ingresso', models.CharField(help_text='Nome da forma de ingresso do aluno', max_length=255, verbose_name='Descrição ingresso')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicioSemestre', models.DateField(help_text='Data do inicio do semestre', verbose_name='Data do inicio do semestre')),
            ],
        ),
        migrations.CreateModel(
            name='SituacaoMatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_situacao_matricula', models.CharField(help_text='Nome da situação da matrícula', max_length=100, verbose_name='Descrição da situação da matrícula')),
            ],
        ),
        migrations.CreateModel(
            name='StituacaoEvasao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_evasao', models.CharField(help_text='Nome da forma de evasão do aluno', max_length=255, verbose_name='Descrição evasão')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo_ingresso', models.DateField(help_text='Período de ingresso do aluno no curso', verbose_name='Período de ingresso')),
            ],
        ),
        migrations.DeleteModel(
            name='TesteModelo',
        ),
        migrations.AddField(
            model_name='fatomatricula',
            name='semestreMatricula',
            field=models.ForeignKey(blank=True, help_text='Semestre em que a matricula foi feita', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.Semestre', verbose_name='Semestre matricula'),
        ),
        migrations.AddField(
            model_name='fatomatricula',
            name='situacaoMatricula',
            field=models.ForeignKey(blank=True, help_text='Situacao em que a matricula foi concluida', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.SituacaoMatricula', verbose_name='Situacao matricula'),
        ),
        migrations.AddField(
            model_name='fatoevasao',
            name='semestreEvasao',
            field=models.ForeignKey(blank=True, help_text='Semestre em que evadiu', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.Semestre', verbose_name='Semestre evasao'),
        ),
        migrations.AddField(
            model_name='fatoevasao',
            name='situacaoEvasao',
            field=models.ForeignKey(blank=True, help_text='Situacao em que a evasao ocorreu', null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.StituacaoEvasao', verbose_name='Situacao evasao'),
        ),
        migrations.AddField(
            model_name='curso',
            name='disciplinas',
            field=models.ManyToManyField(help_text='Disciplinas relacionadas ao curso', to='datawarehouseManager.Disciplina', verbose_name='Disciplinas'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='forma_ingresso',
            field=models.ForeignKey(help_text='Forma de ingresso do aluno no curso', on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.FormaIngresso', verbose_name='Forma de ingresso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(help_text='Período de ingresso do aluno no curso', on_delete=django.db.models.deletion.CASCADE, to='datawarehouseManager.Turma', verbose_name='Período de ingresso'),
        ),
    ]
