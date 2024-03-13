# Generated by Django 5.0.2 on 2024-03-13 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_contratolocacao_options_alter_imovel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratolocacao',
            name='valor_aluguel',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
