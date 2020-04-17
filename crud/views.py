from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Desktop, Laptop, Mobile
from .forms import DesktopForm, LaptopForm, MobileForm


# Create your views here.
def index(request):
    context = {
        'header': ''
    }
    return render(request, 'index.html', context)


# DISPLAY
def display_laptop(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptop',
    }
    return render(request, 'index.html', context)


def display_desktop(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktop',
    }
    return render(request, 'index.html', context)


def display_mobile(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobile',
    }
    return render(request, 'index.html', context)


# ADD
def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            url=''
            if cls==LaptopForm:
                url = '/laptops'
            elif cls==DesktopForm:
                url = '/desktops'
            else:
                url = '/mobiles'
            return redirect(url)
    else:
        form = cls()
        context = {
            'form': form
        }
        return render(request, 'form.html', context)


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_desktop(request):
    return add_device(request, DesktopForm)


def add_mobile(request):
    return add_device(request, MobileForm)


# REMOVE
def del_device(request, cls, pk):
    cls.objects.filter(id=pk).delete()
    items = cls.objects.all()
    context = {
        'items': items,
    }

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def del_laptop(request, pk):
    return del_device(request, Laptop, pk)


def del_desktop(request, pk):
    return del_device(request, Desktop, pk)


def del_mobile(request, pk):
    return del_device(request, Mobile, pk)


# Update
def edit_device(request, cls, model, pk):
    obj = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            url=''
            if model==Laptop:
                url = '/laptops'
            elif model==Desktop:
                url = '/desktops'
            else:
                url = '/mobiles'
            return redirect(url)
    else:
        form = cls(instance=obj)
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)


def edit_laptop(request, pk):
    return edit_device(request, LaptopForm, Laptop, pk)


def edit_desktop(request, pk):
    return edit_device(request, DesktopForm, Desktop, pk)


def edit_mobile(request, pk):
    return edit_device(request, MobileForm, Mobile, pk)