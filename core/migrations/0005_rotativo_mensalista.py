# Generated by Django 4.1.7 on 2023-04-27 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tabela'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rotativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField(verbose_name='Entrada')),
                ('saida', models.DateTimeField(verbose_name='Saida')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
                ('pago', models.BooleanField(default=False, verbose_name='Pago')),
                ('observacoes', models.CharField(max_length=100, verbose_name='Observacoes')),
                ('id_tabela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tabela', verbose_name='Id da Tabela')),
                ('id_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo', verbose_name='Placa do Veiculo')),
            ],
            options={
                'verbose_name_plural': 'Rotativos',
            },
        ),
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observacoes')),
                ('id_tabela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tabela', verbose_name='Valor do Veiculo')),
                ('id_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo', verbose_name='Placa do Veiculo')),
            ],
            options={
                'verbose_name_plural': 'Mensalistas',
            },
        ),
    ]
