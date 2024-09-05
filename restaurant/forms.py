from django import forms

from restaurant.models import Booking


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'no_of_people', 'booking_date', 'booking_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'required': 'required',
                'data-error': 'Firstname is required.',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'E-Mail ID',
                'required': 'required',
                'data-error': 'E-mail id is required.',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Contact No.',
                'class': 'form-control'
            }),
            'no_of_people': forms.Select(choices=[
                ('', 'No. Of persons'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            ], attrs={
                'class': 'form-control selectpicker'
            }),
            'booking_date': forms.TextInput(attrs={
                'placeholder': 'Date',
                'required': 'required',
                'data-error': 'Date is required.',
                'class': 'form-control',
                'type': 'date'
            }),
            'booking_time': forms.TextInput(attrs={
                'placeholder': 'Time',
                'required': 'required',
                'data-error': 'Time is required.',
                'class': 'form-control',
                'type': 'time'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Message',
            })
        }
