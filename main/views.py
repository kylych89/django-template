from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth import login, authenticate

from .models import User, Regions, Areas


def indexView(request):
    info = 'Главная страница'

    context = {
        'info': info,
    }
    return render(request, 'main/index.html', context)


def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})


def registerView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            User.objects.create(username=username, password=password, email=email, ).save()
        return redirect('main:index')

    else:
        form = ContactForm()

        context = {
            'form': form
        }
    return render(request, 'main/register.html', context)


def sverdlovView(request):
    sverdlov = Regions.objects.get(id=1)
    name = sverdlov.name
    info = sverdlov.info

    context = {
        'name': name,
        'info': info,
    }

    return render(request, 'main/sverdlov.html', context)


def leninView(request):
    lenin = Regions.objects.get(id=2)
    name = lenin.name
    info = lenin.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/lenin.html', context)


def oktyabrView(request):
    oktyabr = Regions.objects.get(id=3)
    name = oktyabr.name
    info = oktyabr.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/oktyabr.html', context)


def pervomayView(request):
    pervomay = Regions.objects.get(id=4)
    name = pervomay.name
    info = pervomay.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/pervomay.html', context)


def chuiView(request):
    chui = Areas.objects.get(id=1)
    name = chui.name
    info = chui.info
    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/chui.html', context)


def talasView(request):
    talas = Areas.objects.get(id=2)
    name = talas.name
    info = talas.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/talas.html', context)


def yssykkolView(request):
    yssykkol = Areas.objects.get(id=3)
    name = yssykkol.name
    info = yssykkol.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/yssykkol.html', context)


def narynView(request):
    naryn = Areas.objects.get(id=4)
    name = naryn.name
    info = naryn.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/naryn.html', context)


def oshView(request):
    osh = Areas.objects.get(id=5)
    name = osh.name
    info = osh.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/osh.html', context)


def jalalabadView(request):
    jalalabad = Areas.objects.get(id=6)
    name = jalalabad.name
    info = jalalabad.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/jalalabad.html', context)


def batkenView(request):
    batken = Areas.objects.get(id=7)
    name = batken.name
    info = batken.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/batken.html', context)
