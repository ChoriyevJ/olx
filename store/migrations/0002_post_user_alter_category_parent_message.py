# Generated by Django 4.2.7 on 2024-02-16 14:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True, on_delete=django.db.models.deletion.CASCADE, related_name="children", to="store.category"
            ),
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("content", models.CharField(max_length=511)),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="files/",
                        validators=[
                            django.core.validators.FileExtensionValidator(["pdf", "doc", "docx", "png", "jpeg"])
                        ],
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="images/")),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="messages", to="store.post"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
