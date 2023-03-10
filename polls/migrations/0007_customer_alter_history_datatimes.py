# Generated by Django 4.1.3 on 2023-02-24 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0006_alter_history_adress"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("mobile", models.CharField(blank=True, max_length=20)),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Accounts",
                "verbose_name_plural": "Accounts",
            },
        ),
        migrations.AlterField(
            model_name="history",
            name="datatimes",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 24, 13, 22, 56, 837793)
            ),
        ),
    ]
