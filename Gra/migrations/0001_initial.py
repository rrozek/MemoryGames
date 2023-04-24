# Generated by Django 4.1.7 on 2023-04-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewGame",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("player1", models.CharField(blank=True, max_length=15)),
                ("player2", models.CharField(blank=True, max_length=15)),
                (
                    "number_cards",
                    models.CharField(
                        choices=[
                            (4, "4cards"),
                            (8, "8cards"),
                            (16, "16cards"),
                            (32, "32cards"),
                        ],
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]
