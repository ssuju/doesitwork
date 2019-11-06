from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404

now = timezone.now()

def home(request):
    return render(request, 'rhymesapp/home.html',
                 {'rhymesapp': home})

@login_required
def audio_list(request):
    return render(request, 'rhymesapp/audio_list.html',
                 {'rhymesapp': audio_list})


@login_required
def account_information(request):
    account = Account.objects.filter(created_date__lte=timezone.now())
    return render(request, 'rhymesapp/account_information.html',
                 {'accounts': account})


def signup(request):
    return render(request, 'rhymesapp/signup.html', {'rhymesapp': signup})

def nurseryList(request):
    return render(request, 'rhymesapp/nurseryList.html', {'rhymesapp': nurseryList})

def nurseryPage(request):
    return render(request, 'rhymesapp/nurseryPage.html', {'rhymesapp': nurseryPage})

@login_required
def upgrade(request):
    return render(request, 'rhymesapp/upgrade.html', {'rhymesapp': upgrade})