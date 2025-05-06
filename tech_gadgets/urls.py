from django.urls import path
from .views import start_page_view, single_gadget_Int_view,\
      single_gadget_view, GadgedView, RedirectToGadgetView, \
      RedirectToManufactureView, ManufactureView, single_manufacture_view,\
      single_manufacture_Int_view

urlpatterns = [
    path('start/', start_page_view),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgedView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_Int_view),
    path('gadget/<slug:gadget_slug>', GadgedView.as_view(), name="gadget_slug_url"),
    
    path('manufactuares/', RedirectToManufactureView.as_view()),
    path('<int:manufacture_id>', RedirectToManufactureView.as_view()),
    path('manufacture/', ManufactureView.as_view()),
    path('manufacture/<int:manufacture_id>', single_manufacture_Int_view),
    path('manufacture/<slug:manufacture_slug>', ManufactureView.as_view(), name="manufacture_slug_url"),
]