# Generated by Django 4.1 on 2022-09-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Admin_dashboard", "0005_contactmodels"),
    ]

    operations = [
        migrations.CreateModel(
            name="CatalagueModel",
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
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("year", models.CharField(blank=True, max_length=20, null=True)),
                ("heading", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="SAirModel",
        ),
    ]
