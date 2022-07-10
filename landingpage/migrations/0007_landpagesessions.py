# Generated by Django 3.2.13 on 2022-07-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0006_transparencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandpageSessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exibir_mural', models.BooleanField()),
                ('exibir_biblioteca', models.BooleanField()),
                ('exibir_artigo', models.BooleanField()),
                ('exibir_transparencia', models.BooleanField()),
            ],
        ),
    ]
