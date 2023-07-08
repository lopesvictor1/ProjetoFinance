from django.shortcuts import render
from userProfile.models import Category
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.messages import constants as message_constants
import json

def set_planning(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'set_planning.html', context)

@csrf_exempt
def update_category_value(request, pk):
    new_value = json.load(request)['new_value']
    category = Category.objects.get(id=pk)

    category.planning_value = new_value

    category.save()

    return JsonResponse({'status': 'success'})

def see_planning(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'see_planning.html', context)