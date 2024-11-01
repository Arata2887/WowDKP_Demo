# Generated by Django 4.2.16 on 2024-11-01 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dkp_management", "0002_equipmenttype"),
    ]

    operations = [
        migrations.CreateModel(
            name="Raid",
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
                ("name", models.CharField(max_length=100)),
                ("version", models.CharField(blank=True, max_length=50, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Boss",
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
                ("boss_id", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "raid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bosses",
                        to="dkp_management.raid",
                    ),
                ),
            ],
            options={
                "unique_together": {("raid", "boss_id")},
            },
        ),
        migrations.AddField(
            model_name="dkplog",
            name="boss",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dkp_management.boss",
            ),
        ),
        migrations.AddField(
            model_name="dkplog",
            name="raid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dkp_management.raid",
            ),
        ),
    ]
