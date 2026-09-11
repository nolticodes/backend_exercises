from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .dummy_data import gadgets

from django.utils.text import slugify

# Create your views here.

def start_page_view(request):
    return HttpResponse("Hey das hat funktioniert!")

def single_gadget_view(request, gadget_id):
    return JsonResponse({"result": slugify(gadgets[1]['name'])})