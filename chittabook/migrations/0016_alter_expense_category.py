# Generated by Django 4.2.5 on 2023-10-27 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chittabook', '0015_alter_expense_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=256),
        ),
    ]
