# Generated by Django 4.2.1 on 2023-06-04 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='related_credit',
        ),
        migrations.AddField(
            model_name='position',
            name='related_contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visual.contract'),
        ),
    ]