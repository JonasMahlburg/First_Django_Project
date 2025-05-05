from django.urls import path
from .views import start_page_view, single_gadget_Int_view,\
      single_gadget_view, GadgedView, RedirectToGadgetView

urlpatterns = [
    path('start/', start_page_view),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgedView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_Int_view),
    path('gadget/<slug:gadget_slug>', GadgedView.as_view(), name="gadget_slug_url"),
]