# Generated by Django 4.2.3 on 2023-10-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "chittabook",
            "0005_remove_userprofile_numeric_alter_userprofile_dob_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="dob",
            field=models.DateField(verbose_name="Date of Birth"),
        ),
    ]
