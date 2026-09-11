from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404

from .dummy_data import gadgets

from django.utils.text import slugify

from django.urls import reverse

import json

# Create your views here.

def start_page_view(request):
    return HttpResponse("Hey das hat funktioniert!")

def single_gadget_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("nicht gefunden du spacko")

def single_gadget_slug_view(request, gadget_slug):
    gadget_match = None

    for gadget in gadgets: 
        if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget

    if gadget_match:
        return JsonResponse(gadget_match)
    raise Http404("nichts da")

def single_gadget_post_view(request): 
    if request.method == "POST":
        try: 
            data = json.loads(request.body)
            print(f"received data: {data}")
            return JsonResponse({"response": "Das war was"})
        except:
            return JsonResponse({"response": "Das war wohl nix"})