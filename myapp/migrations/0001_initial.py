# Generated by Django 5.1.5 on 2025-01-29 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
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
                ("address", models.CharField(blank=True, max_length=1000, null=True)),
                ("name", models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
