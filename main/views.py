from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Service, Appointment, Barber
from .forms import AppointmentForm, CustomUserCreationForm

def barbers(request):
    barbers = Barber.objects.all()
    return render(request, 'main/barbers.html', {'barbers': barbers})

def home(request):
    services = Service.objects.all()
    q = request.GET.get('q')
    if q:
        services = services.filter(name__icontains=q)
    return render(request, 'main/home.html', {'services': services})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def book_appointment(request):
    services = Service.objects.all()
    barbers = Barber.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('my_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'main/book_appointment.html', {
        'form': form,
        'services': services,
        'barbers': barbers,
        'request': request,
    })

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('my_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    services = Service.objects.all()
    return render(request, 'main/book_appointment.html', {'form': form, 'services': services, 'edit_mode': True})

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('-appointment_date')
    barbers = Barber.objects.all()
    services = Service.objects.all()

    # Lấy giá trị lọc từ GET
    barber_id = request.GET.get('barber')
    service_id = request.GET.get('service')
    date = request.GET.get('date')

    if barber_id:
        appointments = appointments.filter(barber_id=barber_id)
    if service_id:
        appointments = appointments.filter(service_id=service_id)
    if date:
        appointments = appointments.filter(appointment_date__date=date)

    return render(request, 'main/my_appointments.html', {
        'appointments': appointments,
        'barbers': barbers,
        'services': services,
        'selected_barber': barber_id,
        'selected_service': service_id,
        'selected_date': date,
    })

@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        appointment.delete()
        return redirect('my_appointments')
    return redirect('my_appointments')