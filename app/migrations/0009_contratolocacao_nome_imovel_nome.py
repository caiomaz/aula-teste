# Generated by Django 5.0.2 on 2024-03-12 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_contratolocacao_valor_aluguel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratolocacao',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='imovel',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
    ]
