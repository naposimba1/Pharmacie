# Generated by Django 2.2.28 on 2022-11-12 12:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='dateexpiration',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
