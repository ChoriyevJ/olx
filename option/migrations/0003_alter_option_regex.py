# Generated by Django 4.2.7 on 2024-02-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("option", "0002_postoptionvalue_rename_title_optionvalue_value_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="option",
            name="regex",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
