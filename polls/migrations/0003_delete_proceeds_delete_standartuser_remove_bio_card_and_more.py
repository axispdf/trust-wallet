# Generated by Django 4.1.3 on 2023-02-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_bio_card'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Proceeds',
        ),
        migrations.DeleteModel(
            name='StandartUser',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='card',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='fio',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='kredit',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='number',
        ),
        migrations.AlterField(
            model_name='bio',
            name='balance',
            field=models.CharField(max_length=30),
        ),
    ]
