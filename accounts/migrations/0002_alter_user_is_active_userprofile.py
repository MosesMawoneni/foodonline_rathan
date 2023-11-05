# Generated by Django 4.2.7 on 2023-11-05 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="users/profile_pictures"
                    ),
                ),
                (
                    "cover_photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="users/cover_photos"
                    ),
                ),
                (
                    "address_line_1",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "address_line_2",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("country", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("pin_code", models.CharField(max_length=6)),
                ("longitude", models.CharField(max_length=20)),
                ("latitude", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
