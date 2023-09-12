# Generated by Django 4.2.5 on 2023-09-12 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCombustivel', models.CharField(choices=[('Gasol', 'Gasolina'), ('alco', 'Alcool'), ('Flex', 'Flex')], default='undefined', max_length=20, verbose_name='Tipo Combustivel')),
                ('modelo', models.CharField(max_length=50, verbose_name='modelo')),
                ('marca', models.CharField(max_length=20, verbose_name='marca')),
                ('ano', models.DateField(verbose_name='Ano Do Modelo')),
                ('cambio', models.BooleanField(default=True, verbose_name='Tipo De Cambio')),
                ('categoria', models.CharField(max_length=10, verbose_name='Categoria Carro')),
                ('qtdPortas', models.IntegerField(verbose_name='quantidade de portas')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7, unique=True, verbose_name='Placa')),
                ('quilometragem', models.CharField(max_length=7, verbose_name='Quilometragem')),
                ('ultimaRevisao', models.DateField(verbose_name='Ultima Revisao')),
                ('status', models.BooleanField(default=False, verbose_name='Status Do Veiculo')),
                ('preco', models.IntegerField(verbose_name='Preco Do Veiculo')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anunciarVeiculos.modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.IntegerField(verbose_name='Pontos')),
                ('img1', models.CharField(max_length=100, verbose_name='imagem um')),
                ('img2', models.CharField(max_length=100, verbose_name='imagem dois')),
                ('descricao', models.TextField(max_length=300, verbose_name='descricao')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anunciarVeiculos.veiculo', verbose_name='veiculo')),
            ],
        ),
    ]
