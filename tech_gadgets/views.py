from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.utils.text import slugify
from django.urls import reverse
import json
from django.views import View
from django.views.generic.base import RedirectView
from .dummy_data import gadgets
from .dummy_data import manufactures



def start_page_view(request):
    # return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})
    return render(request, 'tech_gadgets/test.html', {'manufacture_list': manufactures})


class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])
        new_kwargs = {"gadget_slug":slug}
        return super().get_redirect_url(*args, **new_kwargs)

def single_gadget_Int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("no Gadget found")


class RedirectToManufactureView(RedirectView):
    pattern_name = "manufacture_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(manufactures[kwargs.get("manufacture_id", 0)]["name"])
        new_kwargs = {"manufacture_slug":slug}
        return super().get_redirect_url(*args, **new_kwargs)

def single_manufacture_Int_view(request, manufacture_id):
    if len(manufactures) > manufacture_id:
        new_slug = slugify(manufactures[manufacture_id]["name"])
        new_url = reverse("manufacture_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("no Manufacture found")


class GadgedView(View):
    def get(self, request, gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das hat geklappt"})
        except:
            return JsonResponse({"response": "Das war wohl nix!"})
        

class ManufactureView(View):
    def get(self, request, manufacture_slug):
        manufacture_match = None
        for manufacture in manufactures:
            if slugify(manufacture["name"]) == manufacture_slug:
                manufacture_match = manufacture

        if manufacture_match:
            return JsonResponse(manufacture_match)
        raise Http404()
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das hat geklappt"})
        except:
            return JsonResponse({"response": "Das war wohl nix!"})
        

def single_gadget_view(request, gadget_slug=""):
 if request.method == "GET":
       gadget_match = None
       for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget

       if gadget_match:
            return JsonResponse(gadget_match)
       raise Http404()
 if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das hat geklappt"})
        except:
            return JsonResponse({"response": "Das war wohl nix!"})
        

def single_manufacture_view(request, manufacture_slug=""):
 if request.method == "GET":
       manufacture_match = None
       for manufacture in manufactures:
            if slugify(manufacture["name"]) == manufacture_slug:
                manufacture_match = manufacture

       if manufacture_match:
            return JsonResponse(manufacture_match)
       raise Http404()
 if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das hat geklappt"})
        except:
            return JsonResponse({"response": "Das war wohl nix!"})




