# Generated by Django 4.2.3 on 2023-07-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="service",
        ),
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="profile",
            name="linkxdate",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="profile",
            name="miles",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="profile",
            name="owner_full_name",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="profile",
            name="phonenumber",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]