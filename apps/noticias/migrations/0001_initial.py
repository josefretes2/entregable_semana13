# Generated by Django 4.2.3 on 2023-07-19 13:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(blank=True, default='libros/libro_default.png', null=True, upload_to='libros')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.categorias')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]