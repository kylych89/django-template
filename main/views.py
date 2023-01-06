from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactForm, CreateRegionForm, CreateAreasForm
from django.contrib.auth import login, authenticate

from .models import User, Regions, Areas


def baseView(request):
    info = 'Главная страница'
    regions = Regions.objects.all()
    areas = Areas.objects.all()

    context = {
        'info': info,
        'regions': regions,
        'areas': areas,
    }
    return render(request, 'base.html', context)


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
    return render(request, "main/authenticates/login.html", {"form": form})


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
    return render(request, 'main/authenticates/register.html', context)


def createRegionsView(request):
    if request.method == 'POST':
        form = CreateRegionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:base')
        else:
            return HttpResponse('ERROR')
    form = CreateRegionForm
    context = {
        'form': form
    }
    return render(request, 'main/regions/create_region.html', context)


def regionsView(request, pk):
    regions = Regions.objects.all()
    region = Regions.objects.get(id=pk)
    areas = Areas.objects.all()

    context = {
        'region': region,
        'regions': regions,
        'areas': areas,
    }

    return render(request, 'main/regions/regions_view.html', context)


def updateRegionsView(request, pk):
    region = Regions.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateRegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect('main:base')

        return HttpResponse('Invalid data')
    form = CreateRegionForm(instance=region)
    conteext = {
        'form': form
    }
    return render(request, 'main/regions/create_region.html', conteext)


def deleteRegionsView(request, pk):
    region = Regions.objects.get(id=pk)
    region.delete()
    return redirect('main:base')


def createAreasView(request):
    if request.method == 'POST':
        form = CreateAreasForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:base')
        else:
            return HttpResponse('ERROR')
    form = CreateAreasForm
    context = {
        'form': form
    }
    return render(request, 'main/areas/create_areas.html', context)


def areasesView(request, pk):
    areases = Areas.objects.all()
    areas = Areas.objects.get(id=pk)
    regions = Regions.objects.all()

    context = {
        'areas': areas,
        'areases': areases,
        'regions': regions,
    }
    return render(request, 'main/areas/areases_view.html', context)


def updateAreasView(request, pk):
    area = Areas.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateAreasForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('main:base')
        return HttpResponse('Invalid data')

    form = CreateAreasForm(instance=area)

    context = {
        'form': form
    }

    return render(request, 'main/areas/create_areas.html', context)


def deleteAreasView(request, pk):
    area = Areas.objects.get(id=pk)
    area.delete()
    return redirect('main:base')
