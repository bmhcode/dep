# Generated by Django 4.2.4 on 2023-08-13 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppelsOffre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('ao', "Appel d'offre"), ('cs', 'Consultations'), ('gg', 'Grie a Grie')], default='ao', max_length=2)),
                ('projet', models.TextField()),
                ('date_début', models.DateField(blank=True, null=True)),
                ('date_fin', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='BET/')),
                ('telephone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=35, null=True)),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=30, null=True)),
                ('observation', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='Entreprise/')),
                ('telephone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=35, null=True)),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=30, null=True)),
                ('observation', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Infos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('libellé', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('adresse', models.CharField(blank=True, max_length=120, null=True)),
                ('telephone', models.CharField(blank=True, max_length=30, null=True)),
                ('fax', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.CharField(blank=True, max_length=35, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='Direction/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='Direction/')),
                ('directeur', models.CharField(blank=True, default='Mr : Directeur', max_length=50, null=True)),
                ('directeurImage', models.ImageField(blank=True, null=True, upload_to='Direction/')),
                ('directeurInformations', models.TextField(blank=True, null=True)),
                ('OpérationsInscrite', models.PositiveIntegerField(default=0)),
                ('personnel', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Etat', models.CharField(choices=[('Récent', 'Récent'), ('Encours', 'En cours'), ('Achevé', 'Achevé')], default='Récent', max_length=12)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Projets/')),
                ('description', models.TextField(blank=True, null=True)),
                ('afficher', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Secteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nombreProjets', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('afficher', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chefService', models.CharField(default='Chef de Service', max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Chef_Service/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chefSubdivision', models.CharField(default='Chef de Subdivision', max_length=50)),
                ('telephone', models.CharField(default='031 31 31 31', max_length=30)),
                ('email', models.CharField(default='Email', max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='ProjetImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Projets/Images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('afficher', models.BooleanField(default=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='depapp.projet')),
            ],
        ),
        migrations.AddField(
            model_name='projet',
            name='secteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Secteurs', to='depapp.secteur'),
        ),
    ]
