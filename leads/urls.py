#from django.contrib import admin
from django.urls import path
from .views import LeadCreateView, LeadDeleteView, LeadDetailView, LeadListView, lead_delete, lead_detail, lead_create, lead_list, lead_update
app_name = "leads"
urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>', LeadDetailView.as_view(), name="lead-detail"),
    path('<int:pk>/update', lead_update, name="lead-update"),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name="lead-delete"),
]
