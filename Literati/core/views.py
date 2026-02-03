from django.shortcuts import render, redirect
from .models import Service, ContactMessage

def home(request):
    services = Service.objects.all()

    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        return redirect('home')

    return render(request, 'core/home.html', {
        'services': services
    })