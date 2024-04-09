# Generated by Django 4.2.10 on 2024-03-25 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logisticians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=100)),
                ('logistician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logisticians.logistician')),
            ],
        ),
    ]
