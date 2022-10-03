from django.urls import path
from .views import ListLocationView, DetailLocationView, DetailRegionView, DetailLeisureView

urlpatterns = [
    path('locations/', ListLocationView.as_view(), name='locations'),
    path('locations/<int:pk>', DetailLocationView.as_view(), name='location'),
    path('regions/<str:slug>', DetailRegionView.as_view(), name='region'),
    path('leisure/<str:slug>', DetailLeisureView.as_view(), name='leisure')
]
