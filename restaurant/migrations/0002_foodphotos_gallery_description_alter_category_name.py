# Generated by Django 5.1 on 2024-08-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodphotos',
            name='gallery_description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Starters', 'Starters'), ('Main Dishes', 'Main Dishes'), ('Desserts', 'Desserts'), ('Drinks', 'Drinks')], default='Main Dishes', max_length=100),
        ),
    ]
