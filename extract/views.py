import os
import datetime
from io import BytesIO
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from userProfile.models import Account, Category
from django.contrib import messages
from django.contrib.messages import constants as message_constants
from django.utils import timezone
from django.template import loader
from django.conf import settings
from weasyprint import HTML
from .models import Inputs_outputs
from .utils import io_match


def new_value(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        categories = Category.objects.all()

        context = {'accounts': accounts, 'categories': categories}
        return render(request, 'new_value.html', context)
    elif request.method == 'POST':
        value = request.POST.get('value')
        category = Category.objects.get(id = request.POST.get('category'))
        description = request.POST.get('description')
        date = request.POST.get('date')
        account = Account.objects.get(id = request.POST.get('account'))
        type = request.POST.get('type')

        input_output = Inputs_outputs(
            value = value,
            category = category,
            description = description,
            date = date,
            account = account,
            type = type
        )

        if type == 'I':
            messages.add_message(request, message_constants.SUCCESS, "This Input has been successfully submited.")
            account.value += float(value)
        else:
            messages.add_message(request, message_constants.SUCCESS, "This Output has been successfully submited.")
            account.value -= float(value)

        input_output.save()
        account.save()


        return redirect('new_value')


def view_extract(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()
    ios = Inputs_outputs.objects.all()
    
    accounts_get = request.GET.get('account')
    categories_get = request.GET.get('category')
    io_get = request.GET.get('period')

    if accounts_get:
        ios = ios.filter(account__id = accounts_get)

    if categories_get:
        ios = ios.filter(category__id = categories_get)

    if io_get:
        ios = io_match(io_get, ios)


    context = {'accounts': accounts, 'inputs_outputs': ios, 'categories': categories}
    return render(request, 'view_extract.html', context)


def export_extract(request):
    ios = Inputs_outputs.objects.all()
    if ios == None:
        messages.add_message(request, message_constants.ERROR, "No Inputs/Outputs selected.")
        redirect('view_extract')


    path_template = os.path.join(settings.BASE_DIR, 'templates\partials\extract.html')
    context = {'ios': ios}
    template_render = loader.render_to_string(path_template, context)

    path_output = BytesIO()
    HTML(string=template_render).write_pdf(path_output)
    path_output.seek(0)
    return FileResponse(path_output, filename="extract.pdf")