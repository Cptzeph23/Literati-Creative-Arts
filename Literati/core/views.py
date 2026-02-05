from django.shortcuts import render, redirect
from .models import Service, ContactMessage
from django.core.mail import send_mail
from django.conf import settings

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


def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send Email
        send_mail(
            subject=f"New Contact Message from {name}",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return redirect('home')
