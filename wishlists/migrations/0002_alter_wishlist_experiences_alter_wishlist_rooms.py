# Generated by Django 4.1.1 on 2022-12-10 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0002_initial"),
        ("rooms", "0002_initial"),
        ("wishlists", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="experiences",
            field=models.ManyToManyField(
                blank=True, null=True, to="experiences.experience"
            ),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="rooms",
            field=models.ManyToManyField(blank=True, null=True, to="rooms.room"),
        ),
    ]
