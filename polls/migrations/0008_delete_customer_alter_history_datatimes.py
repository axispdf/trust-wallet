# Generated by Django 4.1.3 on 2023-02-24 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0007_customer_alter_history_datatimes"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.AlterField(
            model_name="history",
            name="datatimes",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 24, 13, 28, 25, 181365)
            ),
        ),
    ]
