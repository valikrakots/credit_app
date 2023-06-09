# Generated by Django 4.2.1 on 2023-06-04 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField()),
                ('seller', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='CreditApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_contract', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visual.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('country', models.CharField()),
                ('phone', models.CharField()),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('quantity', models.IntegerField()),
                ('price_of_one', models.FloatField()),
                ('related_credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visual.creditapplication')),
                ('related_producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visual.producer')),
            ],
        ),
    ]
