# Generated by Django 3.0.7 on 2020-06-21 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_register', '0003_auto_20200609_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='citydistrict',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_register.CityDistrict'),
        ),
    ]
