from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
starters, main_dish, desserts, drinks = ('Starters', 'Main Dishes', 'Desserts', 'Drinks')


class Food(models.Model):
    menu_choices = (
        (starters, starters),
        (main_dish, main_dish),
        (desserts, desserts),
        (drinks, drinks),
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=1)
    description = models.CharField(max_length=1000, blank=True, null=True)
    category_name = models.CharField(max_length=100, choices=menu_choices, default=main_dish)

    def __str__(self):
        return self.name

    def get_cover_image(self):
        # Corrected from 'foodphotos__set' to 'foodphotos'
        return self.foodphotos.first().image if self.foodphotos.exists() else None


class FoodPhotos(models.Model):
    image = models.ImageField(upload_to='images/')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='foodphotos')
    gallery_description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.food.name}'s photo"

    class Meta:
        verbose_name = 'Food Photo'
        verbose_name_plural = 'Food Photos'


class Booking(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=100, validators=[
        RegexValidator(
            regex=r'^\+?998?\d{9,13}$',
            message="Telefon raqamingizni to'g'ri kiriting. Masalan: +998901234567 yoki 901234567."
        ),
    ], blank=False, null=False)
    no_of_people = models.IntegerField()
    booking_date = models.DateField(format("%d.%m.%Y"))
    booking_time = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.booking_date} - {self.booking_time} : {self.name} for {self.no_of_people}"

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
