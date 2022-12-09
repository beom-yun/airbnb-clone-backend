# Generated by Django 4.1.1 on 2022-12-09 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("rooms", "0004_alter_amenity_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
    ]
