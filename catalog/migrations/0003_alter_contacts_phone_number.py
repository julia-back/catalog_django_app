# Generated by Django 5.1.3 on 2024-12-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_contacts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacts",
            name="phone_number",
            field=models.CharField(max_length=20),
        ),
    ]
