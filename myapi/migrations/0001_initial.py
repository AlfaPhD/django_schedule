# Generated by Django 2.1.2 on 2019-03-17 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AGENDAMENTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATUS', models.CharField(max_length=30, verbose_name='STATUS')),
                ('DATA_INICIO', models.DateTimeField(verbose_name='DATA_INICIO')),
                ('DATA_FIM', models.DateTimeField(verbose_name='DATA_FIM')),
            ],
        ),
        migrations.CreateModel(
            name='CABELELEIRO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL', models.CharField(max_length=100, verbose_name='EMAIL')),
                ('NOME', models.CharField(max_length=30, verbose_name='NOME')),
                ('SENHA', models.EmailField(max_length=200, verbose_name='SENHA')),
                ('CELULAR', models.CharField(max_length=30, verbose_name='CELULAR')),
            ],
        ),
        migrations.CreateModel(
            name='CLIENTE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('APELIDO', models.CharField(max_length=100, verbose_name='APELIDO')),
                ('SENHA', models.CharField(max_length=30, verbose_name='SENHA')),
                ('NOME', models.CharField(max_length=100, verbose_name='NOME')),
                ('EMAIL', models.EmailField(max_length=200, verbose_name='EMAIL')),
                ('CELULAR', models.CharField(max_length=30, verbose_name='CELULAR')),
            ],
        ),
        migrations.CreateModel(
            name='ESTOQUE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUANTIDADE', models.IntegerField(verbose_name='QUANTIDADE')),
                ('DATA_SAIDA', models.DateField(verbose_name='DATA_SAIDA')),
            ],
        ),
        migrations.CreateModel(
            name='PRODUTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=100, verbose_name='NOME')),
                ('QUANTIDADE', models.IntegerField(verbose_name='QUANTIDADE')),
                ('VALIDADE_PRODUTO', models.DateField(verbose_name='VALIDADE_PRODUTO')),
                ('VALOR_UNITARIO', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='VALOR_UNITARIO')),
                ('ESPECIFICACAO', models.CharField(max_length=400, verbose_name='ESPECIFICACAO')),
            ],
        ),
        migrations.CreateModel(
            name='SERVICO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=30, verbose_name='NOME')),
                ('VALOR', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='VALOR')),
            ],
        ),
        migrations.AddField(
            model_name='estoque',
            name='ID_PRODUTO',
            field=models.ManyToManyField(to='myapi.PRODUTO'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='CABELELEIROS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.CABELELEIRO'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='CLIENTES',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.CLIENTE'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='SERVICOS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.SERVICO'),
        ),
    ]
