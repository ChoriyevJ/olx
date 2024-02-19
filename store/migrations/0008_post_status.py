# Generated by Django 4.2.7 on 2024-02-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0007_remove_subcategory_options_subcategory_option_values"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACTIVE", "Active"),
                    ("WAITING", "Waiting"),
                    ("NOTACTIVE", "Not active"),
                    ("NOTPAID", "Not paid"),
                    ("DEACTIVED", "Deactived"),
                ],
                default="ACTIVE",
                max_length=15,
            ),
        ),
    ]
