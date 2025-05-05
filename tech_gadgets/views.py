from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


from .dummy_data import gadgets



def start_page_view(request):
    return HttpResponse("Hey das hat doch gut geklappt!")

def single_gadged_view(request, gadget_id):
    return JsonResponse(gadgets[gadget_id])
