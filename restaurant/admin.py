from django.contrib import admin

from restaurant.models import Food, Booking, FoodPhotos

# Register your models here.

admin.site.register(Food)
admin.site.register(Booking)
admin.site.register(FoodPhotos)

