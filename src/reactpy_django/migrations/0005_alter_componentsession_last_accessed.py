# Generated by Django 4.2.3 on 2023-08-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reactpy_django", "0004_config"),
    ]

    operations = [
        migrations.AlterField(
            model_name="componentsession",
            name="last_accessed",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
