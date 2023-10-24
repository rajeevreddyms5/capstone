# Generated by Django 4.2.5 on 2023-10-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chittabook', '0010_rename_savingsaccount_bankaccount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditcards',
            old_name='current_balance',
            new_name='balance',
        ),
        migrations.RenameField(
            model_name='loanaccount',
            old_name='lender',
            new_name='lender_name',
        ),
        migrations.RemoveField(
            model_name='investmentaccount',
            name='interest_rate',
        ),
        migrations.RemoveField(
            model_name='loanaccount',
            name='interest_rate',
        ),
        migrations.AddField(
            model_name='creditcards',
            name='initial_debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
