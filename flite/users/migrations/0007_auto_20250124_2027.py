# Generated by Django 2.1.9 on 2025-01-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20250124_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdrawal'), ('TRANSFER', 'Transfer'), ('RECEIVED', 'Received')], max_length=50),
        ),
    ]
