# Generated by Django 5.1.1 on 2024-10-03 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(default='SIN DOMICILIO', max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='dni',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='bank_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.bank'),
        ),
    ]
