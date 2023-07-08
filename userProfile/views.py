from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Account, Category
from django.contrib.messages import constants as message_constants
from django.db.models import Sum
from . import utils



def profileHome(request):
    accounts = Account.objects.all()

    total = utils.value_sum(accounts, 'value')

    context = {'accounts': accounts}
    
    return render(request, 'home.html', context)

def profileManage(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()

    total = utils.value_sum(accounts, 'value')
    print(total)

    context = {'accounts': accounts, 'total' : total, 'categories': categories}

    return render(request, 'manage.html', context)

def register_account(request):
    name = request.POST.get('name')
    bank = request.POST.get('bank')
    type = request.POST.get('type')
    value = request.POST.get('value')
    icon = request.FILES.get('icon')

    valid = True
    if len(name.strip()) < 2:
        messages.add_message(request, message_constants.ERROR, "The account name needs to have at least 2 letters.")
        valid = False
    if bank == None:
        messages.add_message(request, message_constants.ERROR, "The bank must be valid.")
        valid = False
    if type == None:
        messages.add_message(request, message_constants.ERROR, "The type must be valid.")
        valid = False
    if len(value.strip()) < 1:
        messages.add_message(request, message_constants.ERROR, "The value needs to have at least 1 digit.")
        valid = False

    if valid == False:
        return redirect('manage')
    

    conta = Account(name = name, bank = bank, type = type, value = value, icon = icon)
    conta.save()
    messages.add_message(request, message_constants.SUCCESS, "Your account have been created successfully!")

    return redirect('manage')


def delete_account(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()
    messages.add_message(request, message_constants.SUCCESS, "Your account have been deleted successfully!")
    return redirect('manage')


def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('category')
        essencial = bool(request.POST.get('essencial'))

        if len(name.strip()) < 2:
            messages.add_message(request, message_constants.ERROR, "The category name needs to have at least 2 letters.")

        category = Category(name = name, isEssencial = essencial)
        category.save()

        messages.add_message(request, message_constants.SUCCESS, f"The category {name} have been addedd successfully!")

    return redirect('manage')


def update_category(request, pk):
    category = Category.objects.get(id=pk)
    if category.isEssencial:
        category.isEssencial = False
    else:
        category.isEssencial = True
    
    category.save()
    
    return redirect('manage')