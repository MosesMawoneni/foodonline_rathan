# Generated by Django 4.2.7 on 2023-11-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_user_is_active_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="city",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="country",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="latitude",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="longitude",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="pin_code",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="state",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
