# Generated by Django 4.2.7 on 2024-02-17 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_alter_category_parent"),
        ("option", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostOptionValue",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("value", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RenameField(
            model_name="optionvalue",
            old_name="title",
            new_name="value",
        ),
        migrations.RemoveField(
            model_name="option",
            name="category",
        ),
        migrations.RemoveField(
            model_name="option",
            name="post",
        ),
        migrations.RemoveField(
            model_name="option",
            name="subcategory",
        ),
        migrations.AddField(
            model_name="option",
            name="is_required",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="option",
            name="limit",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="option",
            name="order",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="option",
            name="place_holder",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="option",
            name="regex",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="postoption",
            name="value",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="postoption",
            name="option",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="option.option"),
        ),
        migrations.AlterField(
            model_name="postoption",
            name="post",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="store.post"),
        ),
        migrations.DeleteModel(
            name="CategoryOption",
        ),
        migrations.AddField(
            model_name="postoptionvalue",
            name="post_option",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="option.postoption"),
        ),
    ]