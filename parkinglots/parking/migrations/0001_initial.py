# Generated by Django 3.1.6 on 2021-02-26 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import parking.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address1', models.CharField(blank=True, default=None, max_length=1024, null=True, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, default=None, max_length=1024, null=True, verbose_name='Address line 2')),
                ('city', models.CharField(blank=True, default=None, max_length=1024, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, default=None, max_length=1024, null=True, verbose_name='State')),
                ('zip', models.CharField(blank=True, default=None, max_length=12, null=True, verbose_name='ZIP/Postal Code')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('images_id', models.AutoField(primary_key=True, serialize=False)),
                ('image1', models.ImageField(blank=True, upload_to='listing_images/1/%Y/%m/%d/')),
                ('image2', models.ImageField(blank=True, upload_to='listing_images/2/%Y/%m/%d/')),
                ('image3', models.ImageField(blank=True, upload_to='listing_images/3/%Y/%m/%d/')),
                ('image4', models.ImageField(blank=True, upload_to='listing_images/4/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('listing_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('hourly_Rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('day_Rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('overNight', models.BooleanField()),
                ('parking_Pass', models.BooleanField()),
                ('meet_Renter', models.BooleanField()),
                ('vehicles', multiselectfield.db.fields.MultiSelectField(choices=[('C', 'Compact/Sedan'), ('T', 'Truck/SUV'), ('V', 'Van'), ('M', 'Motocycles/Moped'), ('O', 'Motorhomes or Oversized')], max_length=9)),
                ('parking', multiselectfield.db.fields.MultiSelectField(choices=[('R', 'Residential/Private'), ('G', 'Garage'), ('L', 'Parking Lot'), ('S', 'Street Parking'), ('O', 'Other/Misc.')], max_length=9)),
                ('date', models.DateField(validators=[parking.models.validate_date])),
                ('time', models.TimeField()),
                ('is_Rented', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.address')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.images')),
                ('lister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
