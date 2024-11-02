# Generated by Django 5.1 on 2024-08-31 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_userprofile_user_perfilusuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilusuario',
            name='saldo_total',
        ),
        migrations.AddField(
            model_name='saldocriptomoedas',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='saldocriptomoedas',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]