# Generated by Django 2.2 on 2019-06-21 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('quantidade', models.IntegerField(verbose_name='quantidade')),
                ('validade_produto', models.DateField(verbose_name='validade_produto')),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='valor_unitario')),
                ('especificacao', models.CharField(max_length=400, verbose_name='especificacao')),
            ],
        ),
        migrations.CreateModel(
            name='servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='valor')),
                ('url', models.URLField(blank=True, max_length=500, null=True, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(verbose_name='quantidade')),
                ('data_saida', models.DateField(verbose_name='data_saida')),
                ('id_produto', models.ManyToManyField(to='website.produto')),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=100, verbose_name='apelido')),
                ('senha', models.CharField(max_length=30, verbose_name='senha')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('email', models.EmailField(max_length=200, verbose_name='email')),
                ('celular', models.CharField(max_length=30, verbose_name='celular')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='cliente', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='cabeleireiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('senha', models.CharField(max_length=200, verbose_name='senha')),
                ('celular', models.CharField(max_length=30, verbose_name='celular')),
                ('ativo', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='cabeleireiro', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30, verbose_name='status')),
                ('data', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='data')),
                ('hora_inicio', models.TimeField(verbose_name='hora_inicio')),
                ('hora_fim', models.TimeField(verbose_name='hora_fim')),
                ('cabeleireiros', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabeleireiros', to='website.cabeleireiro')),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='website.cliente')),
                ('produtos', models.ManyToManyField(blank=True, null=True, related_name='produtos', to='website.produto')),
                ('servicos', models.ManyToManyField(related_name='servicos', to='website.servico')),
            ],
        ),
    ]
