from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.utils.text import slugify
from django.urls import reverse
import json



from .dummy_data import gadgets



def start_page_view(request):
    return HttpResponse("Hey das hat doch gut geklappt!")

def single_gadget_view(request, gadget_id):
    new_slug = slugify(gadgets[gadget_id]["name"])
    new_url = reverse("gadget_slug_url", args=[new_slug])
    return redirect(new_url)

def single_gadget_slug_view(request, gadget_slug):
    gadget_match = {"result": "nothing"}

    for gadget in gadgets:
        if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget

    return JsonResponse(gadget_match)


