# Generated by Django 4.1 on 2022-08-21 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cadastro", "0008_alter_cadastromodel_cargo_alter_cadastromodel_sexo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cadastromodel",
            name="demissao",
        ),
    ]
