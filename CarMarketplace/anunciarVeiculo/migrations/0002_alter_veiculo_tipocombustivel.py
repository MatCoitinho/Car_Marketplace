# Generated by Django 4.2.5 on 2023-09-09 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anunciarVeiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='tipoCombustivel',
            field=models.CharField(choices=[('Gasol', 'Gasolina'), ('alco', 'Alcool'), ('Flex', 'Flex')], default='undefined', max_length=20, verbose_name='Tipo Combustivel'),
        ),
    ]
