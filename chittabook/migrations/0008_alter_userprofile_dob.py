# Generated by Django 4.2.3 on 2023-10-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chittabook", "0007_alter_userprofile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="dob",
            field=models.DateField(blank=True, null=True, verbose_name="Date of Birth"),
        ),
    ]
