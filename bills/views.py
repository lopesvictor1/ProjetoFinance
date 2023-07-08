from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants as message_constants
from .models import Bill, Payed_Bill
from userProfile.models import Category
from django.utils import timezone
import datetime

def set_bills(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'set_bills.html', context)
    elif request.method == 'POST':
        title = request.POST.get('title')
        category = Category.objects.get(id=request.POST.get('category'))
        description = request.POST.get('description')
        value = request.POST.get('value')
        payment_day = request.POST.get('payment_day')
        valid = True

        if len(title) < 2:
            messages.add_message(request, message_constants.ERROR, 'The title must have at least 2 characters.')
            valid = False
        if category == None:
            messages.add_message(request, message_constants.ERROR, 'You must select one valid category.')
            valid = False
        if len(description) < 1:
            messages.add_message(request, message_constants.ERROR, 'The description must have at least one word.')
            valid = False
        if len(value) < 1:
            messages.add_message(request, message_constants.ERROR, 'The value must be greater than R$ 0,00.')
            valid = False
        elif float(value) < 0.01:
            messages.add_message(request, message_constants.ERROR, 'The value must be greater than R$ 0,00.')
            valid = False
        if len(payment_day) < 1:
            messages.add_message(request, message_constants.ERROR, 'You must select the day of the payment.')
            valid = False

        if valid:
            bill = Bill(
                title=title,
                category= category,
                description= description,
                value = value,
                payment_day = payment_day
            )
            print(bill)
            bill.save()
            messages.add_message(request, message_constants.SUCCESS, 'The Bill has been added to your pannel.') 

        return redirect('set_bills')
    
def show_bills(request):
    MES_ATUAL = timezone.now().month
    DIA_ATUAL = timezone.now().day
    
    bills = Bill.objects.all()

    payed_bills = Payed_Bill.objects.filter(payed__month=MES_ATUAL).values('bill')

    overdue_bills = bills.filter(payment_day__lt=DIA_ATUAL).exclude(id__in=payed_bills)  #payment_day__lt onde lt = less then   Less Then dia atual, quer dizer que já venceu
    
    near_payment_day_bills = bills.filter(payment_day__lte = DIA_ATUAL + 5).filter(payment_day__gte=DIA_ATUAL).exclude(id__in=payed_bills)
    
    others = bills.exclude(id__in=overdue_bills).exclude(id__in=payed_bills).exclude(id__in=near_payment_day_bills)
    print(others)

    context = {'payed_bills':payed_bills, 'overdue_bills':overdue_bills, 'near_payment_day_bills':near_payment_day_bills, 'others': others}
    return render(request, 'show_bills.html', context)

# Criar a função de pagamento das contas e, no html de mostrar as contas, criar uma área para mostrar um relatório de quantas contas estão em cada categoria.
