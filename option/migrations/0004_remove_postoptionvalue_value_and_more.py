# Generated by Django 4.2.7 on 2024-02-19 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("option", "0003_alter_option_regex"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="postoptionvalue",
            name="value",
        ),
        migrations.AddField(
            model_name="postoptionvalue",
            name="option_value",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="option.optionvalue"),
            preserve_default=False,
        ),
    ]
