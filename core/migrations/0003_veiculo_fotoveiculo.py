# Generated by Django 4.1.7 on 2023-04-13 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_veiculo_options_veiculo_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='fotoVeiculo',
            field=models.ImageField(blank=True, null=True, upload_to='veiculo_foto', verbose_name=''),
        ),
    ]
