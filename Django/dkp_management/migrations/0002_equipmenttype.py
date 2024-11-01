# Generated by Django 4.2.16 on 2024-11-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dkp_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EquipmentType",
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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("武器", "武器"),
                            ("护甲", "护甲"),
                            ("戒指", "戒指"),
                            ("项链", "项链"),
                            ("饰品", "饰品"),
                            ("特殊物品", "特殊物品"),
                        ],
                        max_length=20,
                    ),
                ),
                ("is_rare_drop", models.BooleanField(default=False)),
                ("is_set_item", models.BooleanField(default=False)),
            ],
        ),
    ]
