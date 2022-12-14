# Generated by Django 4.1.1 on 2022-12-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_initial"),
        ("experiences", "0002_initial"),
        ("wishlists", "0002_alter_wishlist_experiences_alter_wishlist_rooms"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="experiences",
            field=models.ManyToManyField(blank=True, to="experiences.experience"),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="rooms",
            field=models.ManyToManyField(blank=True, to="rooms.room"),
        ),
    ]
