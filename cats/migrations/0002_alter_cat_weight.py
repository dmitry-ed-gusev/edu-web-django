# Generated by Django 4.1rc1 on 2022-08-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cats", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cat",
            name="weight",
            field=models.FloatField(),
        ),
    ]