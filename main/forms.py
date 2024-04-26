from datetime import date

from django import forms
from .models import LabTest, Doctor, Booking


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LabTestForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ('name', 'description', 'price', 'time', 'image')


class DoctorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'specialization', 'experience', 'description', 'image')


class BookingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('doctor', 'date', 'timeslot', 'patient')

    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError(
                'Выберите, пожалуйста, '
                'дату в будущем (завтра или позднее)',
                code='invalid'
            )
        return day
