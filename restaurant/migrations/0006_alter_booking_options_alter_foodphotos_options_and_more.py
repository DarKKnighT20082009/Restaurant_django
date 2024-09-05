# Generated by Django 5.1 on 2024-09-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_booking_food_booking_message_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': 'Bookings'},
        ),
        migrations.AlterModelOptions(
            name='foodphotos',
            options={'verbose_name': 'Food Photo', 'verbose_name_plural': 'Food Photos'},
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
