from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin)
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView, TemplateView)

from .forms import LabTestForm, DoctorForm, BookingForm
from .models import LabTest, Doctor, Booking


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        send_mail(
            name,
            message,
            phone_number,
            ['sanekzh01@gmail.com'],

        )
    context = {
        'title': 'Контакты',
    }

    return render(request, 'main/contacts.html', context)


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LabTestListView(ListView):
    model = LabTest

    def get_queryset(self):
        labtests = LabTest.objects.all()
        return labtests


class LabTestDetailView(DetailView):
    model = LabTest


class LabTestCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = LabTest
    form_class = LabTestForm
    permission_required = "main.add_labtest"
    success_url = reverse_lazy('main:index')


class LabTestUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LabTest
    form_class = LabTestForm
    permission_required = "main.change_labtest"
    success_url = reverse_lazy('main:index')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return True
        else:
            return False


class LabTestDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                        DeleteView):
    model = LabTest
    permission_required = "main.delete_labtest"
    success_url = reverse_lazy('main:index')


class DoctorListView(ListView):
    model = Doctor


class DoctorDetailView(DetailView):
    model = Doctor


class DoctorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    permission_required = "main.add_doctor"
    success_url = reverse_lazy('main:doctor_list')


class DoctorUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                       UserPassesTestMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    permission_required = "main.change_doctor"
    success_url = reverse_lazy('main:doctor_list')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return True
        else:
            return False


class DoctorDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                       DeleteView):
    model = Doctor
    permission_required = "main.delete_doctor"
    success_url = reverse_lazy('main:doctor_list')


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy('main:doctor_list')
