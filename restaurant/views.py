# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import TemplateView, FormView
# from .forms import ReservationForm
# from restaurant.models import Food, FoodPhotos
#
#
# class RestaurantView(FormView, TemplateView):
#     template_name = 'templates/index.html'
#     form_class = ReservationForm
#     success_url = reverse_lazy('index')
#     model = Food
#     context_object_name = 'foods'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # Add other context data for the food items
#         context['images'] = FoodPhotos.objects.all()
#         context['new_foods'] = Food.objects.order_by('-id')[:4]
#         context['starters'] = Food.objects.filter(category_name='Starters')
#         context['main_dish'] = Food.objects.filter(category_name='Main Dishes')
#         context['desserts'] = Food.objects.filter(category_name='Desserts')
#         context['drinks'] = Food.objects.filter(category_name='Drinks')
#
#         if 'form' not in context:
#             context['form'] = self.form_class()
#
#         return context
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Food, FoodPhotos, Booking
from django.core.mail import send_mail
from django.conf import settings


def RestaurantView(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Send email to admin
            subject = 'New Table Booking'
            message = (
                f'Name: {booking.name}\n'
                f'Phone: {booking.phone}\n'
                f'Email: {booking.email}\n'
                f'Date: {booking.booking_date}\n'
                f'Time: {booking.booking_time}\n'
                f'Number of People: {booking.no_of_people}\n'
                f'Message: {booking.message}\n'
            )
            recipient_list = [settings.EMAIL_RECIPIENT_LIST]  # Email to the admin
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

            return redirect('index')
        else:
            print('Form is not valid')
    else:
        form = ReservationForm()

    foods = Food.objects.all().order_by('price')

    context = {
        'form': form,
        'products': foods,
        'images': FoodPhotos.objects.all(),
        'new_foods': Food.objects.order_by('-id')[:4],
        'starters': Food.objects.filter(category_name='Starters'),
        'main_dish': Food.objects.filter(category_name='Main Dishes'),
        'desserts': Food.objects.filter(category_name='Desserts'),
        'drinks': Food.objects.filter(category_name='Drinks'),
    }
    return render(request, 'index.html', context)
