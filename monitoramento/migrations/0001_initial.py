# Generated by Django 4.2 on 2023-05-31 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cronometro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_running', models.BooleanField(default=False)),
                ('seconds', models.IntegerField(default=0)),
            ],
        ),
    ]
