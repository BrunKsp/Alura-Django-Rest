# Generated by Django 4.1.5 on 2023-02-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_rename_aluno_matricula_aluno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
        ),
    ]
