# Generated by Django 4.1 on 2022-09-15 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Admin_dashboard", "0015_rename_heading_newsmodel_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newsmodel",
            old_name="description",
            new_name="heading",
        ),
    ]
