# Generated by Django 4.2.16 on 2024-11-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dkp_management", "0003_raid_boss_dkplog_boss_dkplog_raid"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="total_dkp",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="dkplog",
            name="note",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
