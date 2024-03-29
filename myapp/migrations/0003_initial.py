# Generated by Django 4.1.6 on 2023-04-25 16:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_delete_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annee',
            fields=[
                ('Annee', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('candidat_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('telephone', models.CharField(max_length=20)),
                ('nationalite', models.CharField(max_length=50)),
                ('date_naissance', models.DateField()),
                ('cycle_vise', models.CharField(max_length=50)),
                ('niveau_etude', models.CharField(max_length=50)),
                ('Anne_visee', models.IntegerField()),
                ('filiere_visee', models.CharField(max_length=50)),
                ('lettre_motivation', models.FileField(upload_to='lettre_motivation/')),
                ('cv', models.FileField(upload_to='cv/')),
                ('bulletins', models.FileField(upload_to='bulletins/')),
                ('message', models.TextField()),
                ('candidature_acceptee', models.BooleanField(default=False)),
                ('inscription_reussi', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidat_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('nom', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('nom', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('coefficient', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('candidat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myapp.candidat')),
                ('etudiant_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('moyenne_semestre1', models.FloatField()),
                ('moyenne_semestre2', models.FloatField()),
                ('autorise_passage_classe_superieur', models.BooleanField(default=False)),
                ('Annee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.annee')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.filiere')),
            ],
            bases=('myapp.candidat',),
        ),
        migrations.CreateModel(
            name='Emploi',
            fields=[
                ('emploi_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('jour', models.CharField(max_length=50)),
                ('heures', models.CharField(max_length=50)),
                ('annee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.annee')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.filiere')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_semestre1', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('note_semestre2', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('annee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.annee')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.filiere')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.matiere')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(max_length=50)),
                ('heures', models.CharField(max_length=50)),
                ('absence', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1)])),
                ('annee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.annee')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.filiere')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.etudiant')),
            ],
        ),
    ]
