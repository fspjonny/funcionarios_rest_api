# Generated by Django 4.1 on 2022-08-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastro", "0005_alter_cadastromodel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastromodel",
            name="cargo",
            field=models.CharField(
                choices=[
                    ("JUNIOR", "Júnior"),
                    ("PLENO", "Pleno"),
                    ("SENIOR", "Sênior"),
                ],
                max_length=6,
                verbose_name="Cargo",
            ),
        ),
    ]
